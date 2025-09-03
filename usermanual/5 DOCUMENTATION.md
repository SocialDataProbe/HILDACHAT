# 5. DOCUMENTATION

### 5.1. Documentation Choices

Before you get lost in the array of documentation, it is worth pausing to consider how you work and what documentation is available to you. You will not need to look at all pieces of documentation that have been prepared to use the datasets efficiently.
There are three main pathways through the documentation:

- Marked-up questionnaires for each wave - you would use these if you wanted to find the exact question format or to find other questions asked in a particular module;
- Subject Level Coding framework (cross-wave) - you would use this if you were interested in a couple of different topics or to find what variables are available for a particular subject;
- Cross-wave variable listing - you would use this if you were frequently using variables across the various waves and were happy to find out the codes used when you started using the variables.
The coding frameworks have been provided in the release (as .pdf documents) as well as in the Online Data Dictionary.
You should also consider which documents you want to print out and which you are happy to look at electronically. You might want to print a couple of pages from the marked-up questionnaire and look at the rest of the files on screen where there are search functions available. ${ }^{36}$
While frequencies of the variables have been provided, it is expected that you might only refer to these in the early stages of an analysis (for example, how many employed people do we have in the sample at wave 1, or what are the codes used for question R3).
The documentation is described in more detail below.


### 5.2. Marked-Up Questionnaires

Beside each question in the questionnaires, the associated variable name has been added. Derived variables are not included, only the variables that relate directly to the question asked.
For waves 1 - 12, paper questionnaires were used (though only as a back-up to CAPI in waves 9 - 12), therefore the marked-up questionnaires are an edited version of these questionnaires. See Figure 5.1 for an example.
In wave 13, the paper back-up questionnaires were dropped, thus the marked-up questionnaires provided for the following waves are a paper representation of the CAPI script. See Figure 5.2 for an example.

[^0]
[^0]:    ${ }^{36}$ In Adobe Acrobat, you would begin a search by clicking on the button that looks like this:

Figure 5.1: Example of the marked-up questionnaires, waves 1-12
H9 I am now going to ask you about the amount of contact you have with your (youngest) child who lives elsewhere.

About how many nights each week, fortnight or month does this child usually stay overnight with you?
If respondent refers to weeks rather than nights, record number of full weeks instead of nights.
If overnight contact is sparse, interviewer to get estimate for 3, 6 or 12 month period.
Zero overnight stays in a year 997

ancngth H9 Youngest non-resident child overnight stays - answered nights or weeks
ancngtn H9 Youngest non-resident child overnight stays - number of nights
ancngtnp H9 Youngest non-resident child overnight stays - nights - period
ancngtw H9 Youngest non-resident child overnight stays - number of weeks
ancngtwp H9 Youngest non-resident child overnight stays - weeks - period

Figure 5.2: Example of the marked-up questionnaires, waves 13 onwards
G9b. About how many nights each week, fortnight or month does [IF
'AgeYoungestElsewhere' not 98 or 99: ['NameYoungestElsewhere'] / ELSE this child] usually stay overnight with you?

INTERVIEWER NOTE: If respondent refers to weeks rather than nights, record number of full weeks instead of nights. If overnight contact is sparse, interviewer to get estimate for 3, 6 or 12 month period.
[DISPLAY GRID]
Number [1-182/RF/DK]
[Nights or Weeks [Nights/Weeks/RF/DK]
Frequency
[mncngtn] [mncngtw]
[mncngth]
[mncngtnp] [mncngtwp]

|  | Number |  | Nights or weeks | Frequency |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
| 0 | [1-182] | 0 | Nights | 0 | Per week |
| 0 | Refused | 0 | Weeks | 0 | Fortnight |
| 0 | Don't know | 0 | Refused | 0 | 4 weeks |
|  |  |  | 0 | 3 months | [4] |
|  |  |  |  | 6 months | [5] |
|  |  |  |  | 0 | Year |
|  |  |  |  | 0 | Refused |
|  |  |  |  | 0 | Don't Know |

[997]

# 5.3. Variable Listings 

### 5.3.1. Subject Level Coding Framework

The Subject Level Coding Framework includes the variables of all files (except the Master File and Longitudinal Weights File) by subject. There is an index at the beginning and the broad subject name is at the top of each page to help you navigate through the very long document (See Figure 5.3 below). This is probably the most useful tool of all the documentation options. It provides information on the codes for each variable, the

population, which waves the variable has been asked and which variables they are constructed from or contribute to.

Figure 5.3: Example of the subject coding framework


# 5.3.2. Cross-Wave Index 

The Cross-Wave Index provides a summary of the Subject Level Coding Framework. It provides information on the file in which the variable can be found, the variable label and lists in which wave(s) the variable has been asked. For the example provided Figure 5.4, we can see that these questions have changed from section $H$ in wave 1 to section $G$ in later waves, and that the question numbering has changed slightly in later waves.

Figure 5.4: Example of the cross-wave index (waves 1-6 truncated)

| CHILDREN - Non-Resident Children |  |  |  |  |  |  |  |  |  |  |  | Wave |  |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| File Variable | Data Item |  | 1 | 2 | 3 |  | 4 |  | 5 |  | 6 |  |
| RP _ncmptb | Yonngest non-resident child overnight stays - answered nights or weeks |  | PQ H9 |  | PQ G9 |  | PQ G9b |  | PQ G9b |  | PQ G11b | PQ G9b |
| RP _ncmptu | Yonngest non-resident child overnight stays - number of nights |  | PQ H9 |  | PQ G9 |  | PQ G9b |  | PQ G9b |  | PQ G11b | PQ G9b |
| RP _ncmptup | Yonngest non-resident child overnight stays - nights - period |  | PQ H9 |  | PQ G9 |  | PQ G9b |  | PQ G9b |  | PQ G11b | PQ G9b |
| RP _ncmptw | Yonngest non-resident child overnight stays - number of weeks |  | PQ H9 |  | PQ G9 |  | PQ G9b |  | PQ G9b |  | PQ G11b | PQ G9b |
| RP _ncmptwp | Yonngest non-resident child overnight stays - weeks - period |  | PQ H9 |  | PQ G9 |  | PQ G9b |  | PQ G9b |  | PQ G11b | PQ G9b |

### 5.3.3. Selected Standard Classifications

A standard classification listing has also been provided. For the General Release, this includes a list of country codes and the 2-digit industry and occupation codes. For the Restricted Release, this includes codes for the country, geography, occupation and industry variables.

### 5.4. Frequencies

The frequencies are a simple (unweighted) listing of the categories for each question and the number of cases falling into each category. The frequencies are produced in Stata.
Note that a variable can appear more than once in the same frequencies file. This is because the file is a concatenation of per wave frequencies done at the household, enumerated person and responding person-levels. For example, for Australian State in each frequency file there are 3 tables:
-> tabulation of _hhstate if responding_household
-> tabulation of _hhstate if enumerated_person
-> tabulation of _hhstate if responding_person

### 5.5. Online Data Dictionary

The searchable Online Data Dictionary can be accessed via the HILDA website:
This browser interface is designed to provide easy access to HILDA variable descriptors. The database provides the user with the same information available in the HILDA coding frameworks (.pdf) and includes the questionnaire text and frequencies for most variables.

The Online Data Dictionary only contains variables available in the General Release.
The Online Data Dictionary allows users to search HILDA metadata:

- by keyword,
- by subject area, or
- by variable name.

A help page (accessed by clicking help/information link from the menu at the right of the page) provides instructions on how to use the system along with example screen shots. Any feedback or comments are welcome.