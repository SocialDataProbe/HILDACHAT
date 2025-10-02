import numpy
import streamlit as st
from google import genai
from google.genai import types
import textwrap
import voyageai
import pandas as pd
import numpy as np
import os
import pickle
import json    
import re
import uuid
import ast
import toml

############################# INITIATE CLIENTS AND FUNCTIONS #############################

# Custom CSS for styling
st.markdown("""
<style>
.current-bot-literature {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 5px;
    border-left: 4px solid #28a745;
    margin: 10px 0;
}

.current-bot-methodology {
    background-color: #d1ecf1;
    color: #0c5460;
    padding: 10px;
    border-radius: 5px;
    border-left: 4px solid #17a2b8;
    margin: 10px 0;
}

.current-bot-variable {
    background-color: #fff3cd;
    color: #856404;
    padding: 10px;
    border-radius: 5px;
    border-left: 4px solid #ffc107;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)


# Initialize Gemini client
client = genai.Client(api_key=st.secrets["genai"]["api_key"])
vo = voyageai.Client(api_key=st.secrets["voyageai"]["api_key"])

# Load the item correspondance data from a file 
with open('Data_Dictionary_Updated.json', 'r') as f:
    json_data = json.load(f)


def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
            #system_instruction=[types.Part.from_text(text="You are a helpful AI assistant.")],
            thinking_config=types.ThinkingConfig(thinking_budget=-1)
        )
    )
    return response.text

def generate_response_nothink(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0,
            #system_instruction=[types.Part.from_text(text="You are a helpful AI assistant.")],
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )
    return response.text

def extract_json_from_response(response):
    # Use regex to extract JSON block inside ```json ... ```
    match = re.search(r"```json\s*(.*?)\s*```", response, re.DOTALL)
    if match:
        json_str = match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON: {e}")
    else:
        raise ValueError("No valid JSON block found in response.")

def get_original_user_query():
    """Finds the first user message in the session state history."""
    for message in st.session_state.messages:
        if message["role"] == "user":
            return message["content"]
    return None # Return None if no user message is found

################################# Search Functions ################################


class BayesianAnalyzer:
   """Handles Bayesian analysis of document similarities."""
   
   def __init__(self):
       pass
   
   def analyze(self, queries, similarities_matrix, metadata, valid_indices, original_query_similarities=None):
       """
       Perform Bayesian analysis on document similarities.
       
       Args:
           queries: List of query strings
           similarities_matrix: 2D array [n_queries, n_docs] of similarity scores
           metadata: List of document metadata dicts (filtered)
           valid_indices: List mapping filtered indices to original doc IDs
           original_query_similarities: Optional array of original query similarities
           
       Returns:
           Dict with bayesian_combined_results
       """
       n_filtered_docs = len(metadata)
       
       # Extract priors from filtered metadata
       priors = np.array([md.get('weights_normalized', 1.0/n_filtered_docs) for md in metadata])
       priors /= priors.sum()
       
       # Calculate posteriors
       joint_likelihoods = np.prod(similarities_matrix, axis=0)
       evidence = np.sum(joint_likelihoods * priors)
       posteriors = (joint_likelihoods * priors) / evidence 
       
       # Sort and format results
       sorted_filtered_indices = np.argsort(posteriors)[::-1]
       
       bayesian_results = []
       for rank, filtered_idx in enumerate(sorted_filtered_indices):
           original_doc_id = valid_indices[filtered_idx]
           result = {
               "doc_id": int(original_doc_id),
               "metadata": metadata[filtered_idx],  # This is already the correct metadata
               "prior": float(priors[filtered_idx]),
               "joint_likelihood": float(joint_likelihoods[filtered_idx]),
               "posterior": float(posteriors[filtered_idx]),
               "individual_similarities": [float(sim[filtered_idx]) for sim in similarities_matrix],
               "bayesian_rank": int(rank + 1),
           }
           if original_query_similarities is not None:
               result["original_query_similarity"] = float(original_query_similarities[filtered_idx])
           bayesian_results.append(result)
       
       return {"bayesian_combined_results": bayesian_results}


class VectorDB:
   def __init__(self):
       self.client = vo
       self.embeddings = []
       self.metadata = []
       self.query_cache = {}
       self.db_path = "vector_db.pkl"
       self.bayesian_analyzer = BayesianAnalyzer()

   def _get_query_embedding(self, query):
       if query in self.query_cache:
           return self.query_cache[query]
       else:
           embedding = self.client.embed([query], model="voyage-2").embeddings[0]
           self.query_cache[query] = embedding
           return embedding

   def _get_filtered_data(self, doc_ids_to_exclude=None):
       """Helper to get filtered data and mappings."""
       if doc_ids_to_exclude is None:
           doc_ids_to_exclude = set()

       n_docs_total = len(self.embeddings)
       valid_indices = [i for i in range(n_docs_total) if i not in doc_ids_to_exclude]

       if not valid_indices:
           return None, None, None

       filtered_embeddings = np.array([self.embeddings[i] for i in valid_indices])
       filtered_metadata = [self.metadata[i] for i in valid_indices]
       
       return valid_indices, filtered_embeddings, filtered_metadata

   def calculate_original_query_similarity(self, original_query, filtered_embeddings):
       """
       Calculate cosine similarity between original query and a filtered set of documents.
       """
       if not original_query or filtered_embeddings.shape[0] == 0:
           return None
           
       query_embedding = self._get_query_embedding(original_query)

       query_norm = np.linalg.norm(query_embedding)
       embedding_norms = np.linalg.norm(filtered_embeddings, axis=1)
       
       dot_products = np.dot(filtered_embeddings, query_embedding)
       similarities = dot_products / (embedding_norms * query_norm)
       
       return (similarities + 1) / 2 # Normalize to [0, 1]

   def search(self, query, original_query=None, doc_ids_to_exclude=None):
       if not self.embeddings:
           raise ValueError("No data loaded in the vector database.")

       valid_indices, filtered_embeddings, filtered_metadata = self._get_filtered_data(doc_ids_to_exclude)

       if valid_indices is None:
           return {"bayesian_combined_results": []}

       queries = [query] if isinstance(query, str) else query
       
       # Embed all queries and calculate similarity matrix
       similarities_matrix = []
       for q in queries:
           query_embedding = self._get_query_embedding(q)
               
           # Calculate similarities for this query
           query_norm = np.linalg.norm(query_embedding)
           embedding_norms = np.linalg.norm(filtered_embeddings, axis=1)
           dot_products = np.dot(filtered_embeddings, query_embedding)
           similarities = dot_products / (embedding_norms * query_norm)
           similarities = (similarities + 1) / 2  # Normalize to [0, 1]
           similarities_matrix.append(similarities)
       
       similarities_matrix = np.array(similarities_matrix)
       
       # Calculate original query similarity if provided
       original_query_similarities = self.calculate_original_query_similarity(original_query, filtered_embeddings)
       
       # Always use Bayesian analysis
       results = self.bayesian_analyzer.analyze(
           queries, 
           similarities_matrix, 
           filtered_metadata,   
           valid_indices,
           original_query_similarities
       )
   
       self.save_db()
       return results

   def save_db(self):
       data = {"embeddings": self.embeddings, "metadata": self.metadata, "query_cache": json.dumps(self.query_cache)}
       with open(self.db_path, "wb") as file:
           pickle.dump(data, file)

   def load_db(self):
       if not os.path.exists(self.db_path):
           raise ValueError("Vector database file not found.")
       with open(self.db_path, "rb") as file:
           data = pickle.load(file)
       self.embeddings = data["embeddings"]
       self.metadata = data["metadata"]
       self.query_cache = json.loads(data["query_cache"])



############### Load Vector Database if exists ###############

vector_db = VectorDB()
vector_db.load_db()


############################ Literature Functions ############################

# Function to enhance query for literature search
def enhance_literature_query(query):
    """Enhanced query processing specifically for literature bot"""
    query_enhancer = textwrap.dedent("""
    # Role
    You are an economist and social scientist specializing in academic literature retrieval.
                                     
    # Task
    Your task is to decompose the user query into semantically distinct, independent statements optimized for retrieval-augmented generation (RAG) against academic abstracts that utilise the Household, Income and Labour Dynamics in Australia (HILDA) Survey.
    
    # Core Requirements:
    1. Semantic Independence: Generate 6-12 statements with zero conceptual overlap. Each must target a unique research dimension, population, or theoretical framework related to the query.
    2. Retrieval Optimization:
       - Use domain-specific academic terminology and research-specific language
       - Incorporate population descriptors (e.g., "working adults," "retirees," "low-income households")
       - Specify measurement approaches (e.g., "subjective well-being scales," "life satisfaction metrics")
    3. Granular Specificity: Each statement should be narrow enough to match distinct abstract content while broad enough to capture relevant papers. Target single concepts or relationships per statement.
    4. Research Context Awareness: Frame statements to align with how academic abstracts are typically described:
       - Research objectives and hypotheses
       - Methodological approaches
       - Population characteristics
       - Key findings or relationships examined
    5. Causally-Distinctive Terminology: Use terms that emphasize the hypothesized causal direction in the user query:
       - For X→Y causation: "X effects on Y," "X impact on Y," "X consequences for Y," "X-induced Y outcomes," "X-driven Y responses"
       - Avoid bidirectional terms: "relationship," "association," "correlation," "link between X and Y"
       - Target forward-causal constructions using distinctive causal vocabulary specific to your domain
    6. Outcome-Focused Framing: Frame the dependent variable as the result/consequence:
        - "X-driven Y outcomes," "Y as consequence of X conditions"
        - "X circumstances affecting Y," "X conditions influencing Y development"
        - Consistently position the hypothesized cause as the driver and effect as the outcome
    7. All abstracts mention the HILDA survey and based in Australia so there is no need to include HILDA or Australia in your statements.
    8. Format: Return as a JSON array of strings.
    
    # User Query
    Here is the user's query:
    {{QUERY}}
    """).replace("{{QUERY}}", query)
    
    return query_enhancer

def lit_prompt(question, abstracts):
    Lit_review_template = textwrap.dedent("""
    # Role
    You are an expert economist and social scientist specializing in academic literature review and synthesis. 
                                          
    # Task
    Your task is to analyze a set of academic abstracts to determine their relevance to the user's question and provide concise summaries of the most relevant papers. To complete this task, please follow these step-by-step Instructions:
    
    ## Step 1: Relevance Classification
    Assign one of the following labels to each abstract based on these precise definitions
    Classify each abstract using these criteria: 
    - Relevant: Directly addresses the user’s research question, mentions the same core variables and the relationship of interest.
    - Somewhat relevant: Touches on concepts and topics related to the user’s research question but do not directly address the same core variables and the relationship of interest.
    - Not relevant: Does not meaningfully address the research question’s core variables and the relationship of interest. 
    Note: All abstracts utilize the HILDA dataset, so focus your relevance assessment on content rather than data source. 
    
    ## Step 2: Summary of Relevant Literature 
    For abstracts classified as "relevant" or "somewhat relevant," provide concise summaries that include: 
    - Research question: What the study aimed to investigate. 
    - Methodology: Key research design, variables, and analytical approach.
    - Main findings: Primary results and their implications for the research question.
    Note: For abstracts classified as Not Relevant, do not provide a summary.
                                          
    # User's Research Question
    Here is the user's question, please analyze it carefully to understand the core variables and the relationship of interest.
                                          
    <question>
    {{QUESTION}}
    </question>
                                          
    # Abstracts
    Here are the abstracts, please read them carefully and only base your answer on them:
                                          
    <abstracts>
    {{ABSTRACTS}}
    </abstracts>

    # OUTPUT GUIDELINES
    1)	If there are no relevant abstracts, feel free to say so.
    2)	Base your entire analysis only on the information contained within the provided abstracts. Do not infer or add any external knowledge.
    3)	Do not mention 'Abstract 1', 'Abstract 2', ... , 'Abstract 50'. Only refer to abstracts by their titles.  
    4)	In your final response there is no need to mention non-relevant abstracts.
    5)  Provide your final answer STRICTLY as a single JSON object. Here is an example of how to format your response. 
        Example JSON format:
        ```json
        [
        {
            "title": "String: Title of the academic abstract",
            "relevance": "String: Classification of relevance (e.g., \"Relevant\", \"Somewhat relevant\")",
            "summary": {
            "research_question": "String: The main research question addressed in the abstract.",
            "methodology": "String: A concise description of the research methods used.",
            "main_findings": "String: The key findings or conclusions of the study."
            }
        }
        ] 
        ```
                                          
    If there are no relevant abstracts, return the following output:
    ```json
        [
        {
            "title": "String: Sorry no abstracts could be found",
            "relevance": "String: N/A",
        }
        ] 
        ```
    """)
    return Lit_review_template.replace("{{QUESTION}}", question).replace("{{ABSTRACTS}}", abstracts)

def extract_top_abstracts_for_lit_prompt(results, question, top_n=60):
    """
    Extract top N abstracts by posterior probability and format for lit_prompt
    
    Args:
        results: Output from vector_db.search() or another Bayesian analysis function
        question: Original user question
        top_n: Number of top abstracts to extract (default: 40)
    
    Returns:
        Formatted prompt string ready for LLM and the list of top documents used.
    """
    if not results or "bayesian_combined_results" not in results:
        return lit_prompt(question, "No abstracts found."), []
    
    # Get top N documents by posterior probability (already sorted)
    top_docs = results["bayesian_combined_results"][:top_n]
    
    if not top_docs:
        return lit_prompt(question, "No abstracts found."), []

    # Format abstracts in markdown
    abstracts_markdown = []
    
    for i, doc in enumerate(top_docs, 1):
        metadata = doc["metadata"]
        title = metadata.get("title", "Title not available")
        abstract = metadata.get("abstract", "Abstract not available")
        
        # Format each abstract with title and abstract text
        abstract_entry = f"""### Abstract {i}
            **Title:** {title}

            **Abstract:** {abstract}

            ---
            """
        abstracts_markdown.append(abstract_entry)
    
    # Join all abstracts
    formatted_abstracts = "\n".join(abstracts_markdown)
    
    # Return the formatted prompt and the list of top docs for later mapping
    return lit_prompt(question, formatted_abstracts), top_docs

# Function to process literature search
def process_literature_search(user_query):
    """Process literature search with enhanced query decomposition"""
    try:
        # Show progress
        with st.spinner("🔍 Analyzing your query and searching literature..."):
            # Generate enhanced query
            enhanced_prompt = enhance_literature_query(user_query)
            
            # Get enhanced statements (assuming generate_response is your LLM function)
            response_text = generate_response_nothink(enhanced_prompt)
            
            # Extract JSON statements
            statements = extract_json_from_response(response_text)
                        
            # Perform vector search (assuming vector_db is available)
            bayesian_results = vector_db.search(query=statements, original_query=user_query)
            
            return bayesian_results
            
    except Exception as e:
        st.error(f"Error processing literature search: {str(e)}")
        return None


################################################ Methodological Functions ################################################

chapter_summary = textwrap.dedent("""
1. Navigatig the HILDA Dataset
This chapter serves as a navigation guide of the HILDA's extensive files. It discusses the structure of the data, variable naming conventions, how the data was collected, how to access the data, and introduces key documentation for finding relevant variables: marked-up questionnaires (showing variable names next to questions), the Subject Level Coding Framework (comprehensive codebook), the Cross Wave Index (condensed version), and the Online Data Dictionary (searchable database). 

2. Overview of the HILDA Survey
This chapter introduces the Household, Income and Labour Dynamics in Australia (HILDA) Survey, outlining its longitudinal design and its primary research areas, which include family dynamics, household formation, income, and employment, to provide context for users new to the survey.
•	2.1 The HILDA Sample and Following Rules: A Summary: This section explains the initial sample selection process, detailing how the sample is designed to be representative of the Australian population, and elaborates on the rules for extending the panel over time, including the definitions and roles of Continuing Sample Members (CSMs) and Temporary Sample Members (TSMs).
•	2.2 Questionnaires: This section describes the various survey instruments used in each wave of the HILDA Survey, including the Household Form (HF), Household Questionnaire (HQ), Person Questionnaires (PQ), and Self-Completion Questionnaire (SCQ), as well as instruments introduced in later waves, providing an overview of the data collection tools.

3. The HILDA Data
This chapter is crucial for users who need to access, understand, and manipulate the HILDA data, as it provides essential information on data access, security requirements, file structure, variable naming conventions, and available support resources.
•	3.1 Ordering the Data: This section guides researchers through the process of applying for and accessing the HILDA data, which is managed through the HILDA Dataverse, and outlines the necessary steps and approvals required.
•	3.2 Cross-National Equivalent File (CNEF): This section introduces the CNEF, a harmonized dataset that includes HILDA data alongside data from other countries, and explains how users can access the HILDA-CNEF data.
•	3.3 A Reminder of the Security Requirements for the Data: This section emphasizes the importance of data security and refers users to the Longitudinal Studies Data Access and Use Guidelines, which detail their obligations as authorized data users.
•	3.4 How the Data Files are Provided: This section specifies the formats in which the HILDA data is provided (SAS, SPSS, and Stata) and mentions the availability of comprehensive documentation to aid in data use.
•	3.5 Structure of the Data Files: This section outlines the structure of the data files provided for each wave, including the Household File, Enumerated Person File, Responding Person File, and Combined File, as well as the Master File and Longitudinal Weights File, which are essential for longitudinal analysis.
•	3.6 Identifiers and Useful Variables: This section explains the various identifiers used to link individuals and households across waves and within households (e.g., xwaveid, _hhrhid, _hhrpid) and provides a list of other useful socio-demographic variables included in the dataset.
•	3.7 Program Library: This section describes a collection of programs available on the HILDA website in SAS, SPSS, Stata, and R formats, designed to assist users in performing common data management and analysis tasks.
•	3.8 PanelWhiz: This section introduces PanelWhiz, a set of Stata/SE Add-On scripts that simplifies the process of working with panel data, making it easier for users to find, retrieve, and manage variables across multiple waves.
•	3.9 Variable Name Conventions: This section explains the systematic naming conventions used for variables in the HILDA dataset, including the use of wave identifiers, subject area codes, and specific data item codes.
•	3.10 Missing Value Conventions: This section details the global codes used to represent missing data in both numeric and text variables, which is crucial for accurate data analysis.
•	3.11 Data with Negative Values: This section explains how data items that can have both positive and negative values (e.g., income, wealth) are provided as two separate variables to accommodate the missing value conventions.
•	3.12 Confidentialisation: This section outlines the methods used to confidentialise the HILDA data, such as withholding certain variables, aggregating variables, and top-coding, to protect the privacy of respondents.

4. Derived Variables
This chapter focuses on explaining the numerous derived variables created from the raw survey data, providing detailed information on how these variables are constructed and categorized to aid in analysis.
•	4.1 Age and Sex: This section explains how age is derived and imputed, and how corrections to birth dates are handled across waves.
•	4.2 History: This section describes history variables, which are accumulated across successive waves to provide longitudinal information on respondents' backgrounds.
•	4.3 Geography: This section details the geographic variables included in the dataset and explains how household addresses are geocoded and assigned to different geographic regions.
•	4.4 Current Education: This section describes variables related to respondents' current educational qualifications and studies, based on the Australian Standard Classification of Education (ASCED).
•	4.5 Current Marital Status and De Facto Relationships: This section explains variables related to respondents' current marital status and de facto relationships, including how these are derived from the relationship grid.
•	4.6 Children: This section describes variables related to the number, age, and residency of children, as well as derived variables related to child maintenance.
•	4.7 Child Care: This section details variables summarizing child care arrangements, including the type of care used, hours of care, and associated costs.
•	4.8 Occupation and Industry: This section explains how occupation and industry variables are coded using standard classifications (ASCO, ANZSCO, ANZSIC).
•	4.9 Other Employment: This section describes other derived employment-related variables, such as unemployment duration, union membership, and casual worker status.
•	4.10 Calculating Hourly Wage Rates: This section provides guidance and example code for calculating hourly wage rates from the available variables.
•	4.11 Employment and Education Calendar: This section describes derived variables related to the employment and education calendar, which provides a detailed record of respondents' activities over time.
•	4.12 Family Relationships: This section explains how family relationships, family types, and income units are derived from the household relationship grid, based on ABS standards.
•	4.13 Health: This section describes derived health variables, including those from the SF-36 and SF-6D health surveys, as well as variables related to height, weight, and body mass index.
•	4.14 Time Use: This section details derived variables related to how respondents allocate their time across various activities.
•	4.15 Personality: This section describes the derivation of personality scales based on the Big Five model of personality traits.
•	4.16 Religion: This section describes the variable on religious classification.
•	4.17 Cognitive Ability Tasks: This section details the cognitive ability tests included in the survey and the derived scores.
•	4.18 Physical Activity and Sleep: This section describes variables related to respondents' physical activity levels and sleep patterns.
•	4.19 Death: This section details variables related to the matching of the sample to the National Death Index, providing information on deceased sample members.
•	4.20 Parents: This section describes variables related to parents' year of birth and death, collected in specific waves.
•	4.21 Main Job Location: This section details variables related to the geographic location of the respondent's main job.
•	4.22 Incentive Payment Method: This section describes variables related to the method used for incentive payments.
•	4.23 Mother’s location of birth: This section describes variables related to the location of the respondent's mother's birth.
•	4.24 Gender Identity: This section describes variables related to the respondent's gender identity.
•	4.25 Income: This section provides a comprehensive overview of the income, tax, and family benefits model used to derive income variables, including details on the imputation methods used to handle missing data.
•	4.26 Wealth: This section describes the wealth model, the imputation methods used for missing wealth data, and the derived wealth variables at both the person and household levels.
•	4.27 Expenditure: This section details the expenditure variables collected in the survey and the imputation methods used to address missing data.
•	4.28 Weights: This section explains the different types of weights provided with the HILDA data (cross-sectional and longitudinal), how they are constructed, and how they should be used in analysis, including information on replicate weights for calculating standard errors.

5. Documentation
This chapter serves as a guide to the extensive documentation available for the HILDA Survey, helping users understand the different types of documentation, how to access them, and how to effectively use them to find the information they need.
•	5.1 Documentation Choices: This section provides advice on how to approach the documentation based on user needs and suggests which documents to print and which to use electronically.
•	5.2 Marked-Up Questionnaires: This section describes the marked-up questionnaires, which are annotated versions of the survey instruments with variable names added next to each question.
•	5.3 Variable Listings: This section details the Subject Level Coding Framework and Cross-Wave Index, which provide comprehensive information about variables, including their codes, the waves in which they were asked, and the files in which they appear.
•	5.4 Frequencies: This section describes the frequency tables provided for each variable, which show the distribution of responses.
•	5.5 Online Data Dictionary: This section introduces the searchable online data dictionary, which allows users to easily access variable descriptions, coding information, and questionnaire text.

6. Data Quality Issues
This chapter provides transparency about known data quality issues in the HILDA Survey, summarizing research on sample representativeness, missing data, and the accuracy of the data, to ensure users are aware of potential limitations.
•	6.1 Summary of Data Quality Issues: This section presents a table summarizing various data quality issues that have been identified in the HILDA data, along with references to relevant technical papers and reports.
•	6.2 Missing Income Data: This section details the extent of missing income data, the imputation methods used to address it, and the impact of missing data on income estimates.
•	6.3 Missing Wealth Data: This section details the extent of missing wealth data, the imputation methods used, and the impact of missing data on wealth estimates.
•	6.4 Missing Expenditure Data: This section details the extent of missing expenditure data and the imputation methods used.

7. The HILDA Sample
This chapter provides a detailed description of the HILDA sample, including the sample design, the reference population, the sampling units, and the sample selection process, to help users understand how the sample was constructed and its representativeness.
•	7.1 Sample Design: This section outlines the overall design of the HILDA sample, including the reference population, the use of households as sampling units, and the multi-stage sampling approach.
•	7.2 Following Rules: This section explains the rules for following sample members over time and how the sample is extended to include new entrants, ensuring the panel remains representative.

8. Data Collection
This chapter provides a comprehensive overview of the data collection procedures used in the HILDA Survey, covering aspects such as pilot testing, the use of dependent data, questionnaire length, interviewer details, fieldwork processes, response rates, and attrition bias.
•	8.1 Pilot Testing: This section describes the pilot testing process, including the Skirmish and Dress Rehearsal, which are used to refine the questionnaires before the main fieldwork.
•	8.2 Dependent Data: This section explains how data collected in previous waves are used in subsequent waves to improve data quality and reduce respondent burden.
•	8.3 Questionnaire Length: This section provides information on the average time taken to complete each questionnaire in each wave.
•	8.4 Interviewers: This section details the number of interviewers used each wave, their training, and the percentage of new interviewers.
•	8.5 Fieldwork Process: This section describes various aspects of the fieldwork process, including the data collection mode, timeline, survey notification material, respondent incentives, call routine, follow-up procedures, refusal aversion strategies, handling of foreign language interviews, and interviewer monitoring.
•	8.6 Response Rates: This section provides detailed information on household and person-level response rates for each wave, including response rates for different subgroups.
•	8.7 Attrition Bias: This section discusses the issue of attrition bias, presenting data on re-interview rates by various sample characteristics and comparing attrition rates to other surveys.

9. HILDA User Training
This chapter informs users about the training courses offered by the Melbourne Institute to help them learn how to effectively use the HILDA data, including an introduction to the survey, a course on data analysis with Stata, and a course on panel data analysis techniques.

""")

def manual_review(question, chapter):
    manual_review_template = textwrap.dedent("""
    Your task is to determine which chapter best aligns with the user's question. Here are the chapters: 
    <manual>
        {{CHAPTER}}
    </manual>

    Here is user's question:
    <question>
        {{QUESTION}}
    </question>
                                            
    Again, your task is to determine which chapter best aligns with the user's question.
                                             
    You may only select one chapter. If you're unsure on which chapter to choose from, explain to the user why you're confused and ask them to clarify.

    At the end of your response, wrap your final response in <category> tags: 
        <category>The chapter number, and only the chapter number, goes here</category>                                           
    """)
    return manual_review_template.replace("{{QUESTION}}", question).replace("{{CHAPTER}}", chapter)

def generate_document_prompt(input_numbers):
    """Generate a prompt string from documents matching numbers in the predefined directory.
    
    Args:
        input_numbers (str): Comma-separated string of numbers to match
    
    Returns:
        str: Formatted prompt containing matched document contents
    """
    numbers = [num.strip() for num in input_numbers.split(',')]
    document_contents = {}
    directory = "usermanual"  # Hardcoded path

    for number in numbers:
        # Find matching files
        matches = [fn for fn in os.listdir(directory)
                  if fn.startswith(f'{number} ')]
        
        if not matches:
            print(f"No match found for number {number}")
            continue
        if len(matches) > 1:
            print(f"Multiple matches for number {number}, using first match")

        # Read first matching file
        file_path = os.path.join(directory, matches[0])
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                document_contents[number] = file.read()
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
            continue

    # Build prompt
    prompt = "##DOCUMENT CONTENT:\n\n"
    prompt += '\n'.join(
        f"--- Section {num} ---\n{content}"
        for num, content in document_contents.items()
    )
    
    return prompt

def chapter_review(question, chapter):
    chapter_review_template = textwrap.dedent("""
    Your task is to use the following chapter from the HILDA user manual to answer the user's question.

    Here is the chapter from the HILDA user manual please read it carefully:
    <chapter>
        {{CHAPTER}}
    </chapter>

    Here is user's question:
    <question>
        {{QUESTION}}
    </question>
                                            
    Again, your task is to use the chapter to answer the user's question.
    You can only base your responses with the content provided in the chapter, do not use any outside knowledge.
    Refer to the chapter as the HILDA user manual. 
    If you're unable to answer the user's question with the chapter's content,
    please inform the user you do not have the information to their question and direct them reach to out to the HILDA team at: hilda-inquiries@unimelb.edu.au.

    Here is some extra context you can apply if the user discusses weights: 
        1. Cross-sectional weights are designed to make each wave's sample representative of the Australian population at that point in time. They account for sample design, non-response, and are benchmarked to known population totals for each specific year.
        2. Longitudinal weights are primarily designed for analyzing changes at the individual level across multiple waves. They're constructed to represent the original population at the beginning of the longitudinal period, not the current population in each wave.
        3. When analysing national representative over time, you're essentially creating a series of representative snapshots of Australia at different points in time, not tracking the same individuals across time.          
        4. Australia's population changes over time due to births, deaths, immigration, and emigration. Cross-sectional weights account for these population changes, while longitudinal weights represent a fixed initial population.                                                  
    """)
    return chapter_review_template.replace("{{QUESTION}}", question).replace("{{CHAPTER}}", chapter)


################################################ Variable Selection Functions ################################################

categories_summary = textwrap.dedent("""
## AD: Australian Defence Force Service History
This category deals with identifying individuals who have served in the Australian Defence Force (ADF). It aims to determine if individuals have ever served, whether they are currently serving or served in the past, and the type of service (Regular or Reserves). It also includes a question related to age, potentially to identify older veterans. The questions are designed to gather information about ADF service history.

## AL: Labour Force - annual leave
This category deals with various types of leave taken by employees in the labor force within the last 12 months. It covers annual leave, sick leave, parental leave, other paid leave (maternity, long-service, paternity, bereavement, family, carers), and unpaid leave. The questions aim to quantify the amount of leave taken in days, weeks, or months, and whether any leave was taken at all.

## AN: Ancestry
This category pertains to the respondent's ancestry, citizenship, residency status, migration journey to Australia, and language proficiency. It includes questions about country of birth, year of arrival in Australia, citizenship and residency status, visa type, refugee/humanitarian status, migration history English proficiency, and whether the respondent is of Aboriginal or Torres Strait Islander origin.

## AP: Activity - Physical
This category focuses on the respondent's physical activity levels, specifically moderate and vigorous physical activity, as well as walking. It measures the frequency (days per week) and duration (minutes per day/week) of these activities, and calculates total physical activity using the Metabolic Equivalent of Task (MET) minutes per week. This category may also include categorical classifications of physical activity beyond these specific types and respondents are also asked to compare their recent physical activity to their usual activity levels.

## BA: Bank accounts
This category gathers information about the respondent's bank accounts, the repondent's childrens bank accounts, including joint accounts and those held solely in their name. It asks about the number of accounts, how respondents' access their accounts, the people with whom accounts are held jointly and their ownership percentage of the joint accounts, the total amount held in these accounts, and whether any accounts are held with non-household members.

## BF: Business
This category focuses on household involvement in businesses. It collects data on business ownership, the share of the business owned by household members, the value of the businesses, and any debt associated with them.

## BI: Business income
This category pertains to income derived from businesses, including dividends, incorporated and unincorporated business income, and whether the respondent worked in their own business, farm, or was a silent partner or trust beneficiary in the last financial year.

## BM: Body mass index
This category collects data related to the respondent's height, weight, desired weight, expected weight, waist measurement, and calculates the Body Mass Index (BMI) and waist-to-height ratio.

## BN: Benefits
This category focuses on government benefits, pensions, and allowances received by the respondent, both currently and in the last financial year. It covers a wide range of benefits, including Age Pension, Disability Support Pension, Carer Payment, Jobseeker Payment, Parenting Payment, and various other allowances and supplements.

## BS: Brothers and sisters
This category gathers information about the respondent's siblings, focusing primarily on those who do not live in the same household (non-resident siblings). The data includes the total number of siblings the respondent has, as well as how many currently live with them. Crucially, for up to 20 non-resident siblings, the data captures detailed information, including the age difference between the respondent and each sibling, whether each sibling is older or younger, the sex of each sibling, and the type of sibling relationship (e.g., biological, adopted, step-sibling, or half-sibling). Furthermore, the data records whether each non-resident sibling is still alive, how far away they live from the respondent, the frequency of in-person contact, and the frequency of contact via telephone, email, or letter."

## CA: Labour Force Calendar
This category records the respondent's labour force activities during the last financial year using a calendar format. It tracks periods of full-time and part-time education, employment in up to 12 different jobs (including start month and year, full-time/part-time status), periods of unemployment, and periods when the respondent was neither employed nor looking for work.

## CC: Child care general
This category focuses on various aspects of childcare for families with children. It includes data on childcare arrangements, responsibility for organizing care, types of care used, and usage patterns while working and not working; government support, receipt and methods of payment for both the Child Care Benefit and Family Tax Benefit; financial aspects, difficulties related to the cost of childcare and estimated annual childcare expenses; challenges in finding suitable care, difficulties encountered in finding childcare that meets various needs (location, cost, quality, specific child needs, hours, etc.); contextual factors, presence of children in the household and household employment status; specific health considerations, including parental decisions regarding child COVID-19 vaccination.

## CE: Childrens education
This category pertains to various aspects of the education and well-being of children within the household related to their schooling. It includes questions about school enrollment, type and year of school, school fees, overall academic achievement, satisfaction with school quality, future educational aspirations (like university), and experiences with bullying (both at school and online). It also covers instances where the school has contacted the household due to the child's behavior.

## CH: Child care during school holidays
This category delves into the specifics of childcare arrangements used by working parents during school breaks. The data encompasses a comprehensive breakdown of care types, including formal options like family day care and vacation care (both at the child's school and elsewhere), as well as informal arrangements such as care provided by relatives (grandparents, siblings, and other relatives, both co-resident and living separately), friends, and neighbors (either in the child's home or the caregiver's home). It also accounts for situations where the child comes to the parent's workplace, is cared for by a non-resident parent, or looks after themself. The category captures the financial aspect by detailing the total weekly cost associated with each specific type of care, culminating in an overall cost for all school-aged children. Furthermore, it quantifies the usage of each care type by providing the total hours per week that children spend in each arrangement. The category also includes options for unspecified or other types of care.

## CN: Non employment related child care
This category deals with childcare arrangements used by parents when they are not working. It distinguishes between children not yet at school and school-aged children and collects data on the types of care used, hours of care used per week, and the associated costs.
This category also focuses on childcare arrangements for children not yet at school while parents are working. It covers the types of care used, the hours of care used per week, and the associated costs.

## CR: Credit cards
This category gathers information about the respondent's credit card usage, including whether they have any credit cards, charge cards, or store accounts, whether these are held jointly with others, the amount owed, and how often they pay off the entire balance.

## CS: Child care during school terms
This category focuses on childcare arrangements during school terms while parents are working. This category captures a wide range of arrangements, from formal childcare services to informal family and friend networks, and even less conventional arrangements like boarding school and self-care.  It details the types of arrangements used, the hours involved, and the costs incurred.

## CT: Cognitive ability tests
This category records the results of cognitive ability tests administered to the respondent, including backwards digit span, symbol digit modalities, and word pronunciation (NART). It also notes any difficulties or assistance received during the tests.

## CV: Coronavirus
This category focuses on the impact of the COVID-19 pandemic on the respondent and their household. It includes questions about health, employment, finances, education, social distancing behaviors, vaccination status, and changes in lifestyle.

## DC: Children deceased
This category collects information about any deceased children of the respondent.  For each deceased child (up to a maximum of 10), we collect the year of birth, year of death, gender, and whether they died before their 15th birthday.  Permission is sought from the respondent before asking these questions.
                                     
## DH: Decision making in household
This category explores how decisions are made within the household regarding various aspects, such as raising children, managing finances, social life, managing finances and leisure time, and work hours. 

## DN: Blood Donation
This category asks whether the respondent has ever donated blood and if they have donated blood in the last 12 months.

## DO: Dwelling and Location Observations / Field Visit Observations
This category records interviewer observations about the dwelling, including security features, external condition, dwelling type, whether it is likely to contain children under 15, and observations about the surrounding environment and location of the dwelling. Refusals about the interview process is included in this section.

## DT: Personal debt
This category gathers information about the respondent's personal debts, including overdue bills, loans from various types of lenders (such as friends and relatives, banks, financial institutions, etc.), car loans, hire purchase loans, Buy Now Pay Later loans, investment loans, and HECS or other student loans.

## DU: Drug usage and substance use
This category asks about the respondent's use of various substances, including illicit drugs and the misuse of prescription medications.  It covers whether the respondent has ever used specific substances, their age of first use, age of last use, and frequency of use. Substances include illicit drugs such as cocaine, ecstasy, hallucinogens, inhalants, marijuana/cannabis, and meth/amphetamine, as well as prescription medications like strong painkillers/opioids and tranquilizers/sleeping pills.  It also includes questions about the use of other illicit drugs not specifically listed.

## EC: Age Confirmation
This category is a simple check to confirm if the respondent is 67 years or older.

## ED: Education
This category covers the respondent's educational background and school experience, including age left school, highest year of schooling completed, country of last school year, qualifications obtained, current enrollment status, field of study, Detailed Qualification Types, bullying, skipping School, Suspension/Expulsion, and Overall Achievement at School.

## EH: Employment history
This category focuses on the respondent's employment history, including time spent in paid work, time spent unemployed and looking for work, time since education, and main activity during time spent neither working nor looking for work.

## ES: Employment status
This category encompasses variables related to both the respondent's current employment status (based on ABS definitions, categorized as broad and detailed) and their broader work history, including whether they have ever engaged in paid work.  Current employment status is categorized as broad (employed, unemployed, not in the labor force) and detailed (employed full-time, employed part-time, unemployed looking for full-time work, unemployed looking for part-time work, not in the labor force).

## FA: Financial assets
This category gathers information about the household's financial assets, including investments, loans to others, other financial investments (bonds, debentures, etc.), and trust funds, as well as the household's expectations for their financial situation in the near future.
                                     
## FF: Food frequency and diet
This category explores the respondent's eating habits and dietary choices. It includes questions about the frequency of eating breakfast, consuming various food groups (breads, cereals, fruits, vegetables, meat, fish, etc.), adding salt to food, and purchasing meals from outlets. It also asks about dieting for weight loss and satisfaction with current weight.

## FI: Attitudes to finances
This category assesses the respondent's attitudes towards borrowing money for various purposes, their ability to raise emergency funds, their role in household financial decision-making, and their comfort and confidence in managing finances.
This category also assesses the respondent's financial well-being through questions about their comfort with their current spending levels, ability to enjoy life due to their financial management, ability to handle unexpected expenses, and whether they are on track to meet future financial needs.
                                     
## FL: Financial literacy
This category measures the respondent's financial literacy through a series of questions testing their understanding of interest rates, inflation, investment risk, and compound interest.  It also includes variables that assess the data collection process, specifically whether respondents received assistance in answering the financial literacy questions. These assistance variables provide context for interpreting the financial literacy scores and understanding the reliability of the responses.

## FM: Family background
This category collects information about the respondent's family background, including parents' employment status and parental seperation/divorce, occupation, education, and country of birth when the respondent was 14. It also asks about the respondent's siblings and whether they lived with both parents during their childhood.

## FS: Food insecurity
This category assesses the respondent's experience of food insecurity in the past 12 months, including worrying about running out of food, eating less than they should, skipping meals, and going without eating for a whole day.

## FT: Children fertility
This category focuses on the respondent's fertility and family planning. It includes questions about current pregnancy status, sterilization, use of birth control, intentions to have more children, and the timing of starting and stopping work around the birth of their most recent child.

## GA: Gambling
This category explores the respondent's gambling habits, including whether they have bet on horse or dog races, sports, played bingo, casino table games, keno, lotto, poker machines, or poker, and the amount of money spent on these activities. It also asks about any negative and social consequences of gambling, such as borrowing money to gamble, feeling guilty about gambling, or experiencing health or financial problems due to gambling.

## GB: Government bonus
This category determines whether the respondent received any Australian Government bonus payments in the last financial year, such as the Back to School Bonus, Farmers hardship bonus, tax credits, temporary supplement to the Education Entry Payment, or the Single Income Family Bonus.

## GC: Grandchildren
This category gathers information about the respondent's grandchildren, including the number of grandchildren, the age of the youngest grandchild, grandparent-grandchild connections, and whether the respondent takes care of any of their grandchildren.

## GH: General health and well-being
This category assesses the respondent's general health and well-being using questions from the SF-36 health survey. It covers physical functioning, role limitations due to physical and emotional problems, bodily pain, vitality, mental health, and social functioning.

## HB: Household bills
This category asks whether the household has any unpaid bills that are now overdue and the total value of these overdue bills. Household bills typically include utilities (electricity, gas, water, internet, phone), council tax, and similar regular expenses related to the home. If the household has no overdue bills (`hbany` is 'no'), then the total value of overdue bills (`hbval`) will be zero or not applicable.

## HC: Children's health
This category focuses on the health of children in the household, including birth weight, whether they see a particular doctor or clinic, number of doctor visits and hospital admissions in the last 12 months, dental health, non-GP healthcare, and out-of-pocket expenses for GP visits.

## HE: Health
This category covers the respondent's health status, including self-assessed health, long-term health conditions, use of aids, need for assistance with daily activities, and whether they have been diagnosed with any serious illnesses.

## HG: Household enumeration grid
This category collects demographic information about each member of the household, including age, sex, relationship to other household members, marital status, employment status, languages spoken, Migration/Visa Status, Long term health condition disability or impairment, National Disability Insurance Scheme (NDIS) agreed package of support, Household Dynamics (Joining/Leaving), variables related to the data collection process itself, and whether they are a full-time or part-time resident of the household.

## HI: Household Income and Government Benefits
This category focuses on the household's income from various sources, including employment, government benefits, investments, and other income streams. It includes detailed information on both current (weekly) and financial year income, categorized by source.  The variables also track various Australian Government payments, such as allowances, pensions, parenting payments, and family tax benefits. Imputation flags are included to indicate the reliability of the data. The category also includes derived variables such as gross, disposable, and regular income, as well as estimated taxes.

## HX: Household expenditure
Household Annual Expenditure (AUD)" provides a detailed record of a household's yearly spending in Australian Dollars. It covers a wide range of expenses, including food, clothing, housing costs (utilities, rates, repairs, insurance), household goods (furniture, appliances, electronics), health, transportation (vehicles, fuel, public transport), communication, recreation, education, insurance, and charitable donations. This comprehensive data allows for analysis of household spending patterns. It also includes questions about the household's ability to make ends meet and any difficulties in paying bills on time.

## IO: Interviewer observations
This category records the interviewer's observations about the interview process, including whether other adults were present, the respondent's cooperation, any documents referred to by the respondent, any difficulties the respondent may have had in understanding or completing the interview, interview method, respondent reactions even after interview completion, and any factors that might affect the quality or interpretation of the interview data.

## IP: Life - intentions and plans
This category explores the respondent's intentions and plans for the future, including plans to change employers, start a new business, return to paid work, stop paid work, move house, and begin a course of study.

## JB: Job characteristics of employed
This category focuses on the characteristics of the respondent's current main job, including occupation, industry, digital work, hours worked, tenure with employer, type of employment contract, work schedule, and whether they work from home. It also covers related aspects such as job satisfaction, workplace characteristics, union membership, training, and job security.

## JD: Job discrimination
This category explores experiences of discrimination in the workplace or during job applications.  Respondents are asked whether they have faced discrimination based on age, ethnicity, gender, long-term health condition or disability, parenting responsibilities, religion, **or any other characteristic**.  The data includes questions about discrimination experienced when applying for jobs and discrimination experienced from employers.  It also includes questions to understand if respondents have been actively applying for jobs and their employment status to provide context for these experiences.

## JO: Opinions about job
This category explores the respondent's opinions about their job, including job satisfaction, work-life balance, job security, and the importance of various job characteristics.

## JS: Job search of those not employed
This category focuses on the job search activities of respondents who are not currently employed. It includes questions about the methods used to look for work, the number of job offers received, starting a business, and the main difficulties faced in finding a job.

## JT: Job training
This category gathers information about any work-related training the respondent has undertaken in the past 12 months, including the aim of the training, the number of days and hours attended, location and timing of training, futur appliccation of training, and whether they contributed to the cost of the training.

## LE: Major life events
This category asks about significant events that have occurred in the past year and have a substantial impact on a person's life. These can include both positive and negative events related to family, relationships, health, work, finances, housing, crime, and legal matters. Examples include: birth or adoption of a child, death of a close friend or family member, marriage, separation, divorce, reconciliation with spouse, moving house, job change (including promotion, being fired/redundant, retirement), major improvements or worsenings in financial situation, serious personal illness or injury, serious illness or injury to a family member, being a victim of property crime or physical violence, having a close family member detained in jail, or being detained in jail yourself, and experiencing a natural disaster that damaged your home.

## LF: Labour Force Status in non-interviewed years
This category collects retrospective data on various aspects of the respondent's labor force status in years when they were not interviewed, including duration of employment and unemployment (in weeks or months), whether they were employed at any point in the year, and whether they actively sought work while unemployed.

## LO: Life opinions
This category explores the respondent's opinions about various aspects of life, including their satisfaction with and importance of aspects such as their overall life, financial situation, health, relationships, employment opportunities, housing, leisure, community, and safety.
This category also explores the respondent's attitudes and values regarding gender roles, work-life balance, childcare, and the importance of a paying job. The questions use a Likert scale to gauge agreement or disagreement with statements related to these topics.
This category also focuses on the respondent's attitudes towards marriage, cohabitation, divorce, having children, diverse family structures (including same-sex relationships and single parenting), gender roles within families, and aspects of the family life cycle.**

## MD: Material deprivation
This category assesses the household's material deprivation by asking whether they can afford a range of essential items and activities, such as a decent and secure home, medical treatment when needed, a telephone, a washing machine, and a week's holiday away from home each year.

## MH: Moving house
This category gathers information about the respondent's plans to move house, including when they expect to move, the reasons for moving, and whether they have moved in the past 10 years.

## MO: Mutual obligations
This category pertains to activities that individuals may be required to undertake by Centrelink or an employment services provider in order to receive unemployment benefits. It includes questions about the types of activities undertaken, the time since the last activity, and whether the respondent is currently undertaking any of these activities.

## MR: Marital relationships
This category focuses on the respondent's marital history, including the number of times they have been legally married, the duration of each marriage, the reasons for separation or divorce, and whether they lived together before marriage.

## MV: Motor vehicles
This category gathers information about the motor vehicles owned by household members, including the number of cars, vans, trucks (often grouped as 'Group 1 vehicles'), motorcycles, scooters, recreational vehicles, and other motor vehicles. It includes data on the number of each type of vehicle and their current worth.

## NB: Non-cash benefits
This category covers non-cash benefits received by the respondent from their current main job, other current jobs, and incorporated businesses. It includes benefits such as childcare, car parking, computers, housing, low-interest loans, motor vehicles, telephone, shares, and superannuation contributions.

## NC: Non-resident children
This category collects information about the respondent's children who do not live in the same household, including their age, sex, whether they have children of their own, their marital and employment status, frequency of contact, and financial support provided or received.

## NL: Not in labour force
This category focuses on respondents who are not currently in the labor force. It includes questions about their main activity, reasons for not looking for work, whether they would like a job, and their ability to start work if offered a suitable job.

## LM: Literacy and Numeracy
This category assesses the respondent's self-perceived mathematical skills related to numeracy, through self-rated questions about their ability, comfort, and confidence in working with numbers and calculations.  Some questions may involve comparative self-assessment (e.g., compared to the average Australian) and explore comfort levels in specific practical numeracy tasks.
This category also relates to an individual's self-assessed reading ability, habits, and attitudes, including the potential impact of health conditions on reading and a comparison of their reading skills to the average Australian. They cover aspects of enjoyment, perceived skill level, and necessity of reading.

## NR: Relationships - defacto: non co-residential
This category pertains to individuals who are in an intimate ongoing relationship with someone they do not live with. It includes questions about the duration of the relationship, whether they have made a definite decision not to live together, the frequency of contact, and characteristics of the non-co-resident partner such as their education, employment, and location.

## OA: Other assets
This category gathers information about other assets owned by household members, such as antiques, works of art, cemetery plots, substantial assets, collectibles, and life insurance policies.

## OI: Other income
This category covers various sources of income other than wages and salaries, including dividends, royalties, interest, rental income, lump sum payments from superannuation, regular superannuation/annuity payments, inheritances, workers' compensation, redundancy payments, life insurance, and transfers from other persons.

## OP: Other property
This category focuses on properties wholly or partially owned by household members other than their primary residence. It includes questions about the number of other properties owned, the type of property, whether it is rented out, any loans on the property, and the approximate value of these properties.

## PA: Parenting
This category explores the respondent's experiences and attitudes towards parenting. It includes questions about the difficulty and joy of parenting, work-family balance, and the division of childcare tasks between partners.

## PD: Kessler-10
This category contains the results of the Kessler-10 psychological distress scale, which measures symptoms of anxiety and depression.

## PE: Pets
This category records information related to pet ownership within the household. This includes whether the household owns pets, and if so, the types of pets they own.  It covers a range of pet types, from common animals like cats and dogs to less common pets like alpacas and lizards.  The category also includes response categories such as 'Don't know' and 'Refused' to account for data collection outcomes, and an 'Other' category for pets not explicitly listed.

## PH: Private health insurance
This category gathers information about the respondent's private health insurance coverage, including the type of cover, when it was commenced (including considerations like the Lifetime Health Cover incentive), their history of private health insurance (including past and dropped cover), and their possession of various government health-related cards such as Commonwealth Seniors Health Cards, Health Care Cards, Pensioner Concession Cards, and Department of Veterans Affairs cards. It also covers whether they have been admitted to hospital as a day patient or overnight patient in the last 12 months, including the number and type of admissions.

## PJ: Previous job
This category focuses on the respondent's previous job if they have changed jobs since the last interview or if they are currently unemployed. It includes questions about the occupation, industry, hours worked, and reason for leaving the previous job.

## PN: Life - personality
This category assesses the respondent's personality traits, focusing on a detailed assessment of numerous specific personality traits and facets, including those related to the Big Five personality dimensions (openness, conscientiousness, extraversion, agreeableness, and emotional stability/neuroticism). It also covers traits related to risk-taking.
                                     
## PR: Partnering / relationships
This category covers the respondent's history of cohabiting relationships (living with a partner). It includes the number of times they have lived with someone in a de facto relationship, the duration of these cohabitations, and start and end dates for current and past cohabiting relationships.
                              
## PS: Parent status
This category gathers information about the respondent's parents, including whether they are still alive, their age, marital status (whether still living together), detailed living arrangements (including living in respondent's household, nursing home, supported accommodation, or with others, and distance from respondent), aspects related to their functional status and care needs (assessed through limitations in activities and who provides care), and frequency of contact.  The data also captures details about who lives with and who cares for the parents, including various family members, professional carers, and institutional staff.

## PW: Personal wealth
This category focuses on the respondent's personal wealth, including own and joint bank accounts, credit card debt, other debts, and superannuation.

## RC: Resident children
This category collects comprehensive information about children (including natural, adopted, step, foster, and grandchildren) living in the respondent's household, including their age, sex, school attendance, and whether they have another parent living elsewhere. The category also captures extensive details regarding financial support arrangements between parents (including amounts, frequency, and types of support), parental work history before the child's birth, parental leave taken, details of contact and visitation with non-resident parents, the resident parent's opinion of that contact, and specifics about childcare responsibilities within the household.

## RE: Religion
This category asks about the respondent's religious affiliation, frequency of attendance at religious services, and the importance of religion in their life.

## RG: Relationship grid
This category records the relationships between all members of the household, using a grid format to indicate the relationship of each person to every other person in the household.

## RW: Weights
This category contains the replicate weights assigned to each respondent and household, which are used for statistical analysis to account for the complex sampling design of the survey. 
This category also contains longitudinal weights assigned to individuals enumerated in the survey sample. These weights are used for statistical analysis to account for the complex sampling design and are provided for both enumerated persons (regardless of response status) and specifically for responding persons.  They are crucial for ensuring the survey data accurately represents the target population over time.
This category also contains Cross-sectional weights are designed to make each wave's sample representative of the Australian population at that point in time. They account for sample design, non-response, and are benchmarked to known population totals for each specific year.
                                     
## SA: Superannuation
This category focuses on the respondent's superannuation arrangements, including whether they have any superannuation funds, the type of fund, the value of the fund, and whether they make personal contributions to their superannuation. It also includes, Employer contributions, Specific types of funds, and Specific types of funds. 

## SC: Self completion
This category records information about the self-completion questionnaire, including the date it was completed and whether the SCQ record matches the PQ record.

## SK: Skills and abilities
This category assesses the respondent's skills and abilities, including their ability to read and speak languages other than English, their computer skills, practical skils, reading ability, and their perceived minimum level of education required to satisfactorily carry out their current job.

## SL: Sleep
This category explores the respondent's sleep patterns, including the amount of sleep they get on workdays and non-workdays, whether they take naps, and any difficulties they have with sleeping.

## SN: Household Screening
This category contains information collected during the initial household screening process.  It includes demographic details such as the number of people living in the household, birthplace (whether anyone was born outside of Australia), and recent immigration history (arrival in Australia after 2011 and permanent residence visa status).  Furthermore, it captures information related to the screening process itself, such as whether a competent respondent was available, if an alternative respondent was needed, and the overall outcome of the screening.  Language diversity within the household, specifically whether a language other than English is spoken, is also recorded.

## SS: Salary sacrifice
This category gathers information about the respondent's salary sacrifice arrangements, including the types of benefits received through salary sacrifice, the amount of salary sacrificed, and the frequency of contributions.

## TC: Total children
This category records the total number of children the respondent has ever had, including those who have died, stillbirths and miscarriages, and the number of resident and non-resident children.

## TI: Total income
This category covers the respondent's total income from all sources, including wages and salaries, business income, investments, government benefits, and other income.

## TX: Taxes
This category encompasses estimated tax-related financial data reported by respondents for a financial year. It includes estimated taxes on both regular income and total income. This category captures both tax liabilities and mechanisms that reduce tax liabilities, related to both regular and total income within a financial year.

## UJ: Job history of those not in paid employment
This category focuses on the job history of respondents who are not currently in paid employment. It includes questions about their last job, including the occupation, industry, hours worked, and reason for leaving the job.

## WC: Labour force - leave / workers compensation
This category deals with absences from work due to workers' compensation, including the number of days absent, the amount of workers' compensation received, and whether any paid workers' compensation was received in the last 12 months.

## WS: Wage and salaries
This category gathers detailed information about the respondent's wages and salaries, including their current weekly gross wages and salary from all jobs, their main job, and other jobs. It also asks about deductions from their pay, such as taxes, superannuation contributions, and health fund contributions.

## YE: Youth - employment
This category focuses on the employment aspirations and expectations of young people. It includes questions about the importance of various job characteristics, such as job security, income, flexibility, and the opportunity to help others.

## YH: Youth - education
This category captures young people's self-reported academic performance in English, mathematics, and overall school achievement specifically during their last year (or most recent year if not completed in a standard sequence) of high school.

## YI: Youth - importance
This category explores the importance that young people place on various aspects of life, such as having a successful career, having children, getting more education, keeping fit, having friends, and making money.

## YP: Youth - property
This category focuses on individuals, particularly young adults, and their experiences, plans, intentions, and concerns regarding first-time home ownership. It includes questions about whether they have ever owned a residential property, their age at first purchase, whether they are currently saving for a deposit, their expectations about when they will buy a property, and their worries about affordability.

## YS: Youth - life satisfaction
This category assesses young people's satisfaction with various aspects of their lives, such as their spare time activities, physical appearance, education, friends, job prospects, living arrangements, love life, and financial situation.

## HW: Household wealth
This category contains detailed information on household wealth in Australian Dollars (AUD), including a comprehensive breakdown of assets and debts. It covers financial assets like bank accounts, investments, and superannuation, as well as non-financial assets such as property, vehicles, and collectibles. The dataset also includes various debt categories, including credit card debt, mortgages, and other loans, along with overall net worth calculations. Imputation flags are included to indicate where values have been estimated or imputed.

## HS: Housing
This category relate to housing characteristics and financial arrangements of households, including details on home ownership, mortgages, loans, rent, board payments, property value, and debt. The variables cover aspects such as the number of bedrooms, loan types and repayment schedules, refinancing, ownership details, and whether household members pay board to one another. They contain information about the amounts, frequencies, and institutions associated with mortgages and loans, as well as information relating to tenure type.
                                     
## RP: Residential property
This category relate to an individual's history of residential property ownership, including the age of first acquisition, current ownership status, recent difficulties with repayments, and reasons for selling a property within the last four years.
                                     
## IH: Housing Insurance 
This category relate to home and contents insurance in a given housing unit. They cover whether the building and/or contents are insured, reasons for not being fully insured or having no insurance, actions taken due to financial constraints, perceived risks of various events (flood, fire, storm, theft), and understanding of local risks before moving in. The variables explore coverage details, reasons for increasing insurance, and reasons for stopping insurance. 
                                     
##  LS: Lifestyle
This category cover a wide range of lifestyle factors, including personal habits, social interactions, sociability, household tasks, relationship dynamics, computer use, neighborhood perceptions, health behaviors, personal control, and community participation. They assess areas such as achievement and other motivation, cognitive activities, smoking and alcohol consumption, time allocation, social support, financial habits, self-control, and trust in others.
This category also represent an individual's self-reported resilience, encompassing their ability to adapt to change, recover from setbacks, and their comfort level with seeking and accepting help.                                                                                                                              
                                     
## IC: Intentions to have children
This category relate to individuals' intentions to have children, including factors influencing their decisions, their expectations and preferences regarding future children, and the timing of having children. The variables cover aspects like age, financial considerations, career impacts, personal values, desired family size, and preferred gender of future children.
                                     
## HH: Household information.
This category describes household-level information from a longitudinal study, covering demographics such as household composition (ages of members, number of children, family type), socioeconomic indicators (SEIFA indices, remoteness, unemployment rate), geographic data (state, statistical region), interview details (mode, length, interviewer ID, response status), and household movement. 
                                     
## RT: Retirement intentions
This category relate to an individual's retirement status, plans, and experiences. They cover a wide range of aspects, including the timing and reasons for retirement (or planned retirement), financial considerations such as superannuation use and income needs, changes in work patterns during a transition to retirement, reasons for coming out of retirement, satisfaction with retirement, and the influence of partners and external factors on retirement decisions. The variables also explore sources of retirement advice, and coping strategies for reduced income.
                                     
## OR: Other relationships
This category describe characteristics of individuals' current and past de facto relationships (cohabitation without marriage), including the duration of relationships, when they began, the number of such relationships, and attitudes toward marriage within the context of these relationships. They cover both current and previous cohabiting partnerships, as well as future marriage intentions.

## ID: Identification
This category relates to the identification of individuals within the study, including unique identifiers, and any relevant codes used to track participants over time.
""")

def categories_review(question, categories):
    categories_review_template = textwrap.dedent("""
    Your task is to determine which categories are related to the user's question and population characteristics. 
    Include demographic characteristics if they are related to the user's question. List your final response as a python list with the categories abbreviations.

    Here are the categories, please read it carefully:                                      
    <categories>
        {{CATEGORIES}}
    </categories>

    Here is the user's question, please read it carefully:
    <question>
        {{QUESTION}}
    </question>

    Remember, your task is to determine which categories are related to the user's question and population characteristics. 
    Include demographic characteristics if they are related to the user's question. List your final response as a python list with the categories abbreviations.   
    Thus, your final response should, for example, have the following format:
    ['EC','HG',...]
    Lastly, you must select the 12-18 most promising categories in your final response.    
    """)

        #Lastly, you may only select the 15 most promising categories in your final response.  
    return categories_review_template.replace("{{QUESTION}}", question).replace("{{CATEGORIES}}", categories)

def variable_selection(question, variables):
    variable_selection_template = textwrap.dedent("""
    Your task is to select relevant variables from a list of variables according to the users question.
   
    The variables come from the The Household, Income and Labour Dynamics in Australia (HILDA) Survey, a 
    household-based longitudinal study that collects valuable information about economic
    and personal well-being, labour market dynamics and family life.
    The Household, Income and Labour Dynamics in Australia (HILDA) Survey is a household-based
    longitudinal study that collects valuable information about economic and personal wellbeing, labour
    market dynamics and family life. It aims to tell the stories of the same group of Australians 
    over the course of their lives. 


    Here are the variables, please read them carefully and select the most relevant to the user's question:                                      
    <variables>
        {{VARIABLES}}
    </variables>

    Here is the user's question, please read it carefully:
    <question>
        {{QUESTION}}
    </question>
                                                  
    When choosing relevant variables, you should always favour variables that are 'DV' in the question form
    and are available for the most waves. 
                                                  
    Income variables are an edge case that needs extra information on how to answer. Please follow these instructions
    when answering questions related to income. The income variables are created through the financial year income
    model. Here is the flowchart that represents that model:
    <income>
        -----------------------------------------------------------------------------------------

        START:

        [ FY wages and ]  -->
        [ salary        ]

        [ FY business   ]  -->
        [ income         ]

        [ FY investment ]  -->
        [ income         ]

        [ FY regular private ] -->
        [ pensions         ]

                            ----------------------------------------------------> [ FY regular market  ]
                                                                            [ income              ]

        -----------------------------------------------------------------------------------------

        [Australian       ]                      [Australian             ]
        [Government       ]  -------------------> [Government             ] -->  [FY Australian public ]
        [pensions         ]                      [income support         ]      [transfers           ]
        [                 ]                      [payments               ]
        [Australian       ]                      [                        ]
        [Government       ]                      [Australian             ]
        [Parenting Payments]                      [Government non-        ]
        [                 ]                      [income support         ]
        [Australian       ]                      [payments                ]
        [Government       ]                      [                        ]
        [allowances        ]
        [                 ]
        ---------------------
        [Estimated family  ]
        [payments          ]
        [                 ]
        ---------------------
        [Estimated         ]
        [Australian        ]
        [Government Bonus  ]
        [payments          ]
        ---------------------
        [Other non-income  ]
        [support payments, ]
        [incl. Mobility and]
        [Carer Allowances  ]
        [                 ]
        ---------------------
        [Other domestic    ]
        [government benefits]
        [and Australian     ]
        [Government benefits]
        [NEI to classify   ]
        [                   ]
        ---------------------
        [Other regular     ]
        [public (including ]
        [scholarships)     ]
        [                 ]
        ----------------------
        [Foreign pensions    ]     ----->  [ FY regular private ]
        [                    ]                [ transfers           ]

                                    \
                                    ----------------> [FY regular private    ]
                                                        [income               ] --> [FY gross regular     ]  ---> [ FY estimated taxes    ]  ---> [FY disposable regular ]
                                                                                    [ income              ]       [ on regular income     ]       [income              ]
                                                                                    /
                                                        -----------------------------------
                                                    /
        [FY irregular income ] <-------------------


                                                                            --------------------------------------> [ FY gross total      ] --->[ FY estimated taxes     ]  ---> [ FY disposable total]
                                                                                                                    [ income              ]     [   on total income      ]     [   income            ]
        END   
    </income> 
                                                  
    You can choose either household income or total income. Choose houeshold if the user's question is related to the household level and choose total income if its related to the individual level. These variables are seperate and you cannot choose both, if you don't know which one to choose you can suggests both.   
    Whatever the income variable choice is, please remind the user that subtraction of the negative income variable from the positive income variable gives the full distribution of that income variable. Remember to emphasize the subtraction.                                            

    Finally, always list multiple relevant variables for the user in your final response and let them decide which is most is most relevant.
                                                  
    # Formatting 
    Please report all relevant variables using the following consistent format.
    Repeat the entire structure (from the variable name heading to the Waves bullet point) for every variable you chose.
                                                  
    *[Variable Name]*: [Brief Description/Source of Variable]

    Categories:

        [Value/Label 1]: [Description]

        [Value/Label 2]: [Description]

        [Value/Label 3]: [Description]

        [Continue listing categories as needed...]

    Relevance: [Brief explanation of what this variable is used for, why it's important, and which values/labels might be of particular focus for a specific analysis.]

    Waves: [Range of waves/data points the variable is available for, e.g., 1-23 (available for all waves), 10-15 only, etc.]
                                                                                                    
    """)
    return variable_selection_template.replace("{{QUESTION}}", question).replace("{{VARIABLES}}", variables)



############################ Streamlit ############################

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_bot" not in st.session_state:
    st.session_state.current_bot = "Literature"
if "show_preface" not in st.session_state:
    st.session_state.show_preface = True
if "selected_papers" not in st.session_state:
    st.session_state.selected_papers = []
if "selected_variables" not in st.session_state:
    st.session_state.selected_variables = []

# Create sidebar for buttons
with st.sidebar:
    st.header("Specializations")
    # Bot selection buttons
    if st.button("📚 Literature", use_container_width=True):
        st.session_state.current_bot = "Literature"
    if st.button("🔬 Methodology", use_container_width=True):
        st.session_state.current_bot = "Methodology"
    if st.button("📊 Variable Selection", use_container_width=True):
        st.session_state.current_bot = "Variable Selection"

   
    st.divider()
   
    # Display current bot with custom styling
    if st.session_state.current_bot == "Literature":
        st.markdown(f'<div class="current-bot-literature">Currently chatting with: 📚 <strong>{st.session_state.current_bot}</strong></div>', unsafe_allow_html=True)
    elif st.session_state.current_bot == "Methodology":
        st.markdown(f'<div class="current-bot-methodology">Currently chatting with: 🔬 <strong>{st.session_state.current_bot}</strong></div>', unsafe_allow_html=True)
    elif st.session_state.current_bot == "Variable Selection":
        st.markdown(f'<div class="current-bot-variable">Currently chatting with: 📊 <strong>{st.session_state.current_bot}</strong></div>', unsafe_allow_html=True)

    # Clear chat history button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.selected_papers = []
        st.session_state.show_preface = True
        st.session_state.selected_variables = []
        st.rerun()

# App title
st.title("🤖 HILDA Research Assistant")

# Display preface only if no messages exist AND show_preface is True
if st.session_state.show_preface and len(st.session_state.messages) == 0:
    st.markdown("""
    ### Welcome to the HILDA Research Assistant! 👋
   
    **How to use this application:**

    1. **Select an AI Specialization** from the sidebar on the left. The **Literature** bot is selected by default.
    2. **Literature**: Ask research questions to find relevant academic papers that use the HILDA Survey. Here are some example questions to get you started:
        - Does education affect income inequality?
        - How does income influence mental health?
        - What is the impact of housing affordability on family well-being?
    3. **Methodology**: Discuss the methods and approaches relevant to your research questions. Some example questions include:
        - What weighting method should I use for my analysis?
        - How is the income variable crafted?
        - Can you explain the sampling design of the HILDA Survey?
    4. **Search Variables**: Identify and refine the key variables related to your research. Feel feel to ask broad or specific queries, such as:
        - Which variables are relevant for studying the impact of education on employment outcomes?
        - Mental health
        - Income inequality
        - Income effect on family well-being
    5. **Switch bots** or **clear the chat history** at any time using the sidebar controls.

    **Note**: I'm a Question and Answering Bot, not a Chat Bot! That means I'm designed not to remember past interactions. 
    This helps me stay accurate and focused on the current context, but do feel free to add details from our previous conversations if you think it will help.

    ---
   
    **Ready to get started?** Type your query below!
    """)

# Helper functions for UI logic
def get_selected_papers_research_questions():
    selected_questions = []
    selected_titles = []
    
    if "selected_papers" not in st.session_state:
        st.session_state.selected_papers = []
    
    # Go through all messages to find literature responses
    for message in st.session_state.messages:
        if message.get("is_literature_response") and message.get("literature_data"):
            message_id = message.get("message_id", "unknown")
            response_data = message.get("literature_data")
            
            for i, paper in enumerate(response_data):
                checkbox_key = f"paper_{message_id}_{i}_{paper.get('title', '')[:20]}"
                
                # Check if this paper is selected
                if checkbox_key in st.session_state.selected_papers:
                    title = paper.get('title', 'Untitled')
                    research_question = paper.get('summary', {}).get('research_question', 'Not specified')
                    selected_titles.append(title)
                    selected_questions.append(research_question)
    
    return selected_titles, selected_questions

def get_all_displayed_doc_ids():
    doc_ids = set()
    for msg in st.session_state.messages:
        if msg.get("is_literature_response"):
            for paper in msg.get("literature_data", []):
                if paper.get('doc_id') is not None:
                    doc_ids.add(paper['doc_id'])
    return doc_ids

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Display the contextual message content first (user prompt or assistant preface)
        if message["content"]:
            st.write(message["content"])

        if message.get("is_literature_response"):
            # Handle literature response display
            response_data = message.get("literature_data")
            if response_data:
                st.subheader(f"Literature Review Results ({len(response_data)} papers)")
                
                for i, paper in enumerate(response_data):
                    # Create a unique key for each checkbox
                    message_id = message.get("message_id", "unknown")
                    checkbox_key = f"paper_{message_id}_{i}_{paper.get('title', '')[:20]}"

                    # Display paper title without checkbox
                    st.write(f"**{paper.get('title', 'Untitled')}**")
                    
                    # Display paper details in an expander
                    with st.expander(f"📄 Details - {paper.get('relevance', 'Unknown relevance')}"):
                        summary = paper.get('summary', {})
                        st.write("**Research Question:**", summary.get('research_question', 'Not specified'))
                        st.write("**Methodology:**", summary.get('methodology', 'Not specified'))
                        st.write("**Main Findings:**", summary.get('main_findings', 'Not specified'))
                        
                        relevance = paper.get('relevance', 'Unknown')
                        if relevance.lower() == 'relevant':
                            st.success(f"Relevance: {relevance}")
                        elif 'somewhat' in relevance.lower():
                            st.warning(f"Relevance: {relevance}")
      
# Chat input
if prompt := st.chat_input("Type your question..."):
    # Hide preface once user sends first message
    st.session_state.show_preface = False
   
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Process based on current bot
    if st.session_state.current_bot == "Literature":
        results = process_literature_search(prompt)
        
        if results:
            formatted_prompt, top_docs = extract_top_abstracts_for_lit_prompt(results, prompt)
            
            # Create a map to link titles back to doc_ids
            title_to_doc_id_map = {doc['metadata']['title']: doc['doc_id'] for doc in top_docs}
            
            response_text = generate_response(formatted_prompt)
            response_data = extract_json_from_response(response_text)
            
            # Augment the response with the doc_id for future reference
            for paper in response_data:
                paper['doc_id'] = title_to_doc_id_map.get(paper.get('title'))
            
            # Generate unique message ID
            message_id = str(uuid.uuid4())
            
            # Add literature response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": "", # The content is rendered customly
                "is_literature_response": True,
                "literature_data": response_data,
                "message_id": message_id
            })
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "I encountered an issue processing your literature search. Please try again."
            })
    
    elif st.session_state.current_bot == "Methodology":
        # Methodology handling flow
        with st.spinner("Processing methodology request..."):
                # You'll need to implement these functions or import them
                chapter_prompt = manual_review(prompt, chapter_summary)
                chap_response = generate_response(chapter_prompt)  # Replace with your model call

                category_match = re.search(r'<category>(\d+)</category>', chap_response)
                category_number = category_match.group(1) if category_match else "0"
               
                relevant_chapter = generate_document_prompt(category_number)
                review_prompt = chapter_review(prompt, relevant_chapter)
                final_response = generate_response(review_prompt)  # Replace with your model call
               
                # Add methodology response to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": final_response
                })

    elif st.session_state.current_bot == "Variable Selection":
        # Variable Selection handling flow
        with st.spinner("Processing variable selection request..."):
            try:
                
                categories_prompt = categories_review(prompt, categories_summary)
                categories_response = generate_response(categories_prompt)
                
                # Clean and parse the response
                clean_string = categories_response.strip("` \npython")
                python_list = ast.literal_eval(clean_string)
                print(python_list)

                # Filter the JSON data to keep only keys with abbreviations in the list and remove unwanted fields
                excluded_fields = ["population", "constructed_from", "construction_contributes", "notes", "subject_category", "dataset"]

                filtered_data = {
                    key: [
                        {k: v for k, v in variable.items() if k not in excluded_fields}
                        for variable in value
                    ]
                    for key, value in json_data.items()
                    if key.split(':', 1)[0].strip() in python_list
}
                # Serialize filtered_data to a formatted JSON string
                variables_str = json.dumps(filtered_data, indent=4)
                
                # Use the JSON string in your template
                variable_output = variable_selection(
                    question=prompt,
                    variables=variables_str
                )
                
                responsefinalcat = generate_response(variable_output)  # Replace with your model call
                
                # Add variable selection response to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": responsefinalcat
                })
                
            except Exception as e:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"I encountered an issue processing your variable selection request: {str(e)}"
                })

    else:
        # Generic response for other bots (Variable Selection, Data Analyst)
        with st.spinner("Thinking..."):
            response = f"Sorry there was an issue and I couldn't process your request."
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Rerun to display the new message
    st.rerun()