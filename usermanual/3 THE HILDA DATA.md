# 3. THE HILDA DATA

### 3.1. Ordering the Data

Researchers wishing to use HILDA data must apply online through the HILDA Dataverse, which is managed by the Australian Data Archive (ADA).
All applicants for datasets must complete a once only Confidentiality Deed Poll and email the scanned, signed copy to DSS (LongitudinalStudiesDataAcess@dss.gov.au) and ADA (ada@anu.edu.au) before applications will be approved.

### 3.2. Cross-National Equivalent File (CNEF)

The Cross-National Equivalent File originated from a Cornell University project to create an equivalent set of income measures for the German Socio-Economic Panel (SOEP) and the American Panel Study of Income Dynamics (PSID). It has since expanded to include data from many other countries which are undertaking longitudinal household panels (including Australia, Canada, Germany, Great Britain, Korea and Switzerland), and the range of data has expanded to include employment, health and psychological measures. The HILDACNEF long file and codebooks are included on the Dataverse website. Breaking with CNEF convention, the variable names are prefixed with 'zz' (a PanelWhiz requirement). The codebooks are wave oriented, but it is straightforward to relate the documentation to the long variables supplied.
Access policies for the datasets within the CNEF vary depending upon the administrative requirements of the individual surveys from which the datasets are taken. DSS is only responsible for approving access to the HILDA-CNEF. Details on how to order the CNEF data for other surveys can be viewed on the CNEF website: http://www.cnefdata.org/
Access to the HILDA-CNEF data is obtained by applying for the HILDA General Release dataset.

### 3.3. A Reminder of the Security Requirements for the Data

For full details of your obligations as an authorised data user please refer to the Longitudinal Studies Data Access and Use Guidelines, which contains helpful information for researchers as well as the full Terms and Conditions of Use.

### 3.4. How the Data Files are Provided

All data are provided in SAS, SPSS, and Stata ${ }^{1}$ formats. (Note: R can read the SPSS or Stata datasets.)
Each release also includes extensive documentation of the data, including coding frameworks, marked-up questionnaires and variable frequencies. The files and the documentation are discussed in detail in later sections of this manual. Changes to the data files between releases can be found in the readme pdf for the current release.
The data files can be transferred to other statistical packages using StatTransfer or any other data conversion package of your choice ${ }^{2}$. You may need to restrict the number of variables to be included in your transferred datasets due to the limitations on the number of variables imposed by some statistical packages.

[^0]
[^0]:    ${ }^{1}$ You will need to use STATA SE as there are more than 2047 variables in the datasets. Suitable maxvar values are provided in "Readme 230.pdf".
    ${ }^{2}$ A trial copy of StatTransfer can be downloaded from www.stattransfer.com or purchased online at http://www.circlesys.com/downloads/

# 3.5. Structure of the Data Files 

For each wave, there are four files:

- Household File - containing information from the HF and HQ.
- Enumerated Person File - containing all persons in all responding households and contains limited information from the HF (includes respondents, nonrespondents and children) ${ }^{3}$.
- Responding Person File - containing all persons who provided an interview and contains CPQ/NPQ and SCQ information ${ }^{4}$.
- Combined File - this is a combined file of the three files above. The household information and responding person information is matched to each enumerated person.
In addition, a Master File and a Longitudinal Weights File are provided. The Master File contains all persons enumerated at any wave, their interview status in each wave and limited information about the individual. The Longitudinal Weights File contains weights for all sequential balanced panel combinations and all balanced pairs of waves.


### 3.6. Identifiers and Useful Variables

Individuals have a unique identifier for all waves which is xwaveid. Individuals in the same household in a particular wave have a household identifier for that wave (_hhrhid) ${ }^{5}$. Note that you will need to replace the underscore '_' in the variable name with the appropriate letter for the wave, 'a' for wave 1, 'b' for wave 2, etc. The household identifier will change from wave to wave as these household identifiers are randomly assigned anew each wave. Further, the length of the household identifier is 6 digits in wave 1 and from wave 11 onwards and is 5 digits in waves 2 to 10 . Related to the household identifier is a wave specific person-level identifier _hhrpid ${ }^{6}$ which adds a further two digits to the household identifier to indicate the person number within the household for that wave. Note that _hhrpid changes over time as the household identifier changes. Also, note that the order that people are listed within the household can change as people leave or join the household. There is no meaning to the order of the people in the household (for example, the first person listed within the household is not necessarily the oldest, a parent or part of a couple).
Household and person-level files within a wave can be merged using _hhrhid (i.e. ahhrhid for wave 1, bhhrhid for wave 2, etc). ${ }^{7}$ Enumerated and responding person files within a wave can be merged by using the cross-wave identifier xwaveid (or alternatively the wave specific person identifier _hhrpid).

[^0]
[^0]:    ${ }^{3}$ The variable _hgenum indicates whether the person belonged to a responding household each wave and this may be useful when selecting those who have been tracked over the entire study irrespective of whether they were interviewed (i.e. just those who were enumerated at all waves).
    ${ }^{4}$ The variable _hgint indicates whether the person completed an interview and this is one way to select a balanced responding panel (_hgint=1 at all waves), or to reduce the Combined Files into "only interviewed adults" files (this removes the person-level records for children or non-responding adults from responding households which are included to describe the household when calculating measures such as the poverty rate or gini coefficient). Conversely _hgni allows selection and separation of not-interviewed adults and notinterviewed children aged under 15. _scmatch indicates that an SCQ has been matched to a PQ.
    ${ }^{5}$ Users of the Restricted Release files can alternatively use _hhid.
    ${ }^{6}$ Users of the Restricted Release files can alternatively use _hhpid.
    ${ }^{7}$ Users of the Restricted Release files can alternatively use _hhid to match the household and person files, and _hhpid to match the person files. In wave 1, the household identifier is six digits long, corresponding to area (three digits), dwelling number (two digits) and household number (one digit). The person identifier in wave 1 is then eight digits long - the first six are the household identifier, followed by two digits for the person number. In subsequent waves, the household identifier is five digits long, and the person identifier is seven digits long. From wave 11, to accommodate the Top-Up sample, the identifiers revert to the wave 1 lengths.

Information from enumerated or responding person files can be linked across waves by using the cross-wave identifier xwaveid.
Partners within the household are identified by their cross-wave identifier (_hhpxid) or by their two-digit person number for the household (_hhprtid). These variables are provided on both the enumerated and responding person files and are derived using the HF relationship grid. Partners are either married or de facto and include same sex couples. If you are using _hhprtid, it is the person number for the household (for example, if person 02's partner is person 05, the partner identifier for person 02 will contain '05' and for person 05 it will contain '02'). You will need to concatenate the household identifier with the partner identifier before you can match on partner characteristics to the person file. Using the partner's cross-wave identifier (_hhpxid) is therefore much easier.
Parents within the household are similarly identified in _hhfxid and _hhmxid (father's and mother's cross-wave identifiers) or _hhfid (father's person number) and _hhmid (mother's person number). A parent may be natural, adopted, step or foster (a parent's de facto partner also counts as a parent).
A list of other biological cross-wave identifiers can be found in Table 3.1.
Table 3.1: Other biological cross-wave identifiers

| Variable | Label | Notes |
| :--: | :--: | :--: |
| _hhbmxid | DV: Biological Mother's crosswave id | For "ever-co-resident parents" (same household, ownparent or own-child relationship), the xwaveid of the parent (text, 7-digit). The biological parent's xwaveid is carried back or forward to all waves even if the parent is not coresident but the child has been enumerated. |
| _hhbfxid | DV: Biological Father's crosswave id |  |
| _hhtwxid | DV: Twin cross-wave id | For "ever-co-resident twins" (same household, same date of birth and full-siblings), the xwaveid of the twin (text, 7digit). The twin's xwaveid is carried back or forward to all waves even if the twin is not co-resident. <br> Adult non-co-resident twins are recorded in the PQ section on siblings asked in waves 8, 12 and 19 (section HS) but they are not added to _hhtwxid (insufficient information to determine if they are part of the sample). Triplets, quadruplets etc. are not included in the twin identifiers. |
| _hhmgmxd | DV: Maternal grandmother's cross-wave id | Defined as the "ever co-resident parents" of the biological parents. |
| _hhmgfxd | DV: Maternal grandfather's cross-wave id | Grandparents where the lineage (paternal or maternal) is not yet known are excluded (that is, in households where only the grandparents and grandchildren have been coresident [across all the waves]). In addition, the variations that step parents and step grandparent and grand step |
| _hhpgmxd | DV: Paternal grandmother's cross-wave id | parents introduce, both in terms of the number of relationships and the variation over time, has led to step relationships being excluded. |
| _hhpgfxd | DV: Paternal grandfather's cross-wave id |  |

Listed below in Table 3.2 are some useful socio-demographic variables. These are provided to help new users get started with using the HILDA data.

Table 3.2: List of useful variables

| Variable | Description | Variable | Description |
| :--: | :--: | :--: | :--: |
| xwaveid | Unique person identifier (across all waves) | _hhtup | Wave Top-Up - person |
| _hhrhid | Random household identifier (wavespecific) | _hhtuh | Wave Top-Up - household |
| _hhrpid | Random person identifier (wavespecific) | _hhfty | Family type |
| hhsm | Sample member type | _hhiu | Income unit |
| _hhresp | Household response status | _hhpers | Number of persons in household |
| _fstatus | Person response status (Master File) | _hhtype | Household type |
| _scmatch | Whether SCQ record matches to a PQ | _hhpxid | Partner's cross-wave identifier |
| _hhyng | Age of youngest person in HH | _hhfxid | Father's cross-wave identifier |
| _hhold | Age of oldest person in HH | _hhmxid | Mother's cross-wave identifier |
| _hhrih | Relationship in household | _hhstate | State |
| _hhfam | Family number | _hhssos | Section of state |
| _hgage | Age | _hhsgcc | Greater Capital City Statistical Area |
| _hgsex | Sex | _hhda10 | SEIFA decile of socio-economic disadvantage |
| _mrcurr | Marital status | _ancob | Country of birth |
| _esbrd, esdtl | Employment status (broad, detail) | _edhigh1 | Highest education level achieved |
| _losat | Life satisfaction | _edfts | Full-time student |
| _jbhruc | Combined per week usually worked in all jobs | _edagels | Age left school |
| _jbmo62 | Occupation code 2-digit ANZSCO | _edhists | Highest year of school completed/currently attending |
| _wscei | Imputed current weekly gross wages and salary - all jobs | _edtypes | Type of school attended/attending |
| _wsfei | Imputed financial year gross wages and salary | _helth | Long term health condition/disability/impairment from PQ |
| _hifdip, hifdin | Household disposable income (positive and negative) |  |  |

# 3.7. Program Library 

Several programs have been provided on the HILDA website in SAS, SPSS, Stata and R to help you get started with the HILDA data.

# 3.7.1. HILDA tax-benefit model 

This Stata program implements the HILDA tax-benefit model, which the HILDA Survey team uses to estimate income taxes and family benefits. The program code makes clear the assumptions, parameters and formulas of this model. This provides users with the option to recalculate taxes and family benefits themselves. The program works with both the General and the Restricted releases of HILDA. Note that, for some observations, the program will produce values that are slightly different from the official values when it is used with the General Release. This is because the General Release provides less precise information on dates of birth and because some income variables of the General Release are topcoded.

### 3.7.2. Match Files

The programs showing how to match files are:

- Program 1 - SAS program to match wave 1 household and responding person files.
- Program 2 - SPSS program to match wave 1 household and responding person files.
- Program 3 - Stata program to match wave 1 household, enumerated and responding person files.
- Program 4 - R program to match wave 1 household and responding person files.


### 3.7.3. Add Partner Variables

Some users may want to include variables for a respondent's partner in their analyses. The programs showing how to utilise the partner's cross-wave identifier _hhpxid to add partner variables onto the Responding Person File are:

- Program 5 - SAS program to add partner variables.
- Program 6 - SPSS program to add partner variables.
- Program 7 - Stata program to add partner variables.
- Program 8 - R program to add partner variables.


### 3.7.4. Create Longitudinal Files

There are several ways users might want to create a continuous balanced panel longitudinal file:

- Wide file of responding persons - this is where we keep only people responding in all waves and put the variables for each wave next to each other (that is, there is one row of data for each person).
- Wide file of enumerated persons - this is where we keep only those people who were in responding households in all waves and the variables for each wave are put next to each other.
- Long file of responding persons - this is where we keep only people responding in all waves and the information for each wave is stacked together (that is, there is a separate row of data for each wave of information for each person).
- Long file of enumerated persons - this is where we keep only those people who were in responding households in all waves and the information for each wave is stacked together.

Most users will probably want to restrict the files to only include respondents or people from responding households. A few users may also want to add people who have died or moved out-of-scope (depending on the research question they are answering).
The programs showing how to create balanced long files of responding persons are:

- Program 9 - SAS program to create long longitudinal files.
- Program 10 - SPSS program to create long longitudinal files.
- Program 11 - R program to create long longitudinal files.

The wide files are created by matching the Responding or Enumerated Files for each wave together using xwaveid. An alternative way to strip off the first letter of the variable names in SAS is provided in:

- Program 12 - SAS macro to strip the first letter from the variable name.

Other users may want to create an unbalanced panel - where you take all respondents or enumerated persons available at each wave (not just those that consistently respond or are consistently in responding households). The above programs can be modified to do this addition. An example Stata program to create a balanced or unbalanced panel is provided in:

- Program 13 - Stata program to create long longitudinal files. ${ }^{8}$

Example programs to create wide files are provided in:

- Program 14 - SAS program to create wide longitudinal files.
- Program 15 - SPSS program to create wide longitudinal files.
- Program 16 - Stata program to create wide longitudinal files.
- Program 17 - R program to create wide longitudinal files.

The longitudinal weights on the enumerated person file and the Responding Person File are for the full balanced panel of respondents and enumerated persons from wave 1 (i.e., across the first two, three, ... waves). If you are constructing a balanced panel with different specifications you should find a suitable weight in the Longitudinal Weights File. Out of scopes (deaths and moves overseas) are treated as acceptable outcomes, so these people have weights applied as well.

# 3.7.5. Applying Weights and Obtaining Appropriate Standard Errors 

The HILDA Survey has a complex sample design, non-response and attrition. This should be considered when creating descriptive statistics. The following programs show how this can be done:

- Program 18 - SAS program to apply weights.
- Program 19 - SPSS program to apply weights.
- Program 20 - Stata program to apply weights.
- Program 21 - R program to apply weights.

Further details on selecting the appropriate weight and applying them is found in Section 4.28 and in Hayes (2008).

[^0]
[^0]:    ${ }^{8}$ This program requires at least 2GB memory to run. If your computer does not have this much memory, then you will need to restrict the datasets to only the subset of variables you need.

# 3.7.6. User Provided Programs 

A small number of user written programs have been added to the program library (at the link above). Users of the HILDA data can contribute code to this library if they believe it may be beneficial to other users. Please send your code to hilda-inquiries@unimelb.edu.au.

### 3.8. PanelWhiz

PanelWhiz is a collection of Stata/SE Add-On scripts to make using panel datasets easier. PanelWhiz simplifies finding, retrieving and managing variables from multiple waves (without the need to refer to external documentation or type long lists of complicated variable names), selecting appropriate weights, matching partner information and a variety of other common tasks that occur in panel research. By allowing you to save variable 'sets' it also simplifies replacing your working files at subsequent releases of HILDA data. The package creates a long longitudinal file. The interface only runs in Stata/SE, but you can export the created datasets into SPSS, SAS, LIMDEP, GAUSS, and Excel.
PanelWhiz is available for the HILDA General Release and Restricted Release Stata files but first requires running the PanelWhiz setup programs. PanelWhiz updates for each release will be available through the usual PanelWhiz channels.
As PanelWhiz is charityware it is suggested that the user make a direct donation to UNICEF. Details of how to access PanelWhiz can be found at www.panelwhiz.eu.

### 3.9. Variable Name Conventions

Variable names have been limited to eight characters (so that the files can be read in older versions of SPSS and SAS). The variable name is divided into three parts and attempts to provide information on the content of the variable:

- First character - wave identifier, with 'a' being used for wave 1, 'b' for wave 2, 'c' for wave 3, etc.
- Second and third character - general subject area (see Table 3.5 for the conventions).
- Fourth to eighth character - specific subject of data item.

Excluding the first character, variable names are the same across waves if the question, question routing (population asked) and response options are the same. If the question or response options have significantly changed, the variable name will also be modified. There are, however, a few (fieldwork) variables where we have decided to vary from this convention:

- Household response status;
- Person response status;
- Household membership;
- New location of mover; and
- Overall self-completion office code.

For these variables, it was thought more important to keep the same variable names. These variables are used for survey administration purposes by the HILDA Survey team at the Melbourne Institute. Many users will not use the detail in these variables. Table 3.4 to Table 3.8 show how the response categories differ for these variables across waves.

Table 3.3: Broad subject area naming conventions, characters 2 and 3 (sorted by code)

| Code | Broad Subject Area | Code | Broad Subject Area | Code | Broad Subject Area |
| :--: | :--: | :--: | :--: | :--: | :--: |
| AD | Australian Defence Force | HC | Children's Health | NS | Non-employment related |
| AL | Leave | HB | Household bills |  | child care for children at school |
| AN | Ancestry | GH | General health and wellbeing | OA | Other assets |
| AP | Activity - Physical |  |  | OI | Other income |
| AT | Attitudes and values | HE | Health | OP | Other property |
| BA | Bank accounts | HG | Household enumeration grid | OR | Other relationships |
| BF | Business Finance | HH | Household information, identifiers and crosssectional weights | PA <br> PD | Parenting <br> Kessler-10 |
| BI | Business Income |  |  | PD | Kessler-10 |
| BM | Body mass index |  |  | PE | Pets |
| BN | Benefits | HI | Household income | PH | Private health insurance |
| BS | Brothers and sisters | HS | Housing | PJ | Previous job |
| CA | Calendar | HW | Household wealth | PN | Personality |
| CC | Child care general | HX | Household expenditure | PR | Partnering / relationships |
| CE | Children's education | IC | Intentions to have children | PS | Parent status |
| CH | Child care during school holidays | IH | Housing insurance | PW | Personal wealth |
| CN | Non-employment related child care | IO | Interviewer observation | RC | Resident children |
|  |  | IP | Intentions and plans | RE | Religion |
| CP | Child care for children not yet at school | JB | Job characteristics of employed | RG <br> RX | Relationship grid <br> (extended) |
| CR | Credit cards | JD | Job discrimination |  | Residential property |
| CS | Child care during school terms | JO | Opinions about job | RP | Reliance Scale |
| CT | Cognitive Ability Tests | JS | Job search of those not employed | RT | Retirement intentions |
| CV | Coronavirus | JT | Job Training | RW | Replicate weight |
| DC | Children - deceased | LE | Major life events | SA | Superannuation |
| DH | Decisions - household | LF | Labour Force | SC | Self-Completion |
| DN | Blood donation | LN | Longitudinal weights | SK | Skills and abilities |
| DO | Dwelling observations | LO | Life opinions | SL | Sleep |
| DT | Personal debt | LS | Lifestyle | SN | Household Screening |
| DU | Drugs | LT | Literacy | SS | Salary Sacrifice |
| DW | Digital platform work | MC | Marriage and children | TA | Training aims |
| ED | Education | MD | Material Deprivation | TC | Total children |
| EH | Employment history | MH | Moving house | TI | Total income |
| ES | Employment status | MO | Mutual obligations | TS | Time stamps |
| FA | Financial assets | MR | Marital relationships | TX | Taxes |
| FF | Food frequency and diet | MS | Marital Status | UJ | Job history of those not in paid employment |
| FI | Attitudes to finances | MV | Motor vehicles |  |  |
| FL | Financial Literacy | NB | Non-cash benefits | WC | Workers compensation |
| FM | Family background | NC | Non-resident children | WS | Wage and salaries |
| FS | Food Insecurity | NL | Not in labour force | XP | Expenditure reported by individual |
| FT | Fertility | NM | Numeracy |  |  |
| FW | Financial Wellbeing | NP | Non-employment related child care for children not yet at school | YH | Youth - employment |
| GA | Gambling |  |  | YH | Youth - education |
| GB | Government Bonus |  |  | YI | Youth - importance |
| GC | Grandchildren | NR | Non co-residential de facto relationship | YP <br> YS | Youth - property <br> Youth - life satisfaction |

Table 3.4: Different codes for household response status

| Description <br> (applies to final _hhresp, initial _hhrespi ${ }^{1}$, follow-up _hhrespi ${ }^{1}$ ) | Codes used |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Wave 1 | Wave 2 | Wave 3 | $\begin{gathered} \text { Wave } \\ 4+ \end{gathered}$ | $\begin{gathered} \text { Wave } \\ 11^{2} \end{gathered}$ | $\begin{gathered} \text { Wave } \\ 23^{3} \end{gathered}$ |
| Full Response |  |  |  |  |  |  |
| Every eligible member of current HH interviewed | 62 | 62 | 62 | 62 |  |  |
| Part Response |  |  |  |  |  |  |
| Part response - refused | 63 | 63 | 63 | 63 |  |  |
| Part response - non-contact | 64 | 64 | 64 | 64 |  |  |
| Part response - contact made with all nonresponse | 65 | 65 | 65 | 65 |  |  |
| Part response - away for workload period | 66 | 66 | 66 | 66 |  |  |
| Part response - language problem | 67 | 67 | 67 | 67 |  |  |
| Part response - incapable/death/illness | 68 | 68 | 68 | 68 |  |  |
| Non-Response |  |  |  |  |  |  |
| Refusal | 69 |  |  |  |  |  |
| PSMs still live there | - | 69 | 69 | 69 |  |  |
| Don't know if PSMs still live there | - | 70 | 70 | 70 |  |  |
| Address occupied - no contact with a sample member | 70 | 71 | 71 | 71 |  |  |
| Contact made and all calls made | 71 | 72 | 72 | 72 |  |  |
| All residents away for workload period | 72 | 73 | 73 | 73 |  |  |
| HH does not speak English | 73 | 74 | 74 | 74 |  |  |
| HH incapable/illness | 74 | 75 | 75 | 75 |  |  |
| Refusal to 1800 number | 75 | 76 | 76 | 76 |  |  |
| Terminate (no PQs) | 76 | 77 | 77 | 77 |  |  |
| HH deceased | - | 78 | 78 | 78 |  |  |
| HH moved out of scope | - | 79 | 79 | 79 |  |  |
| All PSMs moved in with another PSM | - | - | 80 | 80 |  |  |
| All PSMs non-respondents in last 2 waves | - | - | 81 | 81 |  |  |
| Not in area/no phone number | - | - | - | 82 |  |  |
| Untraceable | - | 99 | 99 | 99 |  |  |
| Not issued this wave | - | - | 100 | 100 |  |  |
| Deceased at previous wave | - | - | 101 | 101 |  |  |

| Description <br> (applies to final _hhresp, initial _hhrespi ${ }^{1}$, follow-up _hhrespf ${ }^{1}$ ) | Codes used |  |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  | Wave 1 | Wave 2 | Wave 3 | $\begin{aligned} & \text { Wave } \\ & 4+ \end{aligned}$ | $\begin{gathered} \text { Wave } \\ 11^{2} \end{gathered}$ | $\begin{gathered} \text { Wave } \\ 23^{3} \end{gathered}$ |
| TSM no longer living with PSM at previous wave | - | - | - | 102 | - | - |
| Dwelling out of scope |  |  |  |  |  |  |
| Dwelling vacant for workload period | 77 | - | - | - | 111 | 111 |
| Non-private dwelling - place of business | 78 | - | - | - | 112 | 112 |
| Used for temporary accommodation only | 79 | - | - | - | 113 | 113 |
| Institution with no private HH usually resident | 80 | - | - | - | 115 | 115 |
| Not a main residence (e.g. holiday home) | 81 | - | - | - | 114 | 114 |
| All people in household out of scope | 82 | - | - | - | 110 | 110 |
| Derelict dwelling/demolished/to be demolished | 83 | - | - | - | 116 | 116 |
| Dwelling under construction/unliveable renovations | 84 | - | - | - | 117 | 117 |
| Listing error | 85 | - | - | - | 118 | 118 |
| Screening outcomes |  |  |  |  |  |  |
| Screening questions refused | - | - | - | - | - | 119 |
| Screening questions incomplete | - | - | - | - | - | 120 |
| Screening incomplete - language problem | - | - | - | - | - | 121 |

${ }^{1}$ _hhrespi and _hhrespf are only on the Restricted Release files. For initial response status _hhrespi, subtract 60 from all codes except 99 and wave 11 codes for Dwelling Out of Scope. For follow-up response status _hhrespf, subtract 30 from all codes except 98, 97, 99 and wave 11 codes for Dwelling Out of Scope.
${ }^{2}$ Additional codes used for the Wave 11 Top-Up sample.
${ }^{3}$ Additional codes used for the Wave 23 Top-Up sample.
Table 3.5: Different codes for person response status

| Description (applies to _fstatus, initial _hgri and _hgri1 to _hgri20; follow-up _hgrf and _hgrf1 to _hgrf20; final _hgivw and _hgivw1 to _hgivw20) | Codes used |  |  |
| :--: | :--: | :--: | :--: |
|  | Wave 1 | Wave 2 | Wave 3+ |
| Not part of the household NFI | 4 |  |  |
| Refusal |  |  |  |
| Too busy | 12 | 6 | 7 |
| Too invasive | 11 | 7 | 8 |
| Other reasons | 13 | 8 | 9 |
| Refusal via 1800 number/email | 14 | 9 | 10 |
| Interview terminated | 15 | 10 | 11 |
| Other non-interview |  |  |  |
| Deceased | N/A | 11 | 12 |
| Moved to another HF | N/A | 12 | 13 |
| Language problem | 6 | 13 | 14 |
| Incapable/illness/infirmity | 5 | 14 | 15 |
| Home but unable to contact | 9 | 15 | 16 |
| Away for workload period | 8 | 16 | 17 |
| Away at boarding school/university | 7 |  |  |
| Other reasons | 10 |  |  |
| Household non-contact | N/A | 17 | 18 |
| Household contact made no interviews | N/A | 18 | 19 |
| Household not issued to field - persistent non-respondent | N/A | N/A | 20 |
| Overseas permanently | N/A |  | 21 |
| Household all PSMs non-responding in last 2 waves | N/A | N/A | 22 |
| Permanently incapable from previous wave | N/A |  | 23 |
| Household out of scope NFI | N/A | 19 |  |
| Untraceable overseas | N/A |  | 27 |
| Overseas and aged < 15 | N/A | 20 | 28 |
| Untraceable from prior waves | N/A | N/A | 29 |
| Untraceable determined this wave | N/A | 99 | 99 |

Table 3.6: Different codes for household membership

| Description <br> (applies to_hghhm, _hghhm1 to _hghhm20¹) | Codes used |  |  |
| :--: | :--: | :--: | :--: |
|  | Wave 1 | Wave 2 | Wave 3+ |
| Listed |  |  |  |
| Resident | N/A | 1 | 1 |
| Absent for workload | N/A | 2 | 2 |
| No longer member of household | N/A | 3 | 3 |
| Deceased | N/A | 4 | 4 |
| Not listed |  |  |  |
| Re-joiner/merger | N/A |  | 5 |
| New resident | N/A | 5 | 6 |
| Absent for workload new resident | N/A | 6 | 7 |

Table 3.7: Different codes for new location of mover

| Description <br> (applies to _hgnlc1 to _hgnlc20¹) | Codes Used |  |  |  |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | Wave 1 | Wave 2 | Wave 3-6 | Wave 7 | Wave 8+ |
| Within Australia - new local address | N/A | 2 | 1 | 1 | 1 |
| Within Australia - new non-local address | N/A | 3 | 2 | 2 | 2 |
| Address unknown | N/A | 4 | 3 | 3 | 3 |
| Deceased | N/A | 5 | 4 | 4 | 4 |
| Overseas permanently | N/A |  | 5 |  |  |
| Overseas but not permanently | N/A |  | 6 | 6 |  |
| Overseas | N/A | 1 |  | 5 | 5 |

Table 3.8: Different codes for overall self-completion office code

| Description <br> (applies to _hgscq, _ hgscq1 to _hgscq20¹) | Codes Used |  |
| :--: | :--: | :--: |
|  | Wave 1-8 | Wave 9+ |
| Picked up | 1 | 1 |
| Refused | 2 | 3 |
| To be sent | 3 | 2 |
| Not given | 4 | 4 |
| Provided - not picked up yet |  | 8 |
| Eligible - Update PQ Status |  | 9 |

[^0]
[^0]:    ${ }^{1}$ _hgscq, _hgscq1 to _hgscq20, are only on the Restricted Release.

# 3.10. Missing Value Conventions 

Global codes are used throughout the dataset to identify missing data. These codes are not restated for each variable in the coding framework.

### 3.10.1. Numeric Variables

All missing numeric data are coded into the following set of negative values shown in Table 3.9.

When performing mathematical operations (sum, mean, product etc.) or running a procedure which summarises the data, researchers must first assign or program for the missing values. Failure to do so will give inaccurate or distorted results.

Table 3.9: Missing value conventions for numeric variables

| Code | Description |
| :-- | :-- |
| -1 | Not asked: question skipped due to answer to a preceding question |
| -2 | Not applicable |
| -3 | Don't know |
| -4 | Refused or not answered |
| -5 | Invalid multiple response (SCQ only) |
| -6 | Value implausible (as determined after intensive checking) |
| -7 | Unable to determine value |
| -8 | No Self-Completion Questionnaire returned and matched to individual record |
| -9 | Non-responding household |
| -10 | Non-responding person (Combined File only) |

Note that the SPSS files have these global missing values (-10 to -1 ) set to SPSS userdefined missing. To turn off this setting for an individual variable use:
missing values varname1 ().
To turn off this setting for all variables (for example, if you need to include those who are coded as -1 'Not asked') use the following code:
set errors=none.
do repeat $x=$ all.
missing values $x$ ().
end repeat.
set errors=listing.
execute.

### 3.10.2. Text Variables

Text variables with missing values will contain the text shown in Table 3.10.

Table 3.10: Missing value conventions for text variables

| Text | Description |
| :-- | :-- |
| $[$ blank] | Missing information (no reason specified) |
| -1 | Not asked |
| -2 | Not applicable |
| -3 | Don't know |
| -4 | Refused |
| -7 | Unable to determine value |
| -9 | Non-responding household |

# 3.11. Data With Negative Values 

Data items that can have both negative and positive values, such as business income, total household income, etc., are provided as two variables:

- the variable for positive amounts; and
- the variable for negative amounts.

If the overall value is not missing and is positive, then the negative variable will be zero and the positive variable will hold the actual value. If the overall value is not missing and is negative, then the positive variable will be zero and the negative variable will hold the absolute value of the amount. For example, if we have a person with a business income loss of $\$ 20,000$ in the last financial year, then the positive variable of business income will be zero and the negative variable will be $\$ 20,000$.
Missing data information will be provided in both variables following the negative conventions described above.
Therefore, after handling the missing data, you can create your own variable by subtracting the negative variable from the positive variable. For example, you might set the missing values of business income to system missing and then create a new business income variable as follows:
abifp-abifn
or for the imputed version of business income (which has no missing cases but follows the same convention of splitting positive and negative values):
abifip-abifin

### 3.12. Confidentialisation

The General Release HILDA datasets released have been confidentialised to reduce the risk that individual sample members can be identified. ${ }^{9}$ This has involved:

- withholding some variables (such as day and month of birth, postcode and detailed geography);

[^0]
[^0]:    ${ }^{9}$ For Release 1 to 4 the HILDA data files are referred to as the "Confidentialised" and "Unconfidentialised" files. Between Release 5 to 9 these files were referred to as the "General Release" files and the "Inconfidence Release" files respectively. From Release 10 to 15 these files were referred to as the "General Release" files and the "Unconfidentialised Release" files respectively. From Release 16 onwards these files are referred to as the "General Release" files and the "Restricted Release" files respectively.

- aggregating some variables (for example, occupation has been provided at the two-digit level while it is collected at the four-digit level); and
- top-coding some variables (such as income and wealth variables).

Top-coding substitutes an average value for all the cases which are equal to or exceed a given threshold. The substituted value is calculated as the weighted average of the cases subject to top-coding. As a result, the cross-sectional weighted means of the top-coded variable will be the same as the original variable.
Take, for example, the top-coding of _wscg (current gross wages per week in main job). All cases whose wages are equal to or exceed $\$ 4800$ have had their value replaced by the weighted average of all those cases whose income is equal to or exceeds $\$ 4800$. Let us say that the weighted average of the 22 cases earning $\$ 4800$ or more is $\$ 8450$. $\$ 8450$ is then substituted as the wages for those 22 cases. This provides confidentiality and preserves the weighted distribution means. If the distribution of wages had been simply cut off at $\$ 4800$, when the relevant weights are applied, the mean would be too low.
The top-coding thresholds are adjusted over time to overcome the tendency of income and wealth measures to inflate. Without adjustment, increasing numbers of cases would exceed the threshold and be top-coded. If you need to know the threshold values that have been used at a particular release, see "HILDA-thresholds-by-wave.csv" in the release documentation.