## 1. Introduction

Your supervisor has said 'HILDA would be good for your next project'. But what is HILDA? How do you access it? And when you get it, how do you navigate your way around the 80 plus different data files and over 100,000 variables to find what you are looking for?

This article aims to provide you with an overview of the HILDA Survey, the data and the documentation. It covers the sample design, following rules, fieldwork, survey content, response rates, data sets and conventions, using the documentation, identifying key variables and where to find program codes to get you started.

## 2. Overview of the HILDA Survey

### 2.1 Sample Design and Following Rules

The HILDA Survey is a nationally representative household panel study that began in 2001 with interviews conducted on an annual basis since then. It is funded by the Australian Government through the Department of Social Services, but the responsibility for the design, administration and preparation of data for release rests with the Melbourne Institute: Applied Economic and Social Research at the University of Melbourne. Roy Morgan has undertaken the fieldwork since Wave 9 (the fieldwork for Waves 1-8 was undertaken by Nielsen).

The Wave 1 sample had a multi-stage clustered stratified design with 7,682 responding

households from a total of 11,693 in-scope households, resulting in a household response rate of 66 per cent. Wave 1 responding households contain 19,914 individuals, which include 13,969 respondents, 1,158 nonresponding adults and 4,787 children aged under 15 years. The sample excludes people living in very remote parts of Australia and those living in institutions (such as nursing homes, motels and prisons).

Individuals from responding households in Wave 1 (termed Continuing Sample Members (CSMs)) form the basis of the sample that is followed and interviewed over time. The sample is extended in subsequent waves to include other members who join CSM households (termed Temporary Sample Members (TSMs)). TSMs are converted to CSMs under certain circumstances: if they are a baby of a CSM, if they are the other parent of a CSM baby, or if they have arrived in Australia after a particular cut-off point. ${ }^{1}$ These newly created CSMs are followed and interviewed if they leave the household of an original CSM.

The sample was expanded in Wave 11 (2011) with a top-up sample selected on the same basis as the Wave 1 sample. This added 2,153 responding households containing 4,009 respondents, 273 non-responding adults and 1,180 children to the sample. The household response rate for this top-up sample was 69 per cent.

### 2.2 Fieldwork, Mode and Incentives

The fieldwork extends from late July to early February each year, with about 95 per cent of the interviews conducted between August and November. The interviews with a household consist of a household component and individual components. One person in the household completes the Household Form, which collects the basic details of everyone in the household and how they are related to each other, and the Household Questionnaire, which collects information about child care and housing. Then each person aged 15 and over is interviewed using the Continuing Person Questionnaire (CPQ)
if they have been interviewed before or the New Person Questionnaire (NPQ) if they have never been interviewed before. There is also a Self-Completion Questionnaire (SCQ) that each interviewed person completes either before their interview or after. The SCQ includes attitudinal questions and potentially more sensitive questions that the respondent would be more comfortable answering on their own.

Over 90 per cent of the interviews are conducted face-to-face with the remainder conducted by telephone. During the first eight waves, these interviews were completed using paper questionnaires and responses were dataentered in the office, but since Wave 9 the interviews have been conducted using computer-assisted personal interviewing (CAPI). The SCQ is handed to the respondent on first contact with the household or after their interview. For those interviewed by telephone, the SCQ is mailed out to the respondent after their interview.

With the COVID-19 pandemic in 2020, we switched to predominantly telephone interviewing in Wave 20 with 96 per cent of the interviews conducted by telephone. We continued to use the face-to-face interviewers to undertake telephone interviews to maintain interviewer-respondent continuity where possible. We also added an online option for the SCQ, with 82 per cent of the SCQs completed via this mode.

Response is incentivised, though the structure of the incentive has changed over time. For Waves 1-4, there was a household-level incentive: $\$ 20$ for a part household response (where at least one but not all adults were interviewed) and $\$ 50$ for a full household response. For Waves 5-19, there was an incentive for each interview completed and a household bonus if all adults were interviewed. The amounts increased over time from $\$ 25$ in Wave 5 to $\$ 40$ in Wave 19. In Wave 20, only individual incentives were offered: $\$ 40$ for each interview and $\$ 20$ for each completed and returned SCQ.

In total, across the first 20 waves of the HILDA Survey, 305,143 individual interviews

have been conducted with 33,347 people and 275,147 SCQs have been returned.

### 2.3 Survey Content

The three core pillars of the HILDA Survey content are family life, income, and labour market activity and employment. Questions are included every year on these topics and constitute the bulk of the interview.

Rotating modular content includes questions on wealth, fertility, retirement, health, and human capital and education. These typically occur on a 4 -year cycle. By Wave 20, wealth, retirement and fertility questions have been collected five times and the health and human capital/education modules have been included three times.

When an individual is interviewed for the first time, they are asked a series of background questions covering, for example, their country of birth, education, employment history, marital history and family background. Where relevant, some of these topics are updated in subsequent interviews.

The HILDA Survey questionnaires are available from the HILDA Survey website at: https://melbourneinstitute.unimelb.edu.au/ hilda/for-data-users/questionnaires-and-fieldwork-materials

## 3. How to Order the Data

The HILDA Survey data are available through the Australian Data Archive Dataverse (https:// dataverse.ada.edu.au/dataverse/hilda). Potential users must apply, and be approved for, access to the data sets. Two versions of the HILDA Survey data are available: the General Release and the Restricted Release. The Guidelines available in the HILDA Dataverse will help you decide which version is appropriate to your research needs. Most users use the General Release.

You can download the marked-up questionnaires and codebooks (described below) before you apply for the data. This will help you see if the variables you are after are in the data sets.

## 4. Data Structure

### 4.4 File Structure

For each wave, there are four datafiles:

- Responding person file-contains one record for each person interviewed and includes variables from the Person Questionnaire and the Self-Completion Questionnaire.
- Household file-contains one record per responding household (that is, a household with at least one completed individual interview) and includes variables from the Household Form and the Household Questionnaire.
- Enumerated person file-contains one record per person in responding households and includes information from the Household Form reorganised at the individual level.
- Combined file-matches the enumerated person file, household file and responding person file together.

There is also a master file and a longitudinal weights file. The master file provides details of the sample and contains one record for each person who has ever been part of a responding household. The longitudinal weights file contains weights specific to the paired wave and balanced wave combinations of longitudinal weights for responding and enumerated individuals (described in more detail below).

Most researchers will use the responding person files or the combined files. They will match on information from the other files if needed. If you are using the combined files, be aware of the -10 codes in variables which indicate the person did not provide an interview (that is, because they were a child or a non-responding adult in a responding household).

### 4.5 Variable Naming Conventions

The first character of a variable name represents the wave the variable belongs to

('a' for Wave 1, 'b' for Wave 2, ... 't' for Wave 20). The next two characters in the variable name indicate the broad subject area to which the variable belongs. The remaining five characters of the variable are used to uniquely identify the variable within the broad subject area.

Table 3.3 of the HILDA Survey User Manual provides a list of the broad subject areas. Once you have found some variables relevant to your project, it might be helpful to look through the other variables with the same broad subject area.

### 4.6 Missing Values

Missing values in the HILDA Survey data sets are represented by negative values, as described in Table 1. Make sure that when you are performing a statistical operation or procedure on the data you have suitably coded or programmed for missing values.

Variables that can legitimately contain negative values (such as income or wealth) are provided as two parts: the negative component and the positive component. For example, if a person has a business loss of $\$ 10,000$ in the last financial year, the positive variable (abifp) will contain zero and the negative variable (abifn) will contain 10,000. You would first set missing values for business income to system missing and then calculate abif = abifp - abifn. Or you would use the imputed version of the variables for business income (which no longer have missing values) and you would calculate abifi = abifip - abifin.

## 5. Long versus Wide Files

When you use the data files, you will most likely want to put the files into a long format where you have one record for each observation of each person. So, if a person responds 20 times, you will have 20 rows of data for them and if another person responds three times, you will have three rows of data for them. To do this, you will need to follow these steps:

Table 1 Missing Value Conventions for
Numeric Variables

| Code | Description |
| :-- | :-- |
| -1 | Not asked (question skipped due to answer at a |
|  | previous question) |
| -2 | Not applicable |
| -3 | Don't know |
| -4 | Refused or no answer |
| -5 | Invalid multiple responses selected (only |
|  | appears in the SCQ) |
| -6 | Value recorded for the question is implausible |
| -7 | Value could not be determined |
| -8 | Respondent did not complete the SCQ |
| -9 | Household did not respond |
| -10 | Individual did not provide an interview (only |
|  | used in the combined file) |

STEP 1: Select the variables you want from each wave (including the cross-wave person identifier xwaveid).

STEP 2: Strip off the wave letter for the variables selected from each wave (except for xwaveid).

STEP 3: Create a wave variable (containing $1,2,3, \ldots$ depending on the wave) or a year variable (containing 2001, 2002, 2003, ...).

STEP 4: Append the data for each wave.
This sort of file typically lends itself to the various longitudinal analysis commands available in statistical software.

Alternatively, if you are only using a few waves of data and are interested in change from one time point to another you could set the data up as a wide file where you have one row per person. To do this, you would select the variables you want from each wave (including xwaveid) and then match individual records from one wave to another by xwaveid.

## 6. Example Code

There are a number of programs in SAS, SPSS, Stata and R in the program library on the HILDA Survey website (https://melbourneinstitute. unimelb.edu.au/hilda/for-data-users/programlibrary). There are programs to show you how to match household and responding person files, how to add partner variables, and how to

create long and wide files. Also available on this page are some programs provided by other users and several demonstrate how to use various user-developed macros to create long files.

## 7. Finding Variables

Finding the right variables for your analysis can be challenging given there are many variables in the data sets. A range of different tools have been provided to help you. Personally, I tend to use a combination of the marked-up questionnaires and the cross-wave index. Others are partial to the subject-level codebook or the online data dictionary. You will find what works for you with time.

A good set of variables to look through initially is provided in the useful variables table in the User Manual (see Table 3.2 in Summerfield et al. 2021).

### 7.7 Marked-Up Questionnaires

The marked-up questionnaires provide the associated variable name next to each question in the questionnaires. For Waves 1-12, paper questionnaires were used for the interview components (though only as a backup during Waves 9-12) so the marked-up questionnaires are an edited version of these questionnaires. From Wave 13 onwards, the variable name is inserted next to the relevant question in the paper representation of the CAPI script. For the SCQ, the marked-up questionnaire is provided using the paper questionnaire.

It is good to look at the marked-up questionnaires, even if you found the variable you are after via different means, as this will show you the context within which each question was asked. You might also find some useful variables in the surrounding section of the questionnaire.

### 7.8 User Manual

The User Manual provides more details about the HILDA Survey data than what can be
provided in this brief article (see Summerfield et al. 2021). It provides information on derived variables, weights and imputation. Particularly helpful are the descriptions of the income model, wealth models and family variables. Also useful are two appendices of the User Manual: Appendix 1A provides a brief overview of the survey content and Appendix 1B provides details of the development and sources of the questions included. There is also a section on data quality that contains a summary of various issues examined (primarily by the Melbourne Institute HILDA Survey team) and points to papers for where to find more information.

The User Manual is available on the HILDA Survey website at: https://melb ourneinstitute.unimelb.edu.au/hilda/for-data-users/user-manuals.

### 7.9 Codebooks

The best codebook to work with is the Subject Level Coding Framework. It indicates in which waves a variable exists in the data sets, the question number in each wave, the variable label, the values the variable takes, the value labels, in which file the variable is found, and the population asked. For the derived variables, it also provides notes on how the variable is derived, what variables contribute to the derived variable and to which variables it subsequently contributes. An example of how a variable is summarised in the Subject Level Coding Framework is provided in Figure 1. You will see the variable names with an underscore ('_') replacing the wave letter. That said, this codebook is very long. The Release 20 version of this codebook runs to more than 1,300 pages. A useful tip is to search the PDF for the response categories you might expect a variable to take.

The Cross Wave Index is a slim version of the Subject Level Coding Framework which provides the waves in which the variable exists, the question number in each wave, the variable label and the file in which the variable is found. This document is perhaps best used after you are familiar with the data

Figure 1 Example of the Subject Level Coding Framework

sets and are wanting to verify the waves in which you expect to find that variable.

### 7.10 Online Data Dictionary

The Online Data Dictionary provides information that is very similar to the Subject Level Coding Framework. Most useful is the variable name search function to find details for a variable of which you are already aware. It will provide you with details for that variable in each wave, including the questionnaire text and frequencies (see Figure 2). There is also a cross-wave view which will provide information most similar to the Subject Level Framework along with frequencies by wave.

Perhaps less useful are the keyword and subject-level searches. These searches can bring up pages and pages of variables and it may be hard to find the variable you are interested in. The keyword search now includes searches that will look for the keyword in the description, category or question numbers which may help you find the variable you are interested in. The search facility does not include common alternatives for words used in the variable labels, value labels or description, and as such it is similar to searching in the Subject Level Coding Framework PDF.

The Online Data Dictionary is available here: https://www.online.fbe.unimelb.edu.au/ HILDAodd/Default.aspx.

## 8. Response

### 8.11 Re-Interview Rates

Important to the useability and quality of a longitudinal survey is the re-interview rate of sample members. One measure of this is the percentage of respondents in one wave that is re-interviewed in the next, excluding those who have died or moved abroad. In a household panel survey, this re-interview rate incorporates new sample members and children turning 15 once they are interviewed. Figure 3 shows the re-interview rate for the main and top-up samples in the HILDA Survey (solid lines). The re-interview rates are typically lower in the earlier waves than in the later waves as the sample members become used to being interviewed. From Wave 9 onwards in the main sample, the reinterview rate is 96 per cent or higher, which means the attrition rate is 4 per cent or lower each wave. The HILDA Survey has one of the highest re-interview rates in the world (Watson et al. 2019). It compares well in the early waves to our closest comparator studies, the British Household Panel Survey and the German Socio-Economic Panel, and, from Wave 9, has consistently higher response rates than these studies.

An alternative measure is the re-interview rate of Wave 1 respondents (dashed lines in Figure 3). This is the percentage of Wave 1

Figure 2 Example of the Online Data Dictionary

| Variable | agh4a |
| :--: | :--: |
| Label | SCQ:A4a Role-physical: Cut down the amount of time spent on work or other activities |
| Form | SCQ |
| Question No. | SCQ A4a |
| Questionnaire <br> Text | During the past 4 weeks, have you had any of the following problems with your work or other regular daily activities as a result of your physical health ? a) Cut down the amount of time you spent on work or other activities |
| SCQ Page No. | 3 |
| Population | All |
| Subject Area | HEALTH - General Health and Well-Being |
| Survey Wave | 1 |
| Data File | Responding Person File |
| Frequency |  |
|  | gh4a | RP |
|  | [-4] Refused/Not stated | 292 |
|  | [-5] Multiple response SCQ | 1 |
|  | [-8] No SCQ | 911 |
|  | [1] Yes | 2107 |
|  | [2] No | 10658 |

respondents who are re-interviewed in a wave, excluding those who have died or moved abroad. This sort of measure is more often reported for cohort studies as they have a single group of individuals to follow over time. In Wave 11 the re-interview rate of Wave 1 respondents was 70 per cent and in Wave 20 it was 59 per cent.

### 8.12 SCQ Response Rates

On average over the past 20 waves, 90 per cent of interviewed individuals also return the SCQ. The SCQ response rate for respondents interviewed face-to-face is substantially higher than for those interviewed by telephone ( 92 per cent compared to 60 per cent in Waves 1 to 19). This is, in part, due to the type of respondents interviewed by telephone and that the questionnaire is mailed out to the respondent and has to be mailed back after they complete it. Fortunately, in Wave 20, when most of the interviews were undertaken by telephone, the addition of an online SCQ option and a specific incentive for the SCQ helped deliver an SCQ response rate of 92 per cent, similar to the rates achieved in the previous four waves.

Figure 3 Re-Interview Rates in the HILDA Survey


Source: HILDA Survey User Manual (Table 2.3 in Summerfield et al. 2021).

Further details on the SCQ response rate, methods to increase the response rate and characteristics associated with responses can be found in Watson and Wooden (2015).

### 8.13 Item Non-Response

Item non-response in variables from the interview components is relatively low (typically less than 1 per cent) with the exception of dollar value questions, such as income and wealth. For example, 4 per cent of respondents with wages and salaries did not know or refused to provide the amount in Wave 19. When the various income components are summed at the individual level, the rate of missingness to total financial year income is 11 per cent. An individual may be missing total financial year income because they are missing a small component of income, rendering the total missing also. At the household level, 23 per cent of households are missing total financial year income in Wave 19 because an interviewed individual is missing an income component or an adult in the household was not interviewed.

For the SCQ, the item non-response is higher than in the individual interview
(typically less than 3 per cent). This is because respondents may accidentally (or intentionally) skip questions or because some of the questions may be difficult to answer (such as expenditure).

## 9. Weights

Both cross-sectional weights and longitudinal weights are provided in the HILDA Survey data sets. While not the primary purpose of the HILDA Survey, the cross-sectional weights allow the user to create population estimates for each wave. Cross-sectional weights are provided for responding persons (_hhwtrp), enumerated persons (_hhwte) and households (_hhwth). Longitudinal weights are provided for each pair of waves and each run (or balanced panel) of waves. For example, wlrae is the longitudinal weight for respondents interviewed in Wave 1 (wave letter 'a') and Wave 5 (wave letter 'e') and wlra_e is the longitudinal weight for respondents interviewed each wave from Waves 1 to 5. Some special longitudinal weights are provided for the rotating modules. Longitudinal weights are provided for PQ respondents, SCQ respondents and enumerated persons. The HILDA Survey User Manual

provides guidance on selecting the appropriate weight for your analysis. If you have further questions on using the weights, please email me directly or hilda-inquiries@unimelb.edu.au.

The weights adjust for differential probabilities of selection and attrition (for a summary see the weighting section of the HILDA Survey User Manual or the detailed technical paper on the construction of the weights (Watson 2012)). They are also modified to match several known crosssectional population benchmarks from the Australian Bureau of Statistics (ABS) such as age, sex, household size, partner status and employment status. Replicate weights or the combination of weight, cluster and stratification variables can be used to calculate appropriate standard errors. For examples of how to use weights and construct standard errors appropriate to the complex sample design of the HILDA Survey, see Hayes (2008).

You should use weights when creating descriptive statistics from the HILDA Survey data for the purposes of making inferences about the Australian population. Deciding whether to use weights in regression models is less straightforward. Incorporating the weights in the model can help guard against bias in parameter estimates due to nonresponse but comes at the cost of larger standard errors (Pfeffermann 2011). Comparing weighted and unweighted regression model estimates can be useful in identifying situations in which the model is not taking account of relevant variables that are factored into the weights. This can be a springboard for re-thinking the specification of your unweighted model.

## 10. Imputation

Owing to the amount of missingness in the dollar value variables and the importance of income, wealth and (to a lesser extent) expenditure, these variables have been imputed. The imputed value will normally have an 'i' at the end of the variable name (unless it is a variable that is the positive or negative component, in which case the variable will
end with 'ip' or 'in'). A flag variable is also provided (ending with ' f ') to indicate whether the variable has been imputed or not.

The imputation process uses a longitudinal imputation method proposed by Little and $\mathrm{Su}(1989)$ with a cross-sectional nearest neighbour imputation method as a fallback method. A brief description of the imputation methods is provided in Appendix 2 of the HILDA Survey User Manual and more detail is provide elsewhere (Hayes and Watson 2009; Sun 2010; Watson and Starick 2011).

It is recommended that, unless you are analysing the income, wealth or expenditure variable as the dependent variable in your model, you should use the imputed version of the variable to avoid dropping many cases from your analyses.

## 11. Representativeness of the Sample

The HILDA Survey sample is designed to be representative of the Australian population, with the exception of people living in very remote parts of Australia and people living in institutions. While we did not sample people from very remote parts of Australia or in institutions, we do follow and interview them if they move into these places. However, it is not always possible to interview these people if they are outside of the interviewer network, do not have a telephone, or are otherwise unable to be interviewed (due to ill-health, lack of access, and so forth).

A comparison of the Wave 1 sample to ABS benchmarks shows that non-respondents were more likely to be living in Sydney, male, not married/de facto, aged 20-24 or aged 65 and over, or born in a non-English speaking country (Watson and Wooden 2002). The characteristics of non-respondents in the Wave 11 top-up sample were similar to those observed in Wave 1 with the exception that people born in Australia were less likely to participate than those born abroad in an English-speaking country (Watson 2012).

Further, respondents who are harder to contact in the next wave are more likely to be those who move house or are young, male, not

married/de facto, renters and non-English speakers (Watson and Wooden 2009). Once contact is made, response probabilities are lowest among the young and elderly, people born overseas, the least educated, those with a serious long-term health condition and those living in large households.

The weights help to correct for the bias introduced into the sample due to differential non-response. For example, in a comparison of HILDA Survey estimates of residential mobility to those from various ABS data sources, the weighted HILDA Survey estimates align well with other sources, particularly the General Social Survey (Watson 2020). The unweighted estimates are between 2 and 5 percentage points lower than the weighted estimates.

A particular area of concern in terms of the HILDA Survey's representation of the Australian population is the lack of coverage of recent immigrants. There is no natural mechanism to add a sample of newly arrived immigrants in the same way we add a sample of new births each year. While we have amended the following rules to include new immigrants that join a HILDA Survey household, they are not truly representative of the entire group of immigrants that settle in Australia. The Wave 11 top-up sample ameliorated the situation with a sample of new immigrants arriving between 2002 and 2011. These immigrants form part of the general sample top-up and have large weights. This is because they only had one chance of selection into the sample (in 2011) rather than two (in 2001 and 2011) as was the case with other members of the general sample top-up. We have not yet had a second top-up sample to address the lack of immigrants arriving after 2011. To give some sense of the size of the issue, the 2010 HILDA Survey weighted cross-sectional estimate for the proportion of people aged 15 years who are born in Australia is 75 per cent whereas the Labour Force Survey estimate is 71 per cent (Watson 2012). After incorporating the topup sample the weighted cross-sectional estimate in 2011 from the HILDA Survey is 70 per cent which aligns with the Labour

Force Survey estimate. A difference in estimates once again began to emerge in 2012. This difference will continue to grow whilst we have immigrants arriving into the country until an additional sample of new arrivals is added to the HILDA Survey sample and is repeated on a regular basis.

## 12. More Information

Of course, a short article such as this cannot cover everything you may want to know about the HILDA Survey. I recommend you explore the HILDA Survey website, the User Manual and the discussion and technical papers. You can also view a growing list of journal articles and other reports produced by users of the HILDA Survey data (see the HILDA Survey publication listing at melbourneinstitute. unimelb.edu.au/hilda/publications or the Department of Social Services repository flosse.dss.gov.au). Searching these lists may help you find research relevant to your project.