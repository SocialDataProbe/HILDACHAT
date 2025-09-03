# 4. DERIVED VARIABLES

Derived variables are created from the data in the following circumstances:

- When questions are asked in an easy-to-answer form which requires recombination to a common metric.
- When some 'other, specify' answers are coded (notably sources of other income).
- When a complex combination of data occurs (for example, family type; household disposable income).
- When open-ended answers are converted to standard codeframes (industry; occupation; post-school qualifications).
- When missing data are imputed.
- When external data are matched to derive applicable measures (for example, socio-economic indicators for areas; remoteness area).
- When data are carried over or accumulated across waves (history variables).

Derived variables are created at both the household and person-levels. Most derived variables are available each wave. A description of how the variable was derived is supplied in the coding framework and additional information is provided in this manual as necessary.
All derived variables have the prefix 'DV:' or 'History:' in the variable label. Missing values have the same codes as collected data. Derived variables are not annotated on the marked-up questionnaires but are included in the various coding frameworks.

### 4.1. Age and Sex

For each person interviewed, two ages have been provided:

- _hgage which is the age at last birthday as of 30 June immediately preceding the fieldwork for that wave (i.e. for wave 1, ahgage is the respondents age at 30 June 2001); and
- _hhiage which is the age at last birthday as of the date of interview for that wave (the interview dates for each wave spread over 6 to 8 months).
For non-interviewed people in responding households, _hgage is provided on the Enumerated File and the Combined File.
In the Household and Combined Files, the age (at the $30^{\text {th }}$ of June) of each person in the household is derived in the variables _hgage1 to _hgage20, where _hgage1 is for person 01, and so on. These variables are numbered in the order household members were listed on the Household Form and the number at the end of the variable corresponds to the 2character person number _hhpno.
New-born children born between $30^{\text {th }}$ June and the subsequent household structure date are, by convention, assigned an age of 0.
For the small number of cases where age was not provided, it has been imputed via a Hotdeck method ${ }^{10}$. These cases can be identified by the variables _hgagef, _hgagf1 to _hgagf20, and dobf11.

[^0]
[^0]:    ${ }^{10}$ The Hotdeck method seeks to find a donor with a similar set of characteristics to the non-respondent. See Hayes and Watson (2009) for more details.
    ${ }^{11}$ Along with dobf are mobf and yobf which indicate if the month or year has been imputed. These variables are only on the Restricted Release files.

Note that if the respondent provides a correction to the date of birth listed on the Household Form each wave, this correction is applied back through the previous waves. As a result, the above calculated ages may change from one release to another (hopefully not by much!). Therefore, you may find some 14-year-olds interviewed in an earlier wave.
Similarly, if the respondent provides a correction to the sex listed on the Household Form (_hgsex) each wave, this correction is applied back through the previous waves.

# 4.2. History 

History variables contain data accumulated across successive waves. Some history variables contain background information that does not change and is only asked in the first interview (e.g. country of birth). Others contain accumulated statuses (e.g., number of qualifications; current marriage duration). The variables are provided in the Responding Person File each wave from wave 2 onwards and reflect the status at the completion of each wave.
History variables will first have data in the year the respondent entered the survey and are updated the next time the respondent is interviewed. Someone who was a new entrant at say wave 2 and was interviewed, did not respond in wave 3 and was interviewed again in wave 4 will not have history data for waves 1 and 3, even for invariant information such as country of birth. Those using unbalanced panels will be particularly affected and may need to write a program to 'fill-in' the missing years.
History variables have the prefix 'History:' in the variable label. History variables are not annotated on the marked-up questionnaires but are included in the various coding frameworks. Notes about the construction of the variables are included in the coding framework (and are not duplicated here).
Table 4.1 provides a list of the history variables included on the datasets except for the variables relating to the occupation of the respondent's father and mother (which are provided with other occupation variables in Table 4.7).

Table 4.1: History variables

| Variable | Description |
| :-- | :-- |
| Ancestry |  |
| _ancob, _anbcob | Country of birth (full, brief) |
| _anyoa | Year first came to Australia to live |
| _anengf | Is English the first language you learned to speak as a child |
| _anatsi | Aboriginal or Torres Strait Islander origin |
| Family background |  |
| _fmlwop | Were you living with both your own mother and father around the time you <br> were 14 years' old |
| _fmnprea | Why were you not living with both your parents at age 14 |
| _fmpdiv | Did your mother and father ever get divorced or separate |
| _fmpjoin | Did your mother and father ever get back together again |
| _fmageps | How old were you at the time your parents separated |

| Variable | Description |
| :--: | :--: |
| _fmagelh | How old were you when you first moved out of home as a young person |
| _fmhsib | Ever had any siblings |
| _fmnsib | How many siblings |
| _fmeldst | Were you the oldest child |
| _fmfcob | Father's country of birth |
| _fmmcob | Mother's country of birth |
| _fmfemp | Was father in paid employment when you were 14 |
| _fmfuemp | Was father unemployed for 6 months or more while you were growing up |
| _fmmemp | Was mother in paid employment when you were 14 |
| _fmlbbdy | Where your mother was living when you were born - broad |
| _fmlbdty ${ }^{1}$ | Where your mother was living when you were born - detail |
| Education |  |
| _edagels | Age left school |
| _edhists | Highest level of school completed/currently attending |
| _edtypes | Type of school attended/attending |
| _edcly | Country of last school year |
| _edqenr | Ever enrolled in a course of study to obtain a qualification |
| _edcoq | Country completed highest qualification in |
|  | Number of qualifications obtained since leaving school (ASCED): |
| _edq100, _edq110, <br> _edq120, _edq200, <br> _edq211, _edq221, <br> _edq310, _edq311, <br> _edq312, _edq400, <br> _edq411, _edq413, <br> _edq421, _edq500, <br> _edq511, _edq514, <br> _edq521, _edq524, <br> _edq600, _edq611, <br> _edqunk | 100 Postgraduate 120 Master Degree 211 Graduate Diploma 310 Bachelor Degree 312 Bachelor (Pass) Degree 411 Advanced Diploma 421 Diploma 511 Certificate Level IV 521 Certificate Level II 600 Secondary education Unknown - not enough information |
| _edhigh1 | Highest education level achieved |
| _edpsqau ${ }^{2}$ | Highest post school qualification obtained in Australia |
| _edpsqei ${ }^{2}$ | Type of education institution obtained highest post school qualification |
| _edpsqfd ${ }^{2}$ | Main field of study of highest post school qualification |
| _edpsqun ${ }^{2}$ | Which university obtained highest post school qualification from |

| Variable | Description |
| :--: | :--: |
| _edshyau ${ }^{2}$ | Completed highest year of schooling in Australia |
| _edshys ${ }^{2}$ | State or territory where highest year of schooling completed |
| _edrhq ${ }^{3}$ | Respondent determined highest qualification obtained |
| _edslsa ${ }^{2}$ | Since leaving school have you obtained any formal education qualifications |
| _fmfhlq ${ }^{4}$ | Type of institution fathers highest level qualification obtained from |
| _fmfpsq ${ }^{4}$ | Father completed an educational qualification after leaving school |
| _fmfsch ${ }^{4}$ | How much schooling father completed |
| _fmmhlq ${ }^{4}$ | Type of institution mothers highest level qualification obtained from |
| _fmmpsq ${ }^{4}$ | Mother completed an educational qualification after leaving school |
| _fmmsch ${ }^{4}$ | How much schooling mother completed |
| Marriage and De facto Relationships |  |
| _mrn | How many times have you been legally married |
| _mrpmth | Month - present or most recent marriage |
| _mrpyr, _mr1yr, _mr2yr, <br> _mr3yr, _mr4yr | Year (present/most recent marriage, first, second, third, and fourth marriages) |
| _mrplv, _mr1lv, _mr2lv, <br> _mr3lv, _mr4lv | Live together before marriage (present/most recent marriage, first, second, third, and fourth marriages) |
| _mrpend, _mr1end, <br> _mr2end, _mr3end, <br> _mr4end | How did the marriage end (present/most recent marriage, first, second, third, and fourth marriages) |
| _mrpwidw, _mr1widw, <br> _mr2widw, _mr3widw, <br> _mr4widw | Year widowed (present/most recent marriage, first, second, third, and fourth marriages) |
| _mrpsep, _mr1sep, <br> _mr2sep, _mr3sep, <br> _mr4sep | Year separated (present/most recent marriage, first, second, third, and fourth marriages) |
| _mrpdiv, _mr1div, <br> _mr2div, _mr3div, _mr4div | Year divorced (present/most recent marriage, first, second, third, and fourth marriages) |
| _ordfpst | Ever lived with someone for at least one month without marrying |
| _ordfnum | Number of de facto relationships (lasting at least 3 months) |
| _mrplvt, _mr1lvt, _mr2lvt, <br> _mr3lvt, _mr4lvt | Years lived together before marriage (present/most recent marriage, first, second, third, and fourth marriages) |
| _orcdur | Current de facto duration - years |
| _mrcdur | Current marriage duration - years |
| _mrwdur | Current widow duration - years |
| _mrsdur | Current separated or divorced from date of separation - years |

Variable Description

## Children

_tchad $^{5} \quad$ Total children ever had
_tcdied $^{5} \quad$ Total children since died

## Employment

| _rtage | Age retired/intends to retire |
| :-- | :-- |
| _ehtse | Time since FT education - years |
| _ehtjb | Time in paid work - years |
| _ehtuj | Time unemployed and looking for work - years |
| _ehto | Time not working and not looking for work - years |

## Health ${ }^{6}$

_hespncy, _heheary, _hespchy, _hebflcy, _hesluy, _heluafy, _hedgty, _helufly, _henecy, _hecrpay, _hecrpht, _hemigy, _hedisfy, _hemirhy, _hesbdby, _hecrpy, _hehibdy, _hemedy, _heothy

Year condition first developed
-Sight problems not corrected by glasses/lenses
-Hearing problems
-Speech problems
-Blackouts, fits or loss of consciousness
-Difficulty learning or understanding things
-Limited use of arms or fingers
-Difficulty gripping things
-Limited use of feet or legs
-A nervous or emotional condition which requires treatment
-Any condition which restricts physical activity or physical work (e.g. back problems, migraines)
-Any condition which restricts physical activity or physical work (e.g. back problems) ${ }^{6}$
-Frequent headaches or migraine ${ }^{6}$
-Any disfigurement or deformity
-Any mental illness which requires help or supervision
-Shortness of breath or difficulty breathing
-Chronic or recurring pain
-Long term effects as a result of a head injury, stroke or other brain damage
-Long term condition or ailment which is still restrictive even though it is being treated or medication is being taken for it
-Other long term condition such as arthritis, asthma, heart disease, Alzheimer's disease, dementia etc.

## Housing

_hsyrcad Years at current address

## Migration ${ }^{8}$

| _annzcit | Were you a New Zealand citizen when you arrived in Australia |
| :-- | :-- |
| _anaf99 | Did respondent arrive in Australia after 1999 |
| _anpapp | Australian visa - Primary applicant |

| Variable | Description |
| :-- | :-- |
| _anmigc | Migration category when you or your family first arrived in Australia |
| _anafpay | Who paid for your (air)fare to come to Australia |
| _anref | Did you (and your family) come to Australia as refugees or under a <br> humanitarian migration program |
| _ancitiz | Australian citizenship |

${ }^{1}$ Only in the Restricted Release file
${ }^{2}$ Wave 5 onwards
${ }^{3}$ For these variables, 'children' refers to the respondent's natural and adopted children
${ }^{4}$ Wave 3 onwards
${ }^{5}$ Wave 4 onwards
${ }^{6}$ Waves 16 and 20 only
${ }^{7}$ First asked in wave 22, and thereafter just in the first interview. Combined from wave 22 and answers from NPQ for new persons.
${ }^{8}$ Waves 12, 16 and 20 only
${ }^{9}$ First asked in wave 4, and thereafter just in the first interview. Combined from wave 4 and answers from NPQ for new persons. Updated in wave 18 (citizenship, section K) by the year became an Australian Citizen.

# 4.3. Geography ${ }^{12}$ 

The household addresses from each wave have been geocoded and are assigned the following:

- 2001 Census Collection District (CD);
- 2006 Census CD;
- 2011 Statistical Area Level 1 (SA1) and 2011 Local Government Area;
- 2016 Statistical Area Level 1 (SA1); and
- 2021 Statistical Area Level 1 (SA1) and 2021 Local Government Area.

Where the address details were not sufficient to geocode exactly, the nearest cross section or street segment was used. Further, some fuzzy matching and manual look-up of maps were employed where the street name or suburb did not provide a reasonable match.
We build up from the 2001 CD level to the following geographic regions:

- Statistical Local Area (SLA);
- Local Government Area (LGA);
- Statistical Sub-Division (SSD);
- Statistical Division (SD);
- Section of State (SOS);
- Major Statistical Region (MSR); and
- Remoteness Area (RA).

We also build from 2011 and 2021 SA1s to these regions:

- Statistical Area Level 2 (SA2);
- Statistical Area Level 3 (SA3);

[^0]
[^0]:    ${ }^{12}$ The 2001 and 2006 geography are based on the Australian Bureau of Statistics (ABS) Australian Standard Geographical Classification. The 2011, 2016 and 2021 geography are based on the Australian Statistical Geography Standard (ASGS). This geographic classification is supplied in addition to the ASGC. See https://www.abs.gov.au/statistics/statistical-geography/australian-statistical-geography-standardasgs.

- Statistical Area Level 4 (SA4);
- Greater Capital City Statistical Area (GCCSA);
- Section of State (SOS); and
- Remoteness Area (RA).

Table 4.2 lists the derived geographic variables. Aside from the area identifiers, several other geographic variables are included on the file such as:

- Socio-Economic Indexes for Areas (SEIFA) - deciles are assigned for four types of SEIFA scores based on the assigned 2001 Census CD (or the assigned SLA if no SEIFA score is available for the CD; see Section 3.2 in "ABS 2039.0 Information Paper: Census of Population and Housing -- Socio-Economic Indexes for Areas, Australia, 2001"). An additional series for SEIFA 2011 has been added based on ASGS SA1. If the SA1 is not available, then the SA2 SEIFA scores are used;
- The distance moved from the last wave - this is calculated from the geocoded addresses. Where the geocoding had to be approximated and the household moves close by, there may be some households who have moved but the distance moved is calculated as zero.
Other related geographic variables which are not derived that you should be aware of are State (_hhstate) and whether the household has moved from the last wave (_hhmove).

Table 4.2: Derived geographic variables

| Variable | Description |
| :--: | :--: |
| ahhcd96 ${ }^{1}$ | ABS 1996 Census Collection District |
| _hhcd01 ${ }^{1}$ | ABS 2001 Census Collection District |
| _hhsla ${ }^{1}$, _hhsla9 ${ }^{1}$ | ASGC 2001 Statistical Local Area (5-digit, 9-digit) |
| _hhlga ${ }^{1}$ | ASGC 2001 Local Government Area |
| _hhssd ${ }^{1}$ | ASGC 2001 Statistical Subdivision |
| _hhsd ${ }^{1}$ | ASGC 2001 Statistical Division |
| _hhmsr | ASGC 2001 Major Statistical Region |
| _hhsos | ASGC 2001 Section of State |
| _hhra | ASGC 2001 Remoteness area |
| _hhda ${ }^{1}$, _hhad ${ }^{1}$, <br> _hhec ${ }^{1}$, _hhed ${ }^{1}$ | SEIFA 2001 Index of: <br> - relative socio-economic disadvantage <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhda10, _hhad10, <br> _hhec10, _hhed10 | SEIFA 2001 Decile of Index of: <br> - relative socio-economic disadvantage <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhcd06 ${ }^{1}$ | ABS 2006 Census Collection District |

| Variable | Description |
| :--: | :--: |
| _hhssa1 ${ }^{1}$ | ASGS 2011 Statistical Area Level 1 (SA1) 7-digit |
| _hhssa2 ${ }^{1}$ | ASGS 2011 Statistical Area Level 2 (SA2) 5-digit |
| _hhssa3 ${ }^{1}$ | ASGS 2011 Statistical Area Level 3 (SA3) 5-digit |
| _hhssa4 ${ }^{1}$ | ASGS 2011 Statistical Area Level 4 (SA4) 3-digit |
| _hhslga ${ }^{1}$ | ASGS 2011 Local Government Area (LGA) |
| _hhsgcc | ASGS 2011 Greater Capital City Statistical Area (GCCSA) |
| _hhssos | ASGS 2011 Section of State (SOS) |
| _hhsra | ASGS 2011 Remoteness Area (RA) |
| _hhsad ${ }^{1}$, _hhsec ${ }^{1}$, <br> _hhsed ${ }^{1}$ | SEIFA 2011 Index of: <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhsad10, <br> _hhsec10, <br> _hhsed10 | SEIFA 2011 Decile of Index of: <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhsa116 ${ }^{1}$ | ASGS 2016 Statistical Area Level 1 (SA1) 7-digit |
| _hhs3sa1 ${ }^{1}$ | ASGS 2021 Statistical Area Level 1 (SA1) 11-digit |
| _hhs3sa2 ${ }^{1}$ | ASGS 2021 Statistical Area Level 2 (SA2) 9-digit |
| _hhs3sa3 ${ }^{1}$ | ASGS 2021 Statistical Area Level 3 (SA3) 5-digit |
| _hhs3sa4 ${ }^{1}$ | ASGS 2021 Statistical Area Level 4 (SA4) 3-digit |
| _hhs3lga ${ }^{1}$ | ASGS 2021 Local Government Area (LGA) |
| _hhs3gcc | ASGS 2021 Greater Capital City Statistical Area (GCCSA) |
| _hhs3sos | ASGS 2021 Section of State (SOS) |
| _hhs3ra | ASGS 2021 Remoteness Area (RA) |
| _hhs3ad ${ }^{1}$, <br> _hhs3ec ${ }^{1}$, <br> _hhs3ed ${ }^{1}$ | SEIFA 2021 Index of: <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhs3add, <br> _hhs3ece, <br> _hhs3edd | SEIFA 2021 Decile of Index of: <br> - relative socio-economic advantage/disadvantage <br> - economic resources <br> - education and occupation |
| _hhmovek2, <br> _hhmovem2 | Distance person moved since last wave (kilometres, miles) |
| _hhmvehk2, <br> _hhmvehm2 | Distance household moved since last wave (kilometres, miles) |

[^0]
[^0]:    ${ }^{1}$ Variables are only on the Restricted Release files. See the Selected Standard Classifications.pdf for the coding framework. These variables have too many values to be included in the conventional frameworks.
    ${ }^{2}$ Wave 2 onwards.

# 4.4. Current Education 

The education questions have been used to derive variables (listed in Table 4.3) based on the Australian Standard Classification of Education (ASCED) ${ }^{13}$. There are a series of variables at the 3-digit ASCED level which contain information about:
the number of qualifications completed (for new respondents only);
which qualifications the respondent is currently studying for; and
which qualifications have been obtained since the last interview (for continuing respondents only).
Where a qualification cannot be categorised to the detailed level (for example, 211 Graduate Diploma or 221 Graduate Certificate), the broader category has been used (for example, 200 Graduate Diploma and Graduate Certificate).
Unless you are specifically interested in what qualifications the respondent has completed since the last interview, you should use the history variables described earlier in Section 4.2 (which combines the answers provided in the current and previous wave interviews).

Table 4.3: Derived current education variables

| Variable | Description |
| :--: | :--: |
| Number of qualifications of people interviewed for the first time (ASCED) ${ }^{1}$ |  |

# Qualifications currently studying for (ASCED) 

| _edcq100, _edcq110, | 100 Postgraduate | 110 Doctoral Degree |
| :-- | :-- | :-- |
| _edcq120, _edcq200, | 120 Master Degree | 200 Grad Diploma and Grad Certificate |
| _edcq211, _edcq221, | 211 Graduate Diploma | 221 Graduate Certificate |
| _edcq310, _edcq311, | 310 Bachelor Degree | 311 Bachelor (Honours) Degree |
| _edcq312, _edcq400, | 312 Bachelor (Pass) Degree | 400 Advanced Diploma and Diploma |
| _edcq411, _edcq413, | 411 Advanced Diploma | 413 Associate Degree |
| _edcq421, _edcq500, | 421 Diploma | 500 Certificate - don't know level |
| _edcq511, _edcq514, | 511 Certificate Level IV | 514 Certificate Level III |
| _edcq521, _edcq524, | 521 Certificate Level II | 524 Certificate Level I |
| _edcq600, _edcq611, | 600 Secondary education | 611 Year 12 |
| _edcqunk | Unknown - not enough information |  |

## Qualifications obtained since last interview (ASCED) ${ }^{1}$

| _edrq100, _edrq110, | 100 Postgraduate | 110 Doctoral Degree |
| :--: | :--: | :--: |
| _edrq120, _edrq200, | 120 Master Degree | 200 Grad Diploma and Grad Certificate |
| _edrq211, _edrq221, | 211 Graduate Diploma | 221 Graduate Certificate |
| _edrq310, _edrq311, | 310 Bachelor Degree | 311 Bachelor (Honours) Degree |
| _edrq312, _edrq400, | 312 Bachelor (Pass) Degree | 400 Advanced Diploma and Diploma |
| _edrq411, _edrq413, | 411 Advanced Diploma | 413 Associate Degree |
| _edrq421, _edrq500, | 421 Diploma | 500 Certificate - don't know level |
| _edrq511, _edrq514, | 511 Certificate Level IV | 514 Certificate Level III |
| _edrq521, _edrq524, | 521 Certificate Level II | 524 Certificate Level I |
| _edrq600, _edrq611, | 600 Secondary education | 611 Year 12 |
| _edrqunk | Unknown - not enough information |  |
| _edfts | Full-time student |  |
| _edrhqn ${ }^{2}$ | Respondent determined recent highest qualification obtained |  |

${ }^{1}$ Wave 2 onwards.
${ }^{2}$ Waves 16 and 20 only.

### 4.5. Current Marital Status and De facto Relationships

The relationship section of the Person Questionnaires involves relatively complicated skips (especially from wave 2 onwards), so several partnering variables have been derived as set out in Table 4.4

Table 4.4: Derived current marital status and de facto relationship variables

| Variable | Description |
| :-- | :-- |
| _mrcurr | Marital status from Person Questionnaire |
| _ordflt1 | NPQ: Years living together, first de facto excluding current |
| _ordfrit2 | NPQ: Years living together, most recent de facto excluding current |
| _rg01-_rg203 | Relationship of self to persons 1 to 20 |
| _rg02_01 - _rg20_193 | Relationships between all household members |

[^0]
[^0]:    ${ }^{1}$ Wave 1 and 4 onwards (NPQ).
    ${ }^{2}$ Waves 2 and 3 only.
    ${ }^{3}$ Wave 18 onwards. Relationship type was expanded in wave 18. From Release 18, derived variables have been created to show the previous relationship type structure.

# 4.6. Children 

Table 4.5 shows the various variables that have been created from the family formation section of the Person Questionnaires, including:

- the count of the number of the respondent's own resident and non-resident children (natural or adopted) of various ages, and the age of the respondent's own youngest child;
- the conversion into a common scale for the number of days or nights a child spends with their (other) parent; and
- the total child maintenance paid or received.

Table 4.5: Derived children variables
Variable Description

## All Children

| _icn $^{1}$ | How many more children do you intend to have |
| :-- | :-- |
| _icniz $^{2}$ | How many more children do you intend to have (including zero) |
| _tcyng | Age youngest own child (excl. resident foster/step/grandchild) |

## Resident Children

| _tcr | Count of own resident children (excl. resident foster/step/grandchild): total |
| :--: | :--: |
| _tcr04, _tcr514, <br> _tcr1524, _tcr25 | Count of own resident children and resident step/foster/grandchildren without parent in household, aged 0-4, 5-14, 15-24, 25+ |
| _rcyng | Age youngest resident own child (excl. resident foster/step/grandchildren) |
| _rcngt | Resident child overnight stays with other parent (days per annum) |
| _rcday | Resident child day visits with other parent (days per annum) |
| _rcefspy ${ }^{3}$ | Resident child maintenance paid - annual - all children (\$) |
| _rcefsry ${ }^{3}$ | Resident child maintenance received - annual - all children (\$) |
| arcefsy ${ }^{3}$ | Child maintenance received - annual - all children (\$) |

## Non-resident Children

| _tcnr, tcn04, tcn514, | Count of own non-resident children: total, aged 0-4, 5-14, 15-24, 25+ |
| :--: | :--: |
| tcn1524, tcn25 |  |
| _ncyng | Age youngest non-resident own child |
| _ncngt | Overnight stays of non-resident child (Days per annum) |
| _ncday | Day visits of non-resident child (Days per annum) |

| Variable | Description |
| :-- | :-- |
| _ncefspy2 | Non-resident child maintenance paid - annual - all children (\$) |
| _ncefsry2 | Non-resident child maintenance received - annual - all children (\$) |
| ancefsy2 | Child maintenance paid - annual - all children (\$) |

${ }^{1}$ Variable derived in waves $5,8,11,15,19$ and 23 (Fertility module). This question is asked in all other waves.
${ }^{2}$ Variable asked in waves $5,8,11,15,19$ and 23 (Fertility module).
${ }^{3}$ In wave 1, the question only asked how much child maintenance they paid for non-resident children and how much they received for resident children. From wave 2 onwards, the questions were reworded to pay (_ncefspy, _rcefspy) or receive (_ncefsry, _rcefsry) for both non-resident and resident children.

# 4.7. Child Care 

The variables from the child care grids in the Household Questionnaire are used to produce several summary variables (which are shown in Table 4.6). The children referred to in this section of the HQ are those living in the household aged under 15 and these are split into two groups:

- School-aged children - these children are of an age to attend school (that is, from age 4 or 5 , depending on the State).
- Children not yet at school - these children are aged 0 to 3 or 4 , depending on the State. ${ }^{14}$

The child care questions have changed several times across the waves in the following ways:

- The reason the child care was used - In wave 1, only information about child care used while the parents were working was collected. From wave 2, questions were included about the child care used so parent could undertake non-employment related activities (such as studying, exercising, shopping, etc.).
- The level of detail collected for non-employment related child care - For waves 2 through 4, summary information was collected about the use of non-employment related child care. From wave 5, these grids contain a similar level of detail to the employment related child care grids.
- The level of detail collected for the cost of employment related child care - In wave 1, the cost of each type of child care for each child was collected. From wave 2 onwards, the total cost for each type of child care for the two groups of children (school aged and those not yet at school) was collected.
- The level of detail for relatives looking after children - The types of child care that referred to 'relatives' in waves 1 to 3 were split into 'grandparents' and 'other relatives' from wave 4 onwards.

The child care summary variables indicate whether a particular type of child care is used, along with the hours and cost (summed across the relevant children). As some of these summary variables have been collected directly from the respondent in some or all waves (particularly with respect to cost), derived and non-derived variables are listed in Table 4.6 as appropriate for completeness.

[^0]
[^0]:    ${ }^{14}$ Up to wave 4, the questionnaire referred to the children not yet at school as 'pre-school' children. The shorter name was used in the questionnaire for space reasons, but the interviewers were briefed on the intent of these questions to include all children who were not yet at school (not just those who aged 3 or 4 who are attending pre-school). The variable labels relating to the children not yet at school have been revised to use the 'not yet at school' terminology rather than the 'pre-school' terminology.

Table 4.6: Child care variables

|  | While parents work |  |  | While parents are not working |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | School-aged <br> (term time) | School-aged (holidays) | Not yet at school | School-aged | Not yet at school |

# Type of care used 

Me or my partner
The child's brother or sister
Child looks after self
Child comes to my workplace
A relative who lives with us
A relative who lives elsewhere
Child's grandparent who lives with us
Child's grandparent who lives elsewhere
Other relative who lives with us
Other relative who lives elsewhere
A friend or
neighbour coming to our home
A friend or
neighbour in their home
A paid sitter or nanny
Family day care
Formal outside of school hours care
Out of hours care at child's school
Out of hours care elsewhere
Vacation care
Vacation care at child's school
Vacation care elsewhere
Long day care centre at workplace

```
_csu_me
_csu_bs
_csu_bf
_csu_sf
_csu_wp
_csu_ru
_csu_re
_csu_re
_csu_gu
_csu_ge
_csu_ga
_csu_ao
_csu_fo
_csu_fo
_csu_ft
_csu_ps
_csu_fd
_csu_fd
_csu_fc
_csu_os
_csu_oe
_chu_vc
_chu_vs
_chu_ve
```

_cpu_med
_cpu_ps
_cpu_ff
_cpu_ff
_cpu_ps
_cpu_ff
_cpu_ff
_cpu_ps ${ }^{1}$
_chu_ff
_cpu_ps
_cpu_ff
_cpu_ff ${ }^{1}$
_cpu_ps ${ }^{4,7}$
_cnpu_ru ${ }^{4,7}$
_cnpu_ru ${ }^{4,7}$
_cnpu_ru ${ }^{4,7}$
_cnpu_ru ${ }^{4,7}$
_cnpu_ru ${ }^{4,7}$
_cnpu_gr4,7
_cnpu_gr4,7
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{2}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$
_cnpu_gr ${ }^{3}$

|  | While parents work |  |  | While parents are not working |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | School-aged <br> (term time) | School-aged (holidays) | Not yet at school | School-aged | Not yet at school |
| Private or community long day care centre |  |  | _cpu_pd | _cnsu_pd ${ }^{3}$ | _cnpu_pd ${ }^{3}$ |
| Kindergarten/preschool |  |  | _cpu_kp | _cnsu_kp ${ }^{4,7}$ | _cnpu_kp ${ }^{3}$ |
| Other parent not living in household/expartner | _csu_op | _chu_op | _cpu_op |  |  |
| Not applicable Boarding school | _csu_br | _chu_br ${ }^{8}$ |  | _cnsu_br ${ }^{5,7}$ |  |
| Other 1 | _csu_o1 | _chu_o1 | _cpu_o1 | _cnsu_o1 ${ }^{3}$ | _cnpu_o1 ${ }^{3}$ |
| Other 2 | _csu_o2 | _chu_o2 | _cpu_o2 | _cnsu_o2 ${ }^{3}$ | _cnpu_o2 ${ }^{3}$ |
| Not answered | _csu_na | _chu_na | _cpu_na | _cnsu_na ${ }^{3}$ | _cnpu_na ${ }^{3}$ |
| None |  |  |  | _cnsu_np ${ }^{3}$ | _cnpu_np ${ }^{3}$ |
| Hours |  |  |  |  |  |
| The child's brother or sister | _csh_bs | _chh_bs | _cph_bs | _cnsh_bs ${ }^{3}$ | _cnph_bs ${ }^{3}$ |
| Child looks after self | _csh_sf | _chh_sf |  |  |  |
| Child comes to my workplace | _csh_wp | _chh_wp |  |  |  |
| A relative who lives with us | _csh_ru ${ }^{1}$ | _chh_ru ${ }^{1}$ | _cph_ru ${ }^{1}$ | _cnsh_ru ${ }^{4,7}$ | _cnph_ru ${ }^{4,7}$ |
| A relative who lives elsewhere | _csh_re ${ }^{1}$ | _chh_re ${ }^{1}$ | _cph_re ${ }^{1}$ | _cnsh_re ${ }^{4,7}$ | _cnph_re ${ }^{4,7}$ |
| Child's grandparent who lives with us | _csh_gu ${ }^{2}$ | _chh_gu ${ }^{2}$ | _cph_gu ${ }^{2}$ | _cnsh_gu ${ }^{2}$ | _cnph_gu ${ }^{2}$ |
| Child's grandparent who lives elsewhere | _csh_ge ${ }^{2}$ | _chh_ge ${ }^{2}$ | _cph_ge ${ }^{2}$ | _cnsh_ge ${ }^{2}$ | _cnph_ge ${ }^{2}$ |
| Other relative who lives with us | _csh_au ${ }^{2}$ | _chh_au ${ }^{2}$ | _cph_au ${ }^{2}$ | _cnsh_au ${ }^{2}$ | _cnph_au ${ }^{2}$ |
| Other relative who lives elsewhere | _csh_ae ${ }^{2}$ | _chh_ae ${ }^{2}$ | _cph_ae ${ }^{2}$ | _cnsh_ae ${ }^{2}$ | _cnph_ae ${ }^{2}$ |
| A friend or neighbour coming to our home | _csh_fo | _chh_fo | _cph_fo | _cnsh_fo ${ }^{3}$ | _cnph_fo ${ }^{3}$ |
| A friend or neighbour in their home | _csh_ft | _chh_ft | _cph_ft | _cnsh_ft ${ }^{3}$ | _cnph_ft ${ }^{3}$ |
| A paid sitter or nanny | _csh_ps | _chh_ps | _cph_ps | _cnsh_ps ${ }^{3}$ | _cnph_ps ${ }^{3}$ |
| Family day care | _csh_fd | _chh_fd | _cph_fd | _cnsh_fd ${ }^{3}$ | _cnph_fd ${ }^{3}$ |

|  | While parents work |  |  | While parents are not working |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | School-aged (term time) | School-aged (holidays) | Not yet at school | School-aged | Not yet at school |
| Formal outside of school hours care | _csh_fc ${ }^{2}$ |  |  | _cnsh_fc ${ }^{2}$ |  |
| Out of hours care at child's school | _csh_os ${ }^{1}$ |  |  |  |  |
| Out of hours care elsewhere | _csh_oe ${ }^{1}$ |  |  |  |  |
| Vacation care |  | _chh_vc ${ }^{2}$ |  |  |  |
| Vacation care at child's school |  | _chh_vs ${ }^{1}$ |  |  |  |
| Vacation care elsewhere |  | _chh_ve ${ }^{1}$ |  |  |  |
| Long day care centre at workplace |  |  | _cph_wd |  |  |
| Private or community long day care centre |  |  | _cph_pd | _cnsh_pd ${ }^{3}$ | _cnph_pd ${ }^{3}$ |
| Kindergarten/ preschool |  |  | _cph_kp ${ }^{7}$ | _cnsh_kp ${ }^{4}$ | _cnph_kp ${ }^{3}$ |
| Other 1 | _csh_o1 | _chh_o1 | _cph_o1 | _cnsh_o13 | _cnph_o13 |
| Other 2 | _csh_o2 | _chh_o2 | _cph_o2 | _cnsh_o23 | _cnph_o23 |
| Cost |  |  |  |  |  |
| Total cost | _csctc | _chctc | _cpctc | _nsctc ${ }^{3}$ | _npctc ${ }^{3}$ |
| The child's brother or sister |  |  |  | _cnsc_bs ${ }^{7}$ | _cnpc_bs ${ }^{7}$ |
| Child comes to my workplace | _csc_wp | _chc_wp |  |  |  |
| A relative who lives with us | _csc_ru ${ }^{1}$ | _chc_ru ${ }^{1}$ | _cpc_ru ${ }^{1}$ | _cnsc_ru ${ }^{4}$ | _cnpc_ru ${ }^{4,7}$ |
| A relative who lives elsewhere | _csc_re ${ }^{1}$ | _chc_re ${ }^{1}$ | _cpc_re ${ }^{1}$ | _cnsc_re ${ }^{4}$ | _cnpc_re ${ }^{4,7}$ |
| Child's grandparent who lives with us | _csc_gu²,7 | _chc_gu²,7 | _cpc_gu²,7 | _cnsc_gu²,7 | _cnpc_gu²,7 |
| Child's grandparent who lives elsewhere | _csc_ge ${ }^{2,7}$ | _chc_ge ${ }^{2,7}$ | _cpc_ge ${ }^{2,7}$ | _cnsc_ge ${ }^{2,7}$ | _cnpc_ge ${ }^{2,7}$ |
| Other relative who lives with us | _csc_au²,7 | _chc_au²,7 | _cpc_au²,7 | _cnsc_au²,7 | _cnpc_au²,7 |
| Other relative who lives elsewhere | _csc_ae ${ }^{2,7}$ | _chc_ae ${ }^{2,7}$ | _cpc_ae ${ }^{2,7}$ | _cnsc_ae ${ }^{2,7}$ | _cnpc_ae ${ }^{2,7}$ |
| A friend or neighbour coming to our home | _csc_fo | _chc_fo | _cpc_fo | _cnsc_fo ${ }^{3,7}$ | _cnpc_fo ${ }^{3,7}$ |
| A friend or neighbour in their home | _csc_ft | _chc_ft | _cpc_ft | _cnsc_ft3,7 | _cnpc_ft ${ }^{3,7}$ |

|  | While parents work |  |  | While parents are not working |  |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  | School-aged <br> (term time) | School-aged (holidays) | Not yet at school | School-aged | Not yet at school |
| A paid sitter or nanny | _csc_ps | _chc_ps | _cpc_ps | _cnsc_ps ${ }^{3,7}$ | _cnpc_ps ${ }^{3,7}$ |
| Family day care | _csc_fd | _chc_fd | _cpc_fd | _cnsc_fd ${ }^{3,7}$ | _cnpc_fd ${ }^{3,7}$ |
| Formal outside of school hours care | _csc_fc ${ }^{2,7}$ |  |  | _cnsc_fc ${ }^{2,7}$ |  |
| Out of hours care at child's school | _csc_os ${ }^{1}$ |  |  |  |  |
| Out of hours care elsewhere | _csc_oe ${ }^{1}$ |  |  |  |  |
| Vacation care |  | _chc_vc ${ }^{2,7}$ |  |  |  |
| Vacation care at child's school |  | _chc_vs ${ }^{1}$ |  |  |  |
| Vacation care elsewhere |  | _chc_ve ${ }^{1}$ |  |  |  |
| Long day care centre at workplace |  |  | _cpc_wd |  |  |
| Private or community long day care centre |  |  | _cpc_pd | _cnsc_pd ${ }^{3,7}$ | _cnpc_pd ${ }^{3,7}$ |
| Kindergarten/preschool |  |  | _cpc_kp | _cnsc_kp ${ }^{4,7}$ | _cnpc_kp ${ }^{3,7}$ |
| Other parent not living in household/expartner | _csc_op ${ }^{2,7}$ | _chc_op ${ }^{2,7}$ | _cpc_op ${ }^{2,7}$ |  |  |
| Not applicable Boarding school | _csc_br ${ }^{2,7}$ | _chc_br ${ }^{2,7}$ |  |  |  |
| Other 1 | _csc_o1 | _chc_o1 | _cpc_o1 | _cnsc_o1 ${ }^{3,7}$ | _cnpc_o1 ${ }^{3,7}$ |
| Other 2 | _csc_o2 | _chc_o2 | _cpc_o2 | _cnsc_o2 ${ }^{3,7}$ | _cnpc_o2 ${ }^{3,7}$ |
| Not answered |  | _chc_na ${ }^{2,7}$ |  |  |  |

# Total annual child care cost 

_ccactci3 Annual child care total cost (\$) [estimated]
_ccactcf3
Imputation flag annual child care total cost [estimated]

[^0]
[^0]:    ${ }^{1}$ Waves 1 to 3.
    ${ }^{2}$ From wave 4.
    ${ }^{3}$ From wave 2.
    ${ }^{4}$ Waves 2 and 3.
    ${ }^{5}$ Wave 3 only.
    ${ }^{6}$ Wave 1 and 3 onwards.
    ${ }^{7}$ These variables are not part of the derived variable list, but provided in this table for completeness.
    ${ }^{8}$ Waves 1 and 2 only.

# 4.8. Occupation and Industry 

The occupation and industry derived variables are listed in Table 4.7. The occupation and industry variables for waves 1 to 6 have been coded to two codeframes (correspondence conversion of the old codeframe to the new was only used if there was a 1-to-1 match between the old and new codeframes, otherwise the collected verbatim responses for waves 1 to 6 were coded into the new codeframe variables in 2008). From wave 7 onwards, only the new codeframes have been used.
The occupation variables were coded to the 4-digit Australian Standard Classification of Occupations (ASCO 1997) and to the 4-digit Australian and New Zealand Standard Classification of Occupations (ANZSCO 2006). These are then used to code:

- the 1-digit and 2-digit ASCO and ANZSCO codes;
- ANU4 occupational status scale which ranges from 0 to 100 (based on ASCO);
- AUSEI occupational status scale which also ranges from 0 to 100 (based on ANZSCO); and
- the 2-digit and 4-digit International Standard Classification of Occupation-88 (ISCO-88) codes based on both codeframes.
The industry variables were coded to the 4-digit First Edition and Second Edition of the Australian and New Zealand Standard Industry Classification (ANZSIC 1993 and 2006 respectively). These are then used to produce:
- the division level and 2-digit ANZSIC codes; and
- the 2-digit International Standard Industry Classification (ISIC) codes (only based on ANZSIC 2006).
The 4-digit ASCO, ISCO and ANZSIC codes are available on the Restricted Release files only.
For the occupation of the respondent's mother and father, users will find it easier to use the history variables listed in the following table rather than to compile the answers from the first interview each respondent provided. ${ }^{15}$
Users of the occupation and industry variables should be aware of the data quality issues associated with the coding of these variables (see Watson and Summerfield (2009)).

Table 4.7: Derived occupation and industry variables

|  | Occupation |  | Industry |  |
| :--: | :--: | :--: | :--: | :--: |
|  | Based on <br> ASCO 1997 | Based on <br> ANZSCO 2006 | Based on <br> ANZSIC 1993 | Based on <br> ANZSIC 2006 |
| Current main job |  |  |  |  |
| 1-digit | _jbmocc12 | _jbmo61 | _jbmind12 | _jbmi61 |
| 2-digit | _jbmocc22 | _jbmo62 | _jbmind22 | _jbmi62 |
| 4-digit ${ }^{4}$ | _jbmocc ${ }^{1,2}$ | _jbmo06 ${ }^{1}$ | _jbmind ${ }^{1,2}$ | _jbmi06 ${ }^{1}$ |

[^0]
[^0]:    ${ }^{15}$ The NPQ ASCO variables are _fmfoccn, _fmfocn2, _fmfocn1 for father's 4-digit, 2-digit and 1-digit occupation and _fmmoccn, _fmmocn2, _fmmocn1 for mother's 4-digit, 2-digit and 1-digit occupation. The equivalent ANZSCO variables are _fmfo6n, _fmfo6n2, _fmfo6n1, _fmmo6n, _fmmo6n2, _fmmo6n1. These are combined into the history variables together with the wave 1 responses.

|  | Occupation |  | Industry |  |
| :--: | :--: | :--: | :--: | :--: |
|  | Based on <br> ASCO 1997 | Based on <br> ANZSCO 2006 | Based on <br> ANZSIC 1993 | Based on <br> ANZSIC 2006 |
| ISC 2-digit ${ }^{5}$ | - | _jbm682 | - | _jbmii2 |
| ISC 4-digit ${ }^{5}$ | - | _jbm688 ${ }^{1}$ | - | - |
| Status scale ${ }^{6}$ | _jbmoccs ${ }^{2}$ | _jbmo6s | - | - |

Previous job (for those currently employed and answering the CPQ)

| 1-digit | _pjoocc13 | _pjoo618 | _pjoind13 | _pjoi618 |
| :--: | :--: | :--: | :--: | :--: |
| 2-digit | _pjoocc23 | _pjoo628 | _pjoind23 | _pjoi628 |
| 4-digit ${ }^{4}$ | _pjoocc ${ }^{1,3}$ | _pjoo06 ${ }^{1,8}$ | _pjoind ${ }^{1,3}$ | _pjoi06 ${ }^{1,8}$ |
| ISC 2-digit ${ }^{5}$ | - | _pjo6828 | - | _pjoii28 |
| ISC 4-digit ${ }^{5}$ | - | _pjo688 ${ }^{1,8}$ | - | - |
| Status scale ${ }^{6}$ | _pjooccs ${ }^{3}$ | _pjoo6s ${ }^{8}$ | - | - |

Previous job (for those not currently employed and answering the CPQ)

| 1-digit | _pjotoc13 | _pjoto619 | _pjotin13 | _pjoti619 |
| :--: | :--: | :--: | :--: | :--: |
| 2-digit | _pjotoc23 | _pjoto629 | _pjotin23 | _pjoti629 |
| 4-digit ${ }^{4}$ | _pjotocc ${ }^{1,3}$ | _pjoto06 ${ }^{1,9}$ | _pjotind ${ }^{1,3}$ | _pjoti06 ${ }^{1,9}$ |
| ISC 2-digit ${ }^{5}$ | - | _pjot6829 | - | _pjotii29 |
| ISC 4-digit ${ }^{5}$ | - | _pjot688 ${ }^{1,9}$ | - | - |
| Status scale ${ }^{6}$ | _pjotocs ${ }^{3}$ | _pjoto6s ${ }^{9}$ | - | - |

Last job (for those not currently employed and answering the NPQ)

| 1-digit | _ujljoc12 | _ujjjo61 | _ujljin12 | _ujjji61 |
| :--: | :--: | :--: | :--: | :--: |
| 2-digit | _ujljoc22 | _ujjjo62 | _ujljin22 | _ujjji62 |
| 4-digit ${ }^{4}$ | _ujljocc ${ }^{1,2}$ | _ujjjo06 ${ }^{1}$ | _ujljind ${ }^{1,2}$ | _ujjji06 ${ }^{1}$ |
| ISC 2-digit ${ }^{5}$ | - | _ujlj682 | - | _ujjji2 |
| ISC 4-digit ${ }^{5}$ | - | _ujlj688 ${ }^{1}$ | - | - |
| Status scale ${ }^{6}$ | _ujljocs ${ }^{2}$ | _ujjjo6s | - | - |

Father's job (around the time the respondent was 14 years old - history variable)

| 1-digit | _fmfocc12 | _fmfo61 | - | - |
| :-- | :-- | :-- | :-- | :-- |
| 2-digit | _fmfocc22 | _fmfo62 | - | - |
| 4-digit | _fmfocc ${ }^{1,2}$ | _fmfo06 ${ }^{1}$ | - | - |
| ISC 2-digit ${ }^{5}$ | - | _fmf682 | - | - |
| ISC 4-digit ${ }^{5}$ | - | _fmf688 ${ }^{1}$ | - | - |
| Status scale ${ }^{6}$ | _fmfoccs ${ }^{2}$ | _fmfo6s | - | - |

|  | Occupation |  | Industry |  |
| :--: | :--: | :--: | :--: | :--: |
|  | Based on <br> ASCO 1997 | Based on <br> ANZSCO 2006 | Based on <br> ANZSIC 1993 | Based on <br> ANZSIC 2006 |

Mother's job (around the time the respondent was 14 years old - history variable)

| 1-digit | _fmmocc1 ${ }^{2}$ | _fmmo61 | - | - |
| :--: | :--: | :--: | :--: | :--: |
| 2-digit | _fmmocc2 ${ }^{2}$ | _fmmo62 | - | - |
| 4-digit | _fmmocc ${ }^{1,2}$ | _fmmo06 ${ }^{1}$ | - | - |
| ISC 2-digit ${ }^{5}$ | - | _fmm682 | - | - |
| ISC 4-digit5 | - | _fmm688 ${ }^{1}$ | - | - |
| Status scale ${ }^{6}$ | _fmmoccs ${ }^{2}$ | _fmmo6s | - | - |

Father's job (around the time the respondent was 14 years old - wave 1 collected data) ${ }^{7}$

| 1-digit | - | - | - | - |
| :-- | :--: | :--: | :--: | :--: |
| 2-digit | afmfoc2o | afmfo62o | - | - |
| 4-digit ${ }^{4}$ | afmfocco1 | afmfo06o ${ }^{1}$ | - | - |
| ISC 2-digit5 | - | afmf682o | - | - |
| ISC 4-digit5 | - | afmf688o ${ }^{1}$ | - | - |
| Status scale ${ }^{6}$ | afmfocos | afmfo6os | - | - |

Mother's job (around the time the respondent was 14 years old - wave 1 collected data) ${ }^{7}$

| 1-digit | - | - | - | - |
| :-- | :--: | :--: | :--: | :--: |
| 2-digit | afmmoc2o | afmmo62o | - | - |
| 4-digit4 | afmmocco ${ }^{1}$ | afmmo06o ${ }^{1}$ | - | - |
| ISC 2-digit5 | - | afmm682o | - | - |
| ISC 4-digit5 | - | afmm688o ${ }^{1}$ | - | - |
| Status scale6 | afmmocos | afmmo6os | - | - |

${ }^{1}$ Variables are only on the Restricted Release files.
${ }^{2}$ Waves 1-6 only.
${ }^{3}$ Wave 2-6 only.
${ }^{4}$ These variables are not part of the derived variable list but provided in this table for completeness.
${ }^{5}$ ISC=International standard classification. Occupation was coded to ISCO-88. Industry was coded to ISIC 3.1.
${ }^{6}$ Occupation status scale based on ASCO is the ANU4 status score whereas it is the AUSEI status score for ANZSCO.
${ }^{7}$ In wave 1 only, the family background questions B7 to B16 were skipped if the respondent was still living with both parents. A set of derived variables were created in Release 1 with the information added for these respondents if both parents were interviewed (in Releases 1 to 11 these derived versions had "d" appended to the variable name). From Release 12 both the collected and derived wave 1 variables are renamed. Collected variable names now have "o" (for original) appended, and the derived variables have had the "d" removed. This makes the history variables consistent across waves.
${ }^{8}$ Waves 2-19 only.
${ }^{9}$ Wave 2 onwards.

# 4.9. Other Employment 

The other employment related derived variables are listed in Table 4.8. The history variables in Section 4.2 should first be consulted if you are attempting to piece together information about previous employment spells as some of the work may already be done.

In all waves except wave 2, the labour force status of individuals was asked on the Household Form, which provides useful information in the weighting and imputation processes for non-respondents. We have imputed the broad labour force status for all those people enumerated in wave 2 (see Hayes and Watson (2009) for details of how this was done).

Table 4.8: Other derived employment variables

| Variable | Description |
| :--: | :--: |
| _esdtl, _esbrd | Labour force status (detail, broad) |
| _esempdt | Current employment status (detailed) - classifies whether there are employees in the respondent's own business |
| _hhura | Unemployment rate for persons in same major statistical region |
| _jbhruc, _jbmhruc | Hours per week usually worked (all jobs, main job) |
| _jbhrqf | Data Quality Flag: hours of work main job vs all jobs |
| _jbtprhr | Hours would like to work |
| _es | Employment status in main job if currently employed |
| _jbmtuea | Union membership or employee association |
| _jbcasab | Casual worker (ABS definition: no paid holiday leave, no paid sick leave) |
| _jbocct, _jbempt | Tenure (years): <br> - in current occupation (years) <br> - with current employer (years) |
| ewcpd, _wcapd ${ }^{6}$ | Days of paid workers compensation in last 12 months: <br> - total <br> - absent from work |
| _alpd ${ }^{1}$, _alsk ${ }^{1}$, _alop ${ }^{1}$, <br> _alup ${ }^{1}$ | Days if leave in last 12 months: <br> - paid annual leave <br> - paid sick leave <br> - paid (maternity, paternity, bereavement, family, carers) leave <br> - unpaid leave |
| _tatrwrk | Taken part in any work-related training in the past 12 months |
| _tatrcst | Contributed to cost of job-related training (fees/materials/books/paid for travel/took unpaid leave) |
| _tatrdsg ${ }^{2}$, _tatrhgs ${ }^{2}$, <br> _tatrhsc ${ }^{2}$, _tatrisc ${ }^{2}$, <br> _tatrmps ${ }^{2}$, _tatrpfj ${ }^{2}$, <br> _tatros ${ }^{2}$, _tatrdk ${ }^{3}$, <br> _tatrrf ${ }^{3}$, _tatrna ${ }^{3}$ | Aim of this training <br> - To develop your skills generally <br> - To help you get started in your job <br> - Because of health / safety concerns <br> - To improve your skills in your current job <br> - To maintain professional status and/or meet occupational standards <br> - To prepare you for a job you might do in the future or to facilitate promotion <br> - Other aims <br> - Don't know <br> - Refused <br> - No answer |
| _jst | Weeks unemployed |
| _ujlhruc ${ }^{4}$ | Hours per week worked in last job |
| _ujljws | Pay in last job per annum |

| Variable | Description |
| :-- | :-- |
| _ujijt | Tenure with last employer (years) |
| _molt | Months since did activity required by Centrelink/Employment services <br> provider |
| ajbperm | Permanently unable to work |
| bhgebi | Household Form labour force status - broad [imputed] |
| bhgebf | Imputation flag Household Form labour force status - broad |
| _jbmtabs ${ }^{5}$ | Trade Union membership - ABS defined |
| bhgebi1 to bhgebi20 | Household Form labour force status - broad [imputed] |
| bhgebf1 to bhgebf20 | Imputation flag Household Form labour force status - broad |

${ }^{1}$ Wave 5 onwards.
${ }^{2}$ Waves 3-6 only.
${ }^{3}$ Waves 5-6 only.
${ }^{4}$ Wave 2 onwards.
${ }^{5}$ Wave 9 onwards.
${ }^{6}$ Wave 6 onwards.

# 4.10. Calculating Hourly Wage Rates 

The following aims to point you in the right direction if you want to calculate hourly wage rates. You would use the following derived variables:

- _esbrd Broad labour force status
- _jbhruc Combined hours per week usually worked in all jobs
- _wscei Imputed current weekly gross wages \& salary in all jobs

The hourly wage rate can be calculated in SPSS as follows:
if (aesbrd=1 and ajbhruc>0 and awscei>0) hwr01 = awscei/ajbhruc.
if (besbrd=1 and bjbhruc>0 and bwscei>0) hwr02 = bwscei/bjbhruc.
if (lesbrd=1 and ljbhruc>0 and lwscei>0) hwr12 = lwscei/ljbhruc.
The above code calculates the hourly wage rate (across all their jobs) if the respondent:

- is employed;
- has current wages and salaries; and
- has usual hours worked in all jobs.

If you wish to look at respondents that are full-time and part-time employed separately, use _esdtl (detailed labour force status) to define these groups. The cases that did not need to be imputed can be identified using the flag _wscef $=0$.
If you wish to look at the hourly wage in the respondent's main job, use _wscmei and _jbmhruc.
Please note that the questions about hours worked and income are asked in separate sections of the Person Questionnaire. As some respondents report low wages and salaries with high hours and vice versa, it is important that users are aware that there are some odd cases when deriving hourly wage rates. This is, unfortunately, unavoidable.

# 4.11. Employment and Education Calendar 

The employment and education calendar contain over 1000 variables. Before you trawl through these variables and create your own summary variables, check if one of the derived calendar variables in Table 4.9 may help you. These derived variables typically relate to the financial year, while the calendar may stretch from 14 to 18 months, depending on the interview date.

Table 4.9: Derived employment and education calendar variables

| Variable | Description |
| :-- | :-- |
| _capeft, _capept, _capj, | Per cent time in last financial year spent in: |
| _capune, _capnif | - full-time education |
|  | - part-time education |
|  | - jobs |
|  | - unemployed |
|  | - not in the labour force |
| _cafnj | Number of jobs in last financial year |
| _cantp | Number of time periods answered in calendar |

### 4.12. Family Relationships

The relationship grid on the Household Form collects the relationship of everyone in the household to each other. This information is then used to assign people to family groups and identify what relationship they hold within the family, and what type of family and household they belong to; based on the ABS Standards for Statistics on the Family. ${ }^{16}$
In overview, family type (_hhfty) is derived by first assigning a relationship in household (_hhrih) to each member. These individuals are collected into families and assigned a family number (_hhfam) and a hierarchical description of the family type (_hhfty). Household type (_hhtype) is then assigned based on the combination of family and nonfamily members within the household. Finally, income units (_hhiu) are assigned to subsets of the family thought to systematically pool their income and savings.
The core relationships that make a family are a couple relationship or a parent-child relationship. Others in the household are attached as appropriate to these core relationships to form families. _hhrih defines each person's relationship in the household with the following categories:

1. Couple with child under 15 - part of a married or de facto couple with at least one child under 15 in the household (they may also have other children which are dependent students or not dependent).
2. Couple with dependent student (no child under 15) - part of a married or de facto couple with at least one child in the household who is a dependent student (they may also have other children which are not dependent). They do not have any children under 15 in the household.
3. Couple with non-dependent child (no child under 15 or dependent student) - part of a married or de facto couple with at least one child in the household who is not dependent. They do not have any children in the household who are under 15 or dependent students.
[^0]
[^0]:    ${ }^{16}$ ABS, Standards for Statistics on the Family (ABS Cat. No. 1286.0), ABS, Canberra, 1995.

4. Couple without children - part of a married or de facto couple without children in the household.
5. Lone parent with child under 15 - a parent without a partner with at least one child under 15 in the household (they may also have other children which are dependent students or not dependent).
6. Lone parent with dependent student (no child under 15) - a parent without a partner with at least one child in the household who is a dependent student (they may also have other children which are not dependent). They do not have any children under 15 in the household.
7. Lone parent with non-dependent child (no child under 15 or dependent student) - a parent without a partner with at least one child in the household who is not dependent. They do not have any children who are under 15 or dependent students in the household.
8. Child under 15 - A child who is aged under 15.
9. Dependent student - A dependent student is aged 15 to 24, studying full-time, not working full-time and lives in a household with their parent (natural, step, foster or adopted). ${ }^{17}$ They do not have a partner or child of their own in the household (if they did, they would be classified as a couple or lone parent themselves).
10. Non-dependent child - A child who is at least 15 years of age living in a household with their parent (natural, step, foster or adopted) who does not fall into the category of a dependent student. They do not have a partner or child of their own in the household.
11. Other family member - A person who is not part of a couple or parent-child relationship but is related to other members of the household.
12. Lone person - A single person household.
13. Unrelated to all household members - A person who is not related to any other members of the household.
There are several key points to note about how the families are defined when there are multiple ways to describe the relationship in the household:

- A couple relationship takes precedence over a parent-child relationship (see Figure 4.1. In a household with a mother, father, son and son's de facto partner, the son's couple relationship takes precedence over his relationship to his parents. This household would be a multi-family household, with the mother and father as a couple in one family and the son and his de facto partner in another family.
- The most recent generation has precedence over an older generation and the older generation is then considered an 'other relative'. Figure 4.2 illustrates this case with only two people in the household. The core relationship is defined by the mother-daughter generation (Before Child). However, when the daughter has a daughter herself, that younger generation then takes precedence and forms the core relationship (After Child) and the original mother is considered to be a relative (a grandmother).

[^0]
[^0]:    ${ }^{17}$ Note that this definition of a dependent student is different to the full-time student identifier provided on the Responding Person File.

- When there are two ex-partners living together with their children, the mother and children are considered a lone parent family and the father is considered to be an 'other related' individual.
- Children aged under 15 living in a household without a natural, adopted, step or foster parent are attached to their closest relative. If they are without relatives, then they are attached to the person thought most likely to form a parent-child relationship with that child.

Figure 4.1: Family where a new de facto relationship is formed
Before son's de facto partner moves in After son's de facto partner moves in


$$
\begin{aligned}
& \text { rih }=3 \text { : Couple with non-dependent child } \\
& \text { rih }=4 \text { : Couple without child } \\
& \text { rih }=10 \text { : Non-dependent child }
\end{aligned}
$$

Figure 4.2: Family where a new child is born


Once the relationships in the household have been classified, the individuals are formed into families, households and income units. The description for family type is constructed from three parts - the type of core relationship, the type of the most dependent child in the family, and who else is attached to the family (see Figure 4.3). For example, a couple family with a child under 15 and two non-dependent children without any other people in the household (related or unrelated) would be classified as a "couple family with children < 15 without others".

Figure 4.3: Construction of family type description

Similarly, the description of household type is made up of these three elements with the further allowance for others not related, group households and multi-family households (see Figure 4.4).

<Figure 4.4: Construction of household type description>

[Type of Core Unit]          -->  [Type of Most Dependent Child]   -->  [Type of Others Attached to Family]
---------------------               ------------------------------       -------------------------------------
• Couple family                     • Without children                   • Without others
• Lone parent                       • With child < 15                    • With others related (e.g., aunts,
                                    • With dependent student               uncles, grandparents)
                                    • With non-dependent child           • With others not related


[Type of Core Unit]          -->  [Type of Most Dependent Child]   -->  [Type of Others Attached to Family]
---------------------               ------------------------------       -------------------------------------
• Other related family              • Without children                   • Without others
                                                                         • With others not related

[Type of Core Unit]
 ---------------------  
• Lone person
• Group household
• Multiple family household

</Figure 4.4: Construction of household type description>

The income units are derived from the family units and separate out the non-dependent children and other related or non-related individuals from the rest of the family. The family in Figure 4.5 is divided into 3 income units The first income unit (1) includes mother, father, a dependent student and a child under 15. Each non-dependent child forms their own income unit (income units 2 and 3 ).

Figure 4.5: Income units in a family with child under 15, dependent student and non-dependent children

Along with the variables based on the relationship grid, several other variables are listed in Table 4.10 including identifiers for various people in the household and counts of the number of people in certain age groups. The partner, father, mother and other biological relationship identifiers were discussed in Section 3.6.

Table 4.10: Derived family variables

| Variable | Description |
| :--: | :--: |
| _hhtype | Household type |
| _hhrih ${ }^{1}$ | Relationship in household |
| _hhfam ${ }^{1}$ | Family number (zero for lone persons and unrelated individuals) |
| _hhfty ${ }^{1}$ | Family type |
| _hhiul | Income unit |
| _hhpxid, <br> _hhfxid, <br> _hhmxid, <br> _hhbmxid, <br> _hhbfxid, <br> _hhtwxid, <br> _hhmgmxd, <br> _hhmgfxd, <br> _hhpgmxd, <br> _hhpgfxd | Cross-wave person number (7-digit) of: <br> - partner <br> - father <br> - mother <br> - ever co-resident biological mother <br> - ever co-resident biological father <br> - ever co-resident twin <br> - ever co-resident maternal grandmother <br> - ever co-resident maternal grandfather <br> - ever co-resident paternal grandmother <br> - ever co-resident paternal grandfather |
| _hhprtid, _hhfid, _hhmid, <br> _hhtwid | 2-digit person number within household of: <br> - partner <br> - father <br> - mother <br> - twin |
| _hhyng, _hhold | Age of youngest and oldest person in household. Weighted top-code |
| _hh0_4, _hh5_9, <br> _hh10_14, _hhadult | Number of persons at June 30 aged: <br> $-0-4$ years <br> $-5-9$ years <br> $-10-14$ years <br> $-15+$ years |
| _hhd0_4, _hhd4_18², <br> _hhd5_9, _hhd1014, <br> _hhd1524 | Number of dependent children (including partner's children) at June 30 aged: <br> $-0-4$ years <br> $-4-18$ years <br> $-5-9$ years <br> $-10-14$ years <br> $-15-24$ years |

${ }^{1}$ On the Household File, these variables are listed for each person that is _hhrih01 to _hhrih20, _hhfam01 to _hhfam20, _hhfty01 to _hhfty20, and _hhiu01 to _hhiu20. (Note that variables for persons 19 and 20 are only included from Release 16.)
${ }^{2}$ Wave 9 only as required to calculate Australian Government Bonus payments.

# 4.13. Health 

Each wave the SF-36 instrument is included within the Self-Completion Questionnaire. The SF-36 Health Survey is an internationally recognised diagnostic tool for assessing functional health status and well-being. It comprises 36 items which provide multi-item scales measuring each of eight distinct health concepts. Following the scoring rules outlined in Ware et al. (2000), each of these eight scales has been transformed into a 0-100 index. The individual scores for each of these indices have been provided as derived

variables in the dataset. In addition, the SF-6D health state classification has also been derived from the SF-36 (as outlined in Brazier, Roberts and Deverill, 2002) along with a version using Australian weights (Norman et al, 2014).
From wave 6, respondents are asked to record their height and weight in the SelfCompletion Questionnaire. This is used to derive their body mass index. Further information on the quality of the height and weight data is provided in Wooden and Watson (2008).
Kessler-10 was asked for the first time in wave 7 (question B17 in the SCQ). A description of the associated derived variables is provided in Wooden (2009b). The derived health variables are listed in Table 4.11.

Table 4.11: Derived health variables

| Variable | Description |  |  |
| :--: | :--: | :--: | :--: |
| _ghpf, _ghrp, _ghbp, <br> _ghgh, _ghvt, _ghsf, <br> _ghre, _ghmh | SF-36 transformed: <br> - physical functioning <br> - general health <br> - role-emotional | - role-physical <br> - vitality <br> - mental health | - bodily pain <br> - social functioning |
| _ghrht | SF-36 reported health transitions - raw |  |  |
| _ghsf6d | SF-6D Health state classification |  |  |
| _ghsf6ap, _ghsf6an | SF-6D Health state classification - Australian weights (positive and negative values). By HILDA convention the value is the difference of the values $>=0$ |  |  |
| _bmht ${ }^{1}$ | Height in centimetres |  |  |
| _bmwt ${ }^{1}$ | Weight in kilograms |  |  |
| sbmdwt | Desired weight in kilograms |  |  |
| sbmewt | Expected weight in kilograms |  |  |
| _bmi ${ }^{1}$ | Body Mass Index |  |  |
| _bmwhr ${ }^{2}$ | Waist to height ratio |  |  |
| _hedep ${ }^{3}$ | Diagnosed with serious illness - Depression or anxiety |  |  |
| _hepmdep ${ }^{3}$ | Takes prescription medication for - Depression or anxiety |  |  |
| _pdk10s ${ }^{4}$ | Kessler Psychological Distress Scale (K10) score |  |  |
| _pdk10rc ${ }^{4}$ | Kessler Psychological Distress Scale (K10) risk categories |  |  |
| _hcbwk1-105 | Birth weight ( kg ) - child 1-10 (aged < 15) |  |  |
| _hclbw1-105 | Low birth weight - child 1-10 (aged < 15) |  |  |
| _hcgpc1-105 | Sees a particular GP or clinic if sick or needs health advice - child 1-10 (aged < 15) |  |  |
| _hcgpn1-105 | Number of doctor visits - child 1-10 (aged < 15) |  |  |
| _hchan1-105 | Number of hospital admissions - child 1-10 (aged < 15) |  |  |
| _hchnn1-105 | Number of nights in hospital - child 1-10 (aged < 15) |  |  |
| _hegpc ${ }^{5}$ | Sees a particular GP or clinic if sick or needs health advice |  |  |
| _hegpn ${ }^{5}$ | Number of doctor visits |  |  |

| Variable | Description |
| :-- | :-- |
| _hehan ${ }^{6}$ | Number of hospital admissions |
| _hehnn ${ }^{5}$ | Number of nights in hospital |
| _helv10 ${ }^{4}$ | How likely that you will live to 75 or at least 10 more years |

${ }^{1}$ Wave 6 onwards.
${ }^{2}$ Every $4^{\text {th }}$ wave from Wave 13.
${ }^{3}$ Wave 17 and 21 only. Starting wave 17, depression and anxiety were separated into 2 response categories.
${ }^{4}$ Every second wave from wave 7.
${ }^{5}$ Every $4^{\text {th }}$ wave from Wave 9.
${ }^{6}$ Waves 4 , and every $4^{\text {th }}$ wave from wave 9.
In wave 13, 17 and 21, respondents were asked to record their waist circumference in the SCQ using the tape measure provided. In our editing process, we found that many respondents seemed to have provided their waist measurement in inches or were simply implausible (see Eisenmann (2005), Ford et al. (2012)). Please refer to the Subject Level Coding Framework for further information on the editing undertaken on this variable (_bmwaist).

# 4.14. Time Use 

Table 4.12 lists derived time use variables which combine the hours and minutes spent in a week on various activities.

Table 4.12: Derived time use variables

| Variable | Description |
| :-- | :-- |
| _lsemp, _lscom, _lserr, | Combined hrs/mins per week: |
| _lshw, _lsod, _lschd, | - Paid employment |
| _lsocd, _lsvol, _lscar | - Travelling to/from paid employment |
|  | - Household errands |
|  | - Housework |
|  | - Outdoor tasks |
|  | - Playing with your children |
|  | - Playing with other people's children |
|  | - Volunteer/Charity work |
|  | - Caring for disabled/elderly relative |

### 4.15. Personality

In wave 5 respondents were questioned on their personality character traits using a 36 -item inventory. The approach used was based on the trait descriptive adjectives approach used by Saucier (1994), which in turn was based on the approach employed by Goldberg (1992), both of which assume a 5 -factor structure (as is commonly assumed in the literature). Not all 36 items, however, are used in the five derived scales summarizing the 5 personality factors. First, the ex-ante scales were tested for item reliability, with any items omitted if item total correlation was less than 0.3 . Second, principal components analysis with a fivefactor solution was undertaken, with items only retained if their highest factor loading was on the expected factor, exceeded 0.4 and exceeded the second highest factor loading by at least 0.1. A slightly different approach to derivation of these scales, but which obtains identical conclusions, is provided in Losoncz (2009).
The five scales based on the Big Five are listed in Table 4.13 below. These scales are composed by taking the average of the following items:

- Extroversion - talkative, bashful (reversed), quiet (reversed), shy (reversed), lively, and extroverted.

- Agreeableness - sympathetic, kind, cooperative, and warm.
- Conscientiousness - orderly, systematic, inefficient (reversed), sloppy (reversed), disorganised (reversed), and efficient.
- Emotional stability - envious (reversed), moody (reversed), touchy (reversed), jealous (reversed), temperamental (reversed), and fretful (reversed).
- Openness to experience - deep, philosophical, creative, intellectual, complex, imaginative.
The higher the score, the better that personality character trait describes the respondent.
The items and derived scales were repeated in wave 9, and every 4 waves onwards.
Table 4.13: Derived personality variables

| Variable ${ }^{1}$ | Description |  |
| :--: | :--: | :--: |
| _pnextrv, _pnagree, <br> _pnconsc, _pnemote, <br> _pnopene | Personality scale: <br> - Extroversion <br> - Conscientiousness <br> - Openness to experience | - Agreeableness <br> - Emotional stability |

${ }^{1}$ Every $4^{\text {th }}$ wave from Wave 5.

# 4.16. Religion 

In waves $4,7,10$, and every 4 waves onwards, respondents were asked about their religion. _religb describes their broad religion classification (using the Australian Standard Classification of Religious Groups $1996^{18}$ ).

### 4.17. Cognitive Ability Tasks

In wave 12 and 16, respondents were asked to undertake one or more cognitive ability tests. All respondents (face-to-face and telephone interviews) were asked to undertake the Backwards Digit Span, a generic test of working memory span. If the interview was face-toface, two further tests were undertaken, the symbol-digits modalities test and a shortened (25-item) version of the National American Reading Test. For the test sources see Appendix 1b. For further information about the three cognitive ability tasks, their development and their properties, see Wooden (2013).

Table 4.14: Cognitive Ability Scores

| Variable ${ }^{1}$ | Description |
| :-- | :-- |
| _ctbds | Backwards digits score |
| _ctwps | Word pronunciation score (25-item NART) |
| _ctsds | Symbol-digit modalities score |

${ }^{1}$ Waves 12 and 16 only.

### 4.18. Physical Activity and Sleep

Respondents are asked about the time spent in vigorous physical activities, moderate physical activities and time spent walking. They are also asked about hours of sleep on workday nights and on non-work nights. For further information about these measures, see Wooden (2014).

[^0]
[^0]:    ${ }^{18}$ ABS, Australian Standard Classification of Religious Groups (ABS, Cat. No. 1266.0) ABS, Canberra, 1996.

Table 4.15: Physical activity and sleep variables

| Variable | Description |
| :-- | :-- |
| _apvigd $^{1}$ | Vigorous Physical Activity - Minutes per day |
| _apvigw $^{1}$ | Vigorous Physical Activity - Minutes per week |
| _apmodd $^{1}$ | Moderate Physical Activity - Minutes per day |
| _apmodw $^{1}$ | Moderate Physical Activity - Minutes per week |
| _apwlkd $^{1}$ | Walking - Minutes per day |
| _apwlkw $^{1}$ | Walking - Minutes per week |
| _aptmet $^{1}$ | Total physical activity MET (Metabolic Equivalent of Task) - Minutes per <br> week (IPAQ) |
| _apcat $^{1}$ | Categorical Physical Activity |
| _slhrwk $^{2}$ | Hours of sleep per week |

${ }^{1}$ Waves 13 and 17 only.
${ }^{2}$ Every $4^{\text {th }}$ wave from Wave 13.

# 4.19. Death 

In 2014 the sample was matched to the National Death Index so that details of the date and cause of death could be added to the data files. For cases deemed to have a suitable match, their household and interview outcomes were updated. More details of the death matching are provided in Watson and Summerfield (2014). The table below lists the new variables that have been added to the Master File.

Table 4.16: Death variables

| Variable | Description |
| :-- | :-- |
| yodeath | Year of death [inc. match to National Death Index (NDI) (2014)] |
| dodeath $^{1}$ | Date of death [inc. match to National Death Index (NDI) (2014)] |
| Icdeath $^{1}$ | Leading cause of death [match to National Death Index (NDI) (2014)] |
| mcdeath $^{1}$ | Major cause of death (major ICD-10 chapters) [match to National Death <br> Index (NDI) (2014)] |
| Isdeath | Information source for death |
| aadeath | Age at death |

${ }^{1}$ Variables are only on the Restricted Release files.

### 4.20. Parents

In waves $8,12,15,19$ and 23 the 'History and Status of Parents' module was asked. This collects either the parent's year of birth or their current age (if still living), and, if deceased, the respondent's age when the parent died. This information has been converted to year of birth and year of death. This module is not asked again once both parents are known to be deceased.

Table 4.17: Parent derived variables

| Variable ${ }^{1}$ | Description |
| :-- | :-- |
| _psyobf | Father's year of birth |
| _psyobm | Mother's year of birth |
| _psyodf | Father's year of death |
| _psyodm | Mother's year of death |

${ }^{1}$ Waves $8,12,15,19$ and 23 only.

# 4.21. Main job location 

Starting in wave 17, respondents were asked the town, suburb or locality of the place where they usually work in their main job. They were also asked if they knew the postcode of this location. This information has been used to derive the variables listed in the table below.

Table 4.18: Main job location derived variables ${ }^{1}$

| Variable | Description |
| :-- | :-- |
| _jbmlha | Main job location of work varies |
| _jbmlkm | Main job location distance between work and home ASGS postal area <br> centroids (kilometres) |
| _jbmlkr | Main job location distance between work and home ASGS postal area <br> centroids (range) |
| _jbmlpc | Main job location of work ASGS postal area (POA) |

${ }^{1}$ Wave 17 onwards.
${ }^{2}$ Variables are only on the Restricted Release files.

### 4.22. Incentive Payment Method

From wave 20, information was collected on the how the incentive was paid for the Person Questionnaire and Self-Completion Questionnaire.

Table 4.19: Incentive payment method variables

| Variable | Description |
| :-- | :-- |
| _hhscqpm ${ }^{1}$, hhscqp22, hhscqp3 ${ }^{3}$ | SCQ Payment Method |
| _hhpqpm ${ }^{1}$, hhpqpm22 | PQ Payment Method |

${ }^{1}$ Wave 20 only.
${ }^{2}$ Wave 21 and Wave 22.
${ }^{3}$ Wave 23 onwards.

### 4.23. Mother's location of birth

From wave 21, respondents were asked where their mother was living when they were born. From this information, we have created two derived variables (listed in Table 4.20). _fmlbbd contains the ASGS 2021 Greater Capital City Statistical Area (GCCSA) codes, whereas _fmlbdt contains a 2-digit GCCSA value where the respondent selected from the list, however, where a response was provided in 'Other' or was a rural locality, we have coded these localities to a 3-digit ASGS 2021 Statistical Area Level 4 (SA4) code. From wave 23, history variables have been created (see Section 4.2)

Table 4.20: Mother's location of birth variables ${ }^{1}$

| Variable | Description |
| :-- | :-- |
| _fmlbbd | Where your mother was living when you were born - broad |
| _fmlbdt ${ }^{2}$ | Where your mother was living when you were born - detail |

${ }^{1}$ Wave 21 onwards.
${ }^{2}$ Restricted Release file only

# 4.24. Gender Identity 

From wave 22, we collected information on a respondent's sex recorded at birth and gender in the Self-Completion Questionnaire. From these questions we have derived variables in accordance with the 2020 ABS Gender and Cisgender and Trans and Gender Diverse Classification ${ }^{19}$.

Table 4.21: Gender Identity ${ }^{1}$

| Variable | Description |
| :-- | :-- |
| _scgndr | Gender |
| _scsxgn | Cisgender and Transgender and Gender Diverse Classification |

${ }^{1}$ Restricted Release files only.

### 4.25. Income

### 4.25.1. Income, Tax and Family Benefits Model

A great deal of income information is collected in the Person Questionnaire every wave, most of which relates to the completed financial year immediately preceding the date of interview (for example, 2000-2001 in wave 1). This information is used to construct several variables for financial year income components, which are presented in Figure 4.6, Figure 4.7 and Figure 4.8 for the Household File, enumerated person file and responding person file, respectively. In addition, there are several other income components shown in these figures that are calculated by HILDA staff based on the circumstances of sample members. The figures also show how all the income components are combined to produce more aggregated income components, such as 'market income', and to produce disposable income (total income after receipt of government benefits and deduction of income tax).
Here we provide an overview of how the derived income variables are produced. For full details, see Wilkins (2014).
Derived variables for Australian Government benefits are also provided which reflect the structure of the benefit system. These derived variables comprise:

- Australian Government income support payments ${ }^{20}$, which are further disaggregated into:
- Pensions;
- Parenting Payments; and
- Allowances.

[^0]
[^0]:    ${ }^{19}$ Standard for Sex, Gender, Variations of Sex Characteristics and Sexual Orientation Variables (https://www.abs.gov.au/statistics/standards/standard-sex-gender-variations-sex-characteristics-and-sexual-orientation-variables/latestrelease).
    ${ }^{20}$ These include the Coronavirus Supplement paid to certain income support recipients in 2019-20 and 2020-21

- Australian Government non-income support payments, which are further disaggregated into:
- Family payments (estimated as described below); and
- Other non-income support payments.
- Other domestic government and Australian Government benefits with not enough information to allow classification; and
- Other regular public payments (including scholarships).

Respondents are not asked to report the family payments Family Tax Benefit Part A, Family Tax Benefit Part B, Maternity Allowance (paid up to and including 2003-04) and Maternity Payment (paid from 2004-05 to 2006-07). These are instead calculated based on eligibility criteria and payment rates (inclusive of Commonwealth Rent Assistance) and added to the other income components to produce total financial year income. Full details on the calculation of these government benefits are available in Wilkins (2014).
Until wave 8, Baby Bonus payments were not obtained from respondents; instead, they were calculated, since the payment was universal and a lump sum. From 1 January 2009 until its abolition on 1 March 2014, the Baby Bonus was subject to an income test and was paid in 13 fortnightly installments. As a result, in waves 9 to 14, respondents were asked to report Baby Bonus payments received in the current week (up until wave 13 only) and in the previous financial year. This resulted in a new variable for current Baby Bonus payments in waves 9 to 14.
For the previous financial year, while respondents were asked to report Baby Bonus payments, due to apparent under-reporting and non-reporting of amounts, we continued to estimate them based on date of birth of the child(ren), eligibility rules and payment rates. Note that the income test was based on income in the 6 months following the birth of the child, which is not available in the HILDA data, and so was approximated as equal to $50 \%$ of the mother's partner's annual income plus 10\% of the mother's annual income.
First appearing in the 2008-2009 financial year, various 'bonus' payments have been made by the federal government. They include 2008-09 stimulus payments, 2011-12 Clean Energy Advance Payments, 2011-12 to 2016-17 Schoolkids Bonus payments and 2019-20 to 2020-21 Economic Support Payments. While respondents are asked to report these payments, the values reported in the HILDA Survey data are derived for each enumerated person from calculations based on eligibility criteria and payment rates. They are aggregated into the variable _bnfboni ${ }^{21}$ (enumerated person file) and are a component of Australian public transfers (_bnfapti). Note that the bonus payments are all non-taxable.
In addition to financial-year income information, the HILDA Survey also obtains from respondents current (survey reference week) wage and salary income and current government benefit income. No attempt is made to collect other income components for the survey reference week. Correspondingly, current aggregated income variables, including current disposable income, are not produced.
Each of the income components presented in Figure 4.7 and Figure 4.8 have been imputed for both respondents and non-respondents within responding households. The Enumerated File, as a result, contains component level data. This has also permitted the calculation of these components at the household-level, as detailed in Figure 4.6.
From Release 12, the income model was modified to include 'irregular' income components as part of total income. Previously, these components were excluded from total income.

[^0]
[^0]:    ${ }^{21}$ Wave 9 and 12 onwards.

However, total 'regular' income variables have been preserved which are constructed in the same way as total income in previous releases. Full details of the changes to the income model are provided in Wilkins (2014).
In order to produce the disposable income variable, an income tax model is applied to each sample member that calculates the financial-year tax typically payable for a permanent resident taxpayer in the circumstances akin to those of the respondent. The information collected in the HILDA Survey does not permit accounting for every individual variation in tax available under the Australian taxation system, but most major sources of variation are accounted for. When aggregated, income tax estimates from HILDA compare favourably with national aggregates produced by the Australian Taxation Office (ATO) (once tax on realised capital gains, which are not measured by the HILDA Survey, is excluded).
From Release 16 onwards, we make available to users the Stata program that we use to estimate taxes (and family benefits). This program is available in the program library on the HILDA website (also see Section 3.7).
Following is an outline of the method by which taxes are estimated:

1. The input data are the imputed income variables and the data collected in the Person Questionnaire. The components which the ATO treats as taxable income are summed: wages and salaries, business income, investment income, private pensions and taxable Australian public transfers. Special tax rates apply to superannuation benefits, which are therefore excluded from 'regular' taxable income. (Estimated tax on superannuation benefits is described at Step viii below.) Taxable public transfers are obtained by subtracting from public transfer income Family Tax Benefit Parts A and B, Single Income Family Supplement, Maternity Allowance, Maternity Payment, Disability Support Pension, Wife Pension, Carer Payment, Carer Allowance and estimated Rent Assistance, none of which are taxable. From wave 10, wage and salary earners have been asked to report salary sacrificed income, and to indicate whether they included it in their reported wage and salary income. For respondents who included the salary sacrificed income, it is subtracted from reported wage and salary income to obtain taxable wage and salary income. For respondents who did not include the salary sacrificed income, taxable wage and salary income is as reported (but gross wage and salary income, and hence gross income, are increased by the value of the salary sacrificed income). For waves prior to wave 10, all employees are assumed to receive 0.5 per cent of wage and salary income as salary sacrificed income - that is, 99.5 per cent of wage and salary income is included in taxable income. Note also that JobKeeper Payments in 2019-20 and 2020-21 are included as part of wage and salary income.
2. Tax deductions (for example, for work-related expenses) are assumed to be a fixed percentage of gross income that depends on the level of the individual's gross income. ATO data on deductions as a proportion of income for each of a number of income ranges (reported in Taxation Statistics, which has been produced for each financial year spanned by the HILDA Survey) are used to determine the applicable percentage. That is, the proportion of gross income that is assumed to be claimed as a tax deduction depends on the income category in which the individual falls. Estimated deductions are typically between 3 and 5 per cent of gross income. Estimated deductions are subtracted from the total income obtained at Step 1 above to obtain 'regular' taxable income excluding dividend imputation credits.
3. Dividend imputation credits, which are tax credits received by share-dividend recipients, are estimated, based on ATO Taxation Statistics, as equal to 41 per

cent of share-dividend income (_oifdiva). These are added to the income calculated at Step ii to obtain 'regular' taxable income including dividend imputation credits.
4. The standard marginal income tax rates are applied to the 'regular' taxable income estimate obtained at Step iii. This produces an initial estimated income tax liability.
5. The Medicare Levy is estimated as per the formulas applicable in the relevant financial year. Up to and including the 2013-2014 financial year, the levy was 1.5 per cent of taxable income if the individual has an income that exceeds the applicable threshold (which depends on the year, family situation, age and whether they are a pensioner or not). From the 2014-2015 financial year onward, it increased to 2.0 per cent. Prior to wave 12, the HILDA Survey did not collect private health insurance status (except in waves 4 and 9), so the Medicare Levy Surcharge (MLS) was assumed to be zero for all respondents. From wave 12, this information is obtained, allowing estimation of the MLS.
6. Applicable tax offsets are estimated. These comprise the Low-Income Tax Offset, Senior Australians Tax Offset, Pensioner Tax Offset, Beneficiary Tax Offset, Mature Age Workers Tax Offset (up until 2013-14) and Dependent Spouse Tax Offset (up until 2013-14), which are calculated as per the applicable formulas ${ }^{22}$. All other offsets are estimated based on ATO Taxation Statistics data on their mean value as a proportion of taxable income, averaging approximately 0.4 per cent to 0.5 per cent of taxable income up until 2009-10, and between 0.2 per cent and 0.3 percent of taxable income since 2011-12.
7. Total income tax is calculated as the sum of income tax (Step iv) and the Medicare Levy (Step v), less offsets (Step vi) and dividend imputation credits (Step iii).
8. Special taxation rates apply to superannuation benefits, depending on how the benefit is classified, the amount of the benefit and the age of the recipient. HILDA Survey estimates of tax on superannuation benefits assume benefits are lump sums with a 'taxed' status. Up until 2006-07, for those aged 60 years and over, no tax was payable on the first $\$ 100,696$ of 'taxed' lump sum benefits, and a tax rate of 15 per cent applied to benefits in excess of $\$ 100,696$. Since 2007-08, no tax has been payable on 'taxed' lump sum superannuation benefits for people aged 60 years and over. For those aged under 60, tax rates depend on the amount of the benefit and whether the recipient is below the 'preservation age' ( 55 until 2015-16, when it will begin increasing up to 60 by 2024-25).
9. Taxes on redundancy payments are estimated, and tax on total (regular plus irregular) income is calculated by adding taxes on redundancy payments to taxes calculated in Steps i to viii.

[^0]
[^0]:    ${ }^{22}$ The Senior Australians Tax Offset, Pensioner Tax Offset and Beneficiary Tax Offset have been combined into a single tax offset since 2012-2013.

Figure 4.6: Financial year income model (household-level)

    Part 1: Building Blocks of Income

    The process begins by aggregating base income sources into intermediate categories.

    A. Calculation of FY Regular Market Income (=_hifmkip - _hifmkin)
    This is the sum of the following components:

        FY wages and salary (_hiwsfei)

        FY business income (=_hibifip - _hibifin)

        FY investment income (=_hifinip - _hifinin)

        FY regular private pensions (_hifppi)

    B. Calculation of FY Australian Public Transfers (_hifapti)
    This is the sum of two sub-categories:

        Australian Government income support payments (_hifisi), which includes:

            Australian Government pensions (_hifpeni)

            Australian Government Parenting Payments (_hifpari)

            Australian Government allowances (_hifalli)

        Australian Government non-income support payments (_hifnisi), which includes:

            Estimated family payments (_hiffama)

            Estimated Australian Government Bonus payments (_hifboni)

            Other non-income support payments, incl. Mobility and Carer Allowances (_hifonii)

    Part 2: Aggregating to Gross Income

    The intermediate categories are combined to create gross income measures.

    C. Calculation of FY Regular Private Income (=_hifpiip - _hifpiin)
    This is the sum of:

        FY regular market income (from Part 1.A)

        FY regular private transfers (_hifpti)

    D. Calculation of FY Gross Regular Income (=_hifefp - _hifefn)
    This is the sum of:

        FY regular private income (from Part 2.C)

        FY Australian public transfers (from Part 1.B)

    E. Calculation of FY Gross Total Income (=_hifeftp - _hifeftn)
    This is the sum of:

        FY gross regular income (from Part 2.D)

        FY irregular income (_hifwii)

        Other domestic government benefits and Australian Government benefits NEI to classify (_hifobi)

        Other regular public (including scholarships) (_hifrpi)

        Foreign pensions (_hiffpi)

    Part 3: Calculating Disposable Income

    Taxes are subtracted from gross income measures to determine disposable income.

    F. Calculation of FY Disposable Regular Income (=_hifdip - _hifdin)

        Start with FY gross regular income (from Part 2.D).

        Subtract FY estimated taxes on regular income (=_hiftaxp - _hiftaxn).

        The result is FY disposable regular income.

    G. Calculation of FY Disposable Total Income (=_hifditp - _hifditn)

        Start with FY gross total income (from Part 2.E).

        Subtract FY estimated taxes on total income (=_hifbtp - _hifbtn).

        The result is FY disposable total income.

    Notes on Variables (from the diagram)

        Wave Identifier: Substitute the wave identifier (e.g., 'a', 'b', ...) for the underscore (_) in the variable names.

        Negative Values: Variable names like (=_p - _n) indicate that in the HILDA dataset, variables that can be negative are split into two: one for positive values (suffix 'p') and one for negative values (suffix 'n'). The final value is the difference between them.

Figure 4.7: Financial year income model (enumerated person-level)
    Part 1: Building Blocks of Income

    The process begins by aggregating base income sources into intermediate categories.

    A. Calculation of FY Investment Income (=_oifinp - _oifinn)
    This is the sum of:

        Interest (_oiinti)

        Rent (=_oirntip - _oirntin)

        Dividends and Royalties (_oidvryl)

    B. Calculation of FY Regular Private Pensions (_oifppi)
    This is the sum of:

        Regular superannuation (_oifsupi)

        Worker's comp / accident / sickness (_oifwkci)

    C. Calculation of FY Regular Market Income (=_tifmkip - _tifmkin)
    This is the sum of:

        FY wages and salary (_wsfes)

        FY business income (=_bifip - _bifin)

        FY investment income (from Part 1.A)

        FY regular private pensions (from Part 1.B)

    D. Calculation of FY Australian Public Transfers (_bnftapti)
    This is the sum of two sub-categories:

        Australian Government income support payments (_bnfisi), which includes:

            Australian Government pensions (_bnfpeni)

            Australian Government Parenting Payments (_bnfpari)

            Australian Government allowances (_bnfalli)

        Australian Government non-income support payments (_bnfnisi), which includes:

            Estimated family payments (_bnffama)

            Estimated Australian Government Bonus Payments (_bnfboni)

            Other non-income support payments, incl. Mobility and Carer Allowances (_bnfonii)

    E. Calculation of FY Irregular Income (_oifwii)
    This is the sum of:

        Redundancy / Severance (_oifrsvi)

        Irregular other than redundancy (_oifoin)

    Part 2: Aggregating to Gross Income

    The intermediate categories are combined to create gross income measures.

    F. Calculation of FY Regular Private Income (=_tifpiip - _tifpiin)
    This is the sum of:

        FY regular market income (from Part 1.C)

        FY regular private transfers (_oifpti)

    G. Calculation of FY Gross Regular Income (=_tifefp - _tifefn)
    This is the sum of:

        FY regular private income (from Part 2.F)

        FY Australian public transfers (from Part 1.D)

    H. Calculation of FY Gross Total Income (=_tifeftp - _tifeftn)
    This is the sum of:

        FY gross regular income (from Part 2.G)

        FY irregular income (from Part 1.E)

        Other domestic government benefits and Australian Government benefits NEI to classify (_bnfobi)

        Other regular public (including scholarships) (_bnfrpi)

        Foreign pensions (_bnffpi)

    Part 3: Calculating Disposable Income

    Taxes are subtracted from gross income measures to determine disposable income.

    I. Calculation of FY Disposable Regular Income (=_tifdip - _tifdin)

        Start with FY gross regular income (from Part 2.G).

        Subtract FY estimated taxes on regular income (=_txtotp - _txtotn).

        The result is FY disposable regular income.

    J. Calculation of FY Disposable Total Income (=_tifditp - _tifditn)

        Start with FY gross total income (from Part 2.H).

        Subtract FY estimated taxes on total income (=_txtottp - _txtottn).

        The result is FY disposable total income.

    Notes on Variables (from the diagram)

        Wave Identifier: Substitute the wave identifier (e.g., 'a', 'b', ...) for the underscore (_) in the variable names.

        Negative Values: Variable names like (=_p - _n) indicate that in the HILDA dataset, variables that can be negative are split into two: one for positive values (suffix 'p') and one for negative values (suffix 'n'). The final value is the difference between them.

Figure 4.8: Financial year income model (responding-level)
    Part 1: Building Blocks of Income

    The process begins by aggregating granular income sources into intermediate categories.

    A. Calculation of FY Regular Market Income (=_tifmkip - _tifmkin)
    This is the sum of the following four major components:

        FY wages and salary (_wsfes), which is derived from:

            Wages and salary (_wsfga, _wsfna)

        FY business income (=_bifip - _bifin), which is derived from:

            Incorporated business wages and salary (_bifiga)

            Unincorporated business income (_bifuga)

        FY investment income (=_oifinip - _oifinin), which is the sum of:

            Interest (_oiinti)

            Rent (=_oirntip - _oirntin)

            Dividends and Royalties (_oidvryi)

        FY private pensions (_oifppi), which is the sum of:

            Regular superannuation (_oifsupi)

            Worker's comp / accident / sickness (_oifwkci)

    B. Calculation of FY Private Transfers (_oifpti)
    This is the sum of:

        Child support (_oifchs)

        Regular transfers from non-resident parents (_oifnptr)

        Regular transfers from other non-household members (_oifohhr)

        Other regular private transfers (_oifpria)

    C. Calculation of FY Australian Public Transfers (_bnfapti)
    This is the sum of two sub-categories:

        Australian Government income support payments (_bnfisi), which includes:

            Australian Government pensions (_bnfpeni)

            Australian Government Parenting Payments (_bnfpari)

            Australian Government allowances (_bnfalli)

        Australian Government non-income support payments (_bnfnisi), which includes:

            Estimated family payments (_bnffama)

            Estimated Australian Government Bonus Payments (_bnfboni)

            Other non-income support payments, incl. Mobility and Carer Allowances (_bnfonii)

    D. Calculation of FY Irregular Income (_oifwfli)
    This is the sum of:

        Redundancy / Severance (_oifrsvi)

        Irregular other than redundancy (_oifoiri), which itself is the sum of:

            Inheritance / Bequests (_oifinha)

            Irregular transfers from non-resident parents (_oifnpt)

            Irregular transfers from non-household members (_oifohhl)

            Lump sum workers compensation (_oiflswa)

            Irregular superannuation income (_oifilsa)

            Other irregular payment (_oifirra)

    Part 2: Aggregating to Gross Income

    The intermediate categories are combined to create gross income measures.

    E. Calculation of FY Regular Private Income (=_tifpiip - _tifpiin)
    This is the sum of:

        FY regular market income (from Part 1.A)

        FY private transfers (from Part 1.B)

    F. Calculation of FY Gross Regular Income (=_tifefp - _tifefn)
    This is the sum of:

        FY regular private income (from Part 2.E)

        FY Australian public transfers (from Part 1.C)

    G. Calculation of FY Gross Total Income (=_tifeftp - _tifeftn)
    This is the sum of:

        FY gross regular income (from Part 2.F)

        FY irregular income (from Part 1.D)

        Other domestic government benefits and Australian Government benefits NEI to classify (_bnfobi)

        Other regular public (including scholarships) (_bnfrpi)

        Foreign pensions (_bnffpi)

    Part 3: Calculating Disposable Income

    Taxes are subtracted from gross income measures to determine disposable income.

    H. Calculation of FY Disposable Regular Income (=_tifdip - _tifdin)

        Start with FY gross regular income (from Part 2.F).

        Subtract FY estimated taxes on regular income (=_txtotp - _txtotn).

        The result is FY disposable regular income.

    I. Calculation of FY Disposable Total Income (=_tifditp - _tifditn)

        Start with FY gross total income (from Part 2.G).

        Subtract FY estimated taxes on total income (=_txtottp - _txtottn).

        The result is FY disposable total income.

    Notes on Variables (from the diagram)

        Wave Identifier: Substitute the wave identifier (e.g., 'a', 'b', ...) for the underscore (_) in the variable names.

        Negative Values: Variable names like (=_*p - _*n) indicate that in the HILDA dataset, variables that can be negative are split into two: one for positive values (suffix 'p') and one for negative values (suffix 'n').


        Wages and Salary Variable: _wsfes is only available from Wave 10 onwards. In Waves 1 to 9, the variable is _wsfei, which excludes some salary-sacrificed income.

        Irregular Superannuation: _oifilsa is only available from Wave 18 onwards.

        Exclusions: Reinvested lump sum superannuation payouts and payments received from resident parents do not appear in this income model.


Additional derived income variables are provided in Table 4.22 and Table 4.24, the latter containing variables directly related to the income imputation.
There are several issues to take note of in Table 4.22:

- Wages and salaries were asked of respondents for their main job, then for all their other jobs combined. The suffixes ' $g$ ' and ' $e$ ' refer to gross and estimated gross incomes - where the respondent didn't know their gross income, their aftertax income was asked for and this was translated back into an estimated gross income. The 'e' variables will have fewer cases with missing wages and salaries than the ' $g$ ' variables, as the ' $e$ ' variables include all the known ' $g$ ' values.
- The variable labels indicate when top-coding has occurred. The actual value replacing the top-coded value will be the weighted mean of the top-coded units (see Section 3.12 on Confidentialisation).
- Child support is calculated from the questions asked about the children in the family formation grid, rather than from the single category listed in the 'other income' question in the income section. This is because it is more likely the respondent would provide a more accurate response to the detailed questions rather than the broad 'catch all' question.
- The components of 'irregular' income include inheritances, redundancies, irregular payments from parents, lump sum workers compensation payouts and, since Wave 18, irregular lump sum superannuation income.
- Since Wave 18, respondents have been asked to separately report regular superannuation payouts (which are treated as part of regular income) and irregular lump sum superannuation payouts. For irregular lump sum payouts, respondents have also been asked what they did with the payouts. Lump sum superannuation that is not reinvested is treated as regular income if less than the annualised average weekly earnings of full-time employees and as irregular income otherwise. Reinvested superannuation is treated as not income. Prior to Wave 18, superannuation payouts larger than annualised average weekly earnings of full-time employees were deemed to not be income unless similar payouts were observed over surrounding years. All superannuation payouts less than annualised average weekly earnings of full-time employees were deemed to be part of regular income-that is, no superannuation payouts could be classified as part of irregular income prior to Wave 18.
- In wave 1, respondents were asked how different their current wage and salary income was from one year ago. This has been provided in dollar terms in awsly.
The imputation method and derived variables are discussed in the following sections.

Table 4.22: Other derived income variables

| Variable | Description |
| :--: | :--: |
| Current wages and salaries and current benefits - person-level |  |
| _wscg, _wscmg, _wscog | Current gross wages and salary per week (\$), weighted top-code ${ }^{1,2}$ <br> - All jobs <br> - Main job <br> - Other jobs |
| _bncis, _bncisi, _bncisf, | Current weekly Australian Government income support payments (pre-imputed, post-imputed, flag) |
| _bncapu, _bncapui, <br> _bncapuf | Current weekly public transfers excluding family benefits (pre-imputed, postimputed, flag) |
| awsly | Gross weekly current wages and salary (from all jobs) one year ago (\$) |

# Financial year income - unimputed variables - person-level 

| _wsfg, | - gross wages and salary, weighted top-code ${ }^{1,2}$ |
| :-- | :-- |
| _oidiv, | - dividends |
| _oiroy, | - royalties |
| _tifmktp, _tifmktn, | - market income (positive and negative values, weighted top-code ${ }^{1}$ ) |
| _tifprip, _tifprin | - private income (positive and negative values, weighted top-code ${ }^{1}$ ) |

## Current wages and salaries and current benefits - household-level

| _hicisi, _hicisf, | Current weekly Australian Government income support payments (post- |
| :-- | :-- |
| _hicnisi, _hicnisf, | imputed, flag), |
| _hicapi, _hicapf | Current weekly Australian Government non-income support payments (post- |
|  | imputed, flag), Current weekly public transfers (post-imputed, flag) |

## Financial year income - estimated Family and Medicare related items - person-level

| _bnfftba | Family Tax Benefit Part A (\$) financial year |
| :--: | :--: |
| _bnfftbb | Family Tax Benefit Part B (\$) financial year |
| _bnfsifs ${ }^{3}$ | Single Income Family Supplement (\$) financial year |
| _bnfmat ${ }^{4}$ | Maternity Payments (\$) financial year |
| _phlfyi ${ }^{5}$, _phlfy ${ }^{5}$ | Covered by private patient hospital (insurance) cover for the whole of last year (post-imputed, flag) |

## Financial year income - estimated Family and Medicare related items - household-level

| _bnftaf1, _bnftaf2, | Family Tax Benefit Part A (\$) for financial year for family number 1, 2 and 3 |
| :--: | :--: |
| _bnftaf3 |  |
| _bnftbf1, _bnftbf2, | Family Tax Benefit Part B (\$) for financial year for family number 1, 2 and 3 |
| _bnftbf3 |  |
| _hifftb | Household Family Tax Benefit (FTB-A and FTB-B) (\$) financial year |
| _bnsiff13, _bnsiff23, | Single Income Family Supplement (\$) financial year for family number 1, 2 and |
| _bnsiff3 ${ }^{3}$ | 3 |
| _hifsifs ${ }^{3}$ | Household Single Income Family Supplement (\$) financial year |
| _bnmatf14, _bnmatf24, | Maternity Payments (\$) for financial year for family number 1, 2 and 3 |
| _bnmatf3 ${ }^{4}$ |  |
| _hifmat ${ }^{4}$ | Household Maternity Payments [Baby Bonus] (\$) financial year |
| _hiffama | Household Australian Government family payments (\$) for financial year |

| Variable | Description |
| :--: | :--: |
| Financial year- taxes |  |
| _txdic | Estimated dividend imputation credits ($) |
| _txtotp, _txtotn | Estimated taxes on regular income ($) (positive and negative values) |
| _txtottp, _txtottn | Estimated taxes on total income ($) (positive and negative values) |
| Salary sacrifice and non-cash benefit - current and financial year - person-level |  |
| _sscmrei6, _sscmref6 | Salary sacrifice reported earlier - current main job [imputed] (post-imputed, flag) |
| _sscorei6, _sscoref6 | Salary sacrifice reported earlier - current other jobs [imputed] (post-imputed, <br> flag) |
| _ssfarei6, _ssfaref6 | Salary sacrifice reported earlier - financial year [imputed] (post-imputed, flag) |
| _ssfbrei7, _ssfbref7 | Salary sacrifice reported earlier - financial year incorporated businesses <br> [imputed] (post-imputed, flag) |
| _wscmes ${ }^{6}$, _wscmesf ${ }^{6}$ | Current weekly gross wages \& salary - main job ($) [imputed][inc. salary <br> sacrifice] |
| _wscoes ${ }^{6}$, _wscoesf ${ }^{6}$ | Current weekly gross wages \& salary - other jobs ($) [imputed][inc. salary <br> sacrifice] |
| _wsces ${ }^{6}$, _wscsf ${ }^{6}$ | Current weekly gross wages \& salary - all jobs ($) [imputed][inc. salary sacrifice] |
| _wsfes ${ }^{6}$, _wsfesf ${ }^{6}$ | Financial year gross wages \& salary ($) [imputed][inc. salary sacrifice] |
| Salary sacrifice and non-cash benefit - current and financial year - household-level ${ }^{6}$ |  |
| _hiwscms ${ }^{6}$, _hiwcmsf ${ }^{6}$ | Household current weekly gross wages and salary including salary sacrifice - <br> main job (post-imputed, flag) |
| _hiwscos ${ }^{6}$, _hiwcosf ${ }^{6}$ | Household current weekly gross wages and salary including salary sacrifice - <br> other jobs (post-imputed, flag) |
| _hifnb ${ }^{6}$, _hifnbf ${ }^{6}$ | Household financial year non-cash benefits (post-imputed, flag) |
| _hiwsces ${ }^{6}$, _hiwscsf ${ }^{6}$ | Household current weekly gross wages and salary - all jobs ($) [imputed][inc <br> salary sacrifice] |
| Australian Government Bonus Payments |  |
| ibnfbtsa | 2009 Back to School Bonus Part A if parent ($) [estimated] |
| ibnfbtsb | 2009 Back to School Bonus Part B if child on Disability Support Pension or <br> Carer Payment ($) [estimated] |
| ibnfeep | 2009 Temporary supplement to the Education Entry Payment ($) [estimated] |
| ibnffam | 2008 Bonus payment for families ($) [estimated] |
| ibnffh | 2009 Farmers Hardship Bonus ($) [estimated] |
| ibnfpens | 2008 Bonus payment for pensioners, seniors, people with disability, carers and <br> veterans ($) [estimated] |
| ibnfsif | 2009 Single Income Family Bonus ($) [estimated] |
| ibnftal | 2009 Training and Learning Bonus ($) [estimated] |
| ibnftb | 2009 Tax bonus for Working Australians ($) [estimated] |

| Variable | Description |
| :--: | :--: |
| lbnfceap | 2012 Bonus payment - Clean Energy Advance Payments (\$) [estimated] |
| _bnfskb ${ }^{5}$ | Bonus payment - School Kids Bonus (\$) [estimated] |
| _bnfbon, _bnfboni, <br> _bnfbonf | Australian government bonus payments - Total bonuses (\$) [estimated]) preimputed, post-imputed, flag) ${ }^{8}$ |
| _bnfespa ${ }^{9}$ | Bonus payment - Economic Support Payment (\$) [estimated] |
| Superannuation - financial year - person-level ${ }^{10}$ |  |
| _oifilsa | Financial year irregular lump sum superannuation income (\$) |
| _oiflsa | Financial year lump sum superannuation income (\$) |
| _oiflssa | Lump sum superannuation (non-income) (\$) |
| _oifrlsa | Financial year regular lump sum superannuation income (\$) |
| _oifsup | Financial year regular superannuation/annuity payments - received |
| _oifsupa | Financial year regular superannuation/annuity payments (\$) |

${ }^{1}$ See Section 3.12 on Confidentialisation for a description of the top-coding process.
${ }^{2}$ These variables are as calculated from reported wage and salary income and may include salary sacrifice income.
${ }^{3}$ Wave 14 onwards.
${ }^{4}$ Waves 1-15 only.
${ }^{5}$ Wave 12 onwards.
${ }^{6}$ Wave 10 onwards.
${ }^{7}$ Wave 17 onwards.
${ }^{8}$ Wave 20 and 21 only.
${ }^{9}$ Wave 18 only.
${ }^{10}$ Wave 18 only.

# 4.25.2. Imputation Method 

The following imputation methods are used in the HILDA Survey, each to varying extents:

- The Nearest Neighbour Regression method;
- The Little and Su method;
- The Population Carryover method; and
- The Hotdeck method.

The particular combination of methods adopted for the imputation of income data resulted from a detailed study undertaken by Watson and Starick (2011) and employs the first three of these four methods.
The imputation steps for each income variable are as follows:

- Step 1 - Carryover of zeros. For non-responding persons (in responding households), the income amounts are estimated to be zero or non-zero by carrying forward or backward this information from the surrounding waves (where it is available) with the same probability as that observed for complete cases.
- Step 2 - Nearest Neighbour Regression imputation. The predicted values from a regression model are used to identify a donor from which the reported value is taken as the imputed value for the recipient. For non-respondents, a single donor for all income components is used and the zero or non-zero determination from step 1 is observed.

- Step 3 - Little and Su imputation. This method incorporates, via a multiplicative model, the trend across waves (column effect), the recipient's departure from the trend (row effect), and a residual effect donated from another respondent with complete income information for that component (residual effect). Wherever possible, the Little and Su imputation replaces the Nearest Neighbour Regression imputation. The zero or non-zero determination from step 1 is observed.
Imputation classes are used for some variables to ensure the donors and recipients match on a small number of characteristics. ${ }^{23}$ For example, age categories are used in the imputation of some of the income variables to improve the similarity of donors and recipients, hence improving the accuracy of the imputation.
Once each income component has been imputed (where required), total income is then constructed as the sum of the imputed components.
A full description of the imputation process for the income variables is provided by Hayes and Watson (2009). Appendix 2 provides an extract from this paper which details the Population Carryover method, the Nearest Neighbour Regression method and the Little and Su method.
Table 4.23 shows the percentage of missing cases that were imputed by each imputation method (for the proportion of cases which are missing, see Table 6.2). The percentages are summarized across all income variables that have been imputed. Ideally all records would be imputed by the Little and Su method, however sufficient information is not always available (particularly for non-respondents within responding households).
With additional waves of income data and improvements to the imputation methodology, the imputed values will change from release to release.

[^0]
[^0]:    ${ }^{23}$ From Release 11, we added a restriction for non-respondents that donors match the full-time, part-time, or not employed status of the recipients in the Nearest Neighbour Regression method and that the Little and Su imputed amounts match the zero/non-zero pattern imputed by the Nearest Neighbour Regression method. From Release 12, the Little and Su imputes were restricted to fall within the observed ranges of reported values.

Table 4.23: Percentage of missing cases imputed by imputation method (income), waves 1 - 23

|  Imputation method | Wave |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $11^{*}$ | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23  |
|  Responding Persons |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest
Neighbour | 11.7 | 3.8 | 3.7 | 3.7 | 4.0 | 4.1 | 3.7 | 3.4 | 3.8 | 4.1 | 4.9 | 2.7 | 3.3 | 3.5 | 3.7 | 3.3 | 2.9 | 2.8 | 2.9 | 2.1 | 2.8 | 2.4 | 7.2  |
|  Little \& Su | 88.3 | 96.2 | 96.3 | 96.3 | 96.0 | 95.9 | 96.3 | 96.6 | 96.2 | 95.9 | 95.1 | 97.3 | 96.7 | 96.5 | 96.3 | 96.7 | 97.1 | 97.2 | 97.1 | 97.9 | 97.2 | 97.6 | 92.8  |
|  Enumerated Persons |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest
Neighbour | 61.1 | 44.2 | 47.4 | 45.2 | 47.2 | 49.2 | 48.6 | 42.2 | 46.4 | 44.7 | 51.2 | 47.5 | 48.9 | 51.2 | 50.9 | 51.1 | 50.4 | 50.2 | 52.3 | 51.0 | 53.3 | 52.7 | 63.2  |
|  Little \& Su | 23.8 | 26.7 | 28.4 | 26.2 | 30.9 | 32.0 | 32.6 | 32.5 | 36.0 | 35.4 | 33.2 | 33.9 | 33.4 | 35.8 | 33.9 | 34.4 | 34.3 | 34.1 | 35.2 | 33.3 | 30.3 | 29.5 | 27.8  |
|  Carryover | 15.1 | 29.0 | 24.2 | 28.6 | 21.8 | 18.8 | 18.8 | 25.3 | 17.6 | 19.8 | 15.6 | 18.6 | 17.7 | 13.0 | 15.2 | 14.5 | 15.2 | 15.7 | 12.4 | 15.7 | 16.5 | 17.8 | 9.0  |

- A Top-Up sample was added in wave 11 and 23.

In wave 9, certain stimulus payments were imputed (via the Nearest Neighbour Regression method) for those whom receipt of such payments could not be determined from their financial and family situation. This imputation occurred for:

- the bonus payment for training and learning, the temporary supplement to the Education Entry Payment, and the farmers hardship bonus (both for respondents and for non-respondents in responding households); and
- the bonus payment for pensioners, seniors, people with disabilities, carers and veterans (for non-respondents in responding households).
Salary sacrifice and non-cash benefit variables (from questions introduced in wave 10) were also imputed. Two methods were used. The Little and Su method or (failing that) the Nearest Neighbour Regression was used to impute the amount of salary sacrificed or the amount of non-cash benefits. The Nearest Neighbour Regression method (using logistic regression) was then used to impute whether someone included these amounts in their reporting of wages and salaries. This imputation was undertaken for a person's main job held currently, other jobs held currently, and together for all jobs held in the last financial year.
From wave 12, an indicator variable for whether the person was covered by private health insurance was also imputed via the Nearest Neighbour method (as this is required for the tax model).


# 4.25.3. Imputed Income Variables 

All income imputation was undertaken at the derived variable level, leaving the original data unchanged. Generally, both the pre-imputed and post-imputed variables are available in the datasets, along with an imputation flag, so that it is easy to switch between using the preimputed data or the post-imputed data.
An overview of the pre- and post-imputed income variables is provided in Table 4.24.
Table 4.24: Imputed income variables

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Responding person file |  |  |  |
| Current income |  |  |  |
| Wages and salaries - all jobs | _wsce | _wscei | _wscef |
| Wages and salaries - main job | _wscme | _wscmei | _wscmef |
| Wages and salaries - other jobs | _wscoe | _wscoei | _wscoef |
| Salary sacrifice - main job ${ }^{1}$ | _sscm | _sscmi | _sscmf |
| Salary sacrifice - other jobs ${ }^{1}$ | _ssco | _sscoi | _sscof |
| Non-cash benefits - main job ${ }^{1}$ | _nbcm | _nbcmi | _nbcmf |
| Non-cash benefits - other jobs ${ }^{1}$ | _nbco | _nbcoi | _nbcof |
| Australian Government pensions | _bncpen | _bncpeni | _bncpenf |
| Australian Government parenting payment | _bncpar | _bncpari | _bncparf |

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Australian Government allowances | _bncall | _bncalli | _bncallf |
| Non-income support other than family payments | _bnconi | _bnconii | _bnconif |
| Other Australian Government benefits, not enough information (NEI) to classify | _bncob | _bncobi | _bncobf |
| Financial year income |  |  |  |
| Wages and salaries | _wsfe | _wsfei | _wsfef |
| Salary sacrifice - employment ${ }^{1}$ | _ssfa | _ssfai | _ssfaf |
| Salary sacrifice - incorporated businesses ${ }^{2}$ | _ssfb | _ssfbi | _ssfbf |
| Non-cash benefits - employment ${ }^{1}$ | _nbfa | _nbfai | _nbfaf |
| Non-cash benefits - incorporated businesses ${ }^{2}$ | _nbfb | _nbfbi | _nbfbf |
| Australian Government pensions | _bnfpen | _bnfpeni | _bnfpenf |
| Australian Government parenting payment | _bnfpar | _bnfpari | _bnfparf |
| Australian Government allowances | _bnfall | _bnfalli | _bnfallf |
| Australian Government Bonus payments | _bnfbon | _bnfboni | _bnfbonf |
| Australian Government income support payments | _bnfis | _bnfisi | _bnfisf |
| Australian Government non-income support payments | _bnfnis | _bnfnisi | _bnfnisf |
| Australian public transfers | - | _bnfapti | _bnfaptf |
| Non-income support other than family payments | _bnfoni | _bnfonii | _bnfonif |
| Other regular public payments | _bnfrp | _bnfrpi | _bnfrpf |
| Other Australian Government benefits, not enough information (NEI) to classify | _bnfob | _bnfobi | _bnfobf |
| Foreign government pensions | _bnffp | _bnffpi | _bnffpf |
| Business income | _bifp, _bifn | _bifip, _bifin | _biff |
| Investments | _oifinvp, _oifinvn | _oifinip, _oifinin | _oifinf |
| Dividends and royalties | _oidvry | _oidvryi | _oidvryf |
| Interest | _oiint | _oiinti | _oiintf |
| Rental income | _oirntp, _oirntn | _oirntip, _oirntin | _oirntf |
| Regular private pensions | _oifpp | _oifppi | _oifppf |
| Regular superannuation/annuity payments ${ }^{3}$ | _oifsupa | _oifsupi | _oifsupf |

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Regular workers compensation insurance ${ }^{3}$ | _oifwkca | _oifwkci | _oifwkcf |
| Regular private transfers | _oifpt | _oifpti | _oifptf |
| Gross regular income | - | _tifefp, _tifefn | _tifeff |
| Gross total income | - | _tifeftp, _tifeftn | _tifeftf |
| Income prior to family benefits |  | _tifeip, _tifein | _tifeif |
| Redundancy and severance payments ${ }^{3}$ | _oifrsva | _oifrsvi | _oifrsvf |
| Irregular income other than redundancy | _oifoira | _oifoiri | _oifoirf |
| Regular market income | - | _tifmkip, _tifmkin | _tifmktf |
| Regular private income | - | _tifpiip, _tifpiin | _tifpif |
| Disposable regular income | - | _tifdip, _tifdin | _tifdif |
| Disposable total income | - | _tifditp, _tifditn | _tifditf |
| Irregular income | _oifwfl | _oifwfli | _oifwflf |
| Enumerated person file |  |  |  |
| Current income |  |  |  |
| Wages and salaries - all jobs | - | _wscei | _wscef |
| Wages and salaries - main job | - | _wscmei | _wscmef |
| Wages and salaries - other jobs | - | _wscoei | _wscoef |
| Salary sacrifice - main job ${ }^{1}$ | - | _sscmi | _sscmf |
| Salary sacrifice - other jobs ${ }^{1}$ | - | _sscoi | _sscof |
| Non-cash benefits - main job ${ }^{1}$ | - | _nbcmi | _nbcmf |
| Non-cash benefits - other jobs ${ }^{1}$ | - | _nbcoi | _nbcof |
| Australian Government pensions | - | _bncpeni | _bncpenf |
| Australian Government parenting payment | - | _bncpari | _bncparf |
| Australian Government allowances | - | _bncalli | _bncallf |
| Non-income support other than family payments | - | _bnconii | _bnconif |
| Other Australian Government benefits, not enough information (NEI) to classify | - | _bncobi | _bncobf |

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Financial year income |  |  |  |
| Wages and salaries | - | _wsfei | _wsfef |
| Salary sacrifice - employment ${ }^{1}$ | - | _ssfai | _ssfaf |
| Salary sacrifice - incorporated businesses ${ }^{2}$ | - | _ssfbi | _ssfbf |
| Non-cash benefits - employment ${ }^{1}$ | - | _nbfai | _nbfaf |
| Non-cash benefits - incorporated businesses ${ }^{2}$ | - | _nbfbi | _nbfbf |
| Australian Government pensions | - | _bnfpeni | _bnfpenf |
| Australian Government parenting payment | - | _bnfpari | _bnfparf |
| Australian Government allowances | - | _bnfalli | _bnfallf |
| Australian Government Bonus payments | - | _bnfboni | _bnfbonf |
| Australian Government income support payments | - | _bnfisi | _bnfisf |
| Australian Government non-income support payments | - | _bnfnisi | _bnfnisf |
| Australian public transfers | - | _bnfapti | _bnfaptf |
| Non-income support other than family payments | - | _bnfonii | _bnfonif |
| Other regular public payments | - | _bnfrpi | _bnfrpf |
| Other Australian Government benefits, not enough information (NEI) to classify | - | _bnfobi | _bnfobf |
| Foreign government pensions | - | _bnffpi | _bnffpf |
| Business income | - | _bifip, _bifin | _biff |
| Investments | - | _oifinip, _oifinin | _oifinf |
| Dividends and royalties | _oidvry | _oidvryi | _oidvryf |
| Interest | _oiint | _oiinti | _oiintf |
| Rental income | _oirntp, _oirntn | _oirntip, _oirntin | _oirntf |
| Regular private pensions | - | _oifppi | _oifppf |
| Regular superannuation/annuity payments | - | _oifsupi | _oifsupf |
| Regular workers compensation insurance | - | _oifwkci | _oifwkcf |
| Regular private transfers | - | _oifpti | _oifptf |
| Gross regular income ${ }^{3}$ | - | _tifefp, _tifefn | _tifeff |
| Gross total income | - | _tifeftp, _tifeftn | _tifeftf |

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Income prior to family benefits | tifep, _tifen | _tifeip, _tifein | _tifeif |
| Redundancy and severance payments | - | _oifrsvi | _oifrsvf |
| Irregular income other than redundancy | - | _oifoiri | _oifoirf |
| Regular market income | - | _tifmkip, _tifmkin | _tifmktf |
| Regular private income | - | _tifpiip, _tifpiin | _tifpif |
| Disposable regular income | - | _tifdip, _tifdin | _tifdif |
| Disposable total income | - | _tifditp, _tifditn | _tifditf |
| Irregular income | - | _oifwfli | _oifwflf |
| Household File |  |  |  |
| Current income |  |  |  |
| Wages and salaries - all jobs | - | _hiwscei | _hiwscef |
| Wages and salaries - main job | - | _hiwscmi | _hiwscmf |
| Wages and salaries - other jobs | - | _hiwscoi | _hiwscof |
| Australian Government pensions | - | _hicpeni | _hicpenf |
| Australian Government parenting payment | - | _hicpari | _hicparf |
| Australian Government allowances | - | _hicalli | _hicallf |
| Non-income support other than family payments | - | _hiconii | _hiconif |
| Other Australian Government benefits, not enough information (NEI) to classify | - | _hicobi | _hicobf |
| Financial year income |  |  |  |
| Wages and salaries | - | _hiwsfei | _hiwsfef |
| Australian Government pensions | - | _hifpeni | _hifpenf |
| Australian Government parenting payment | - | _hifpari | _hifparf |
| Australian Government allowances | - | _hifalli | _hifallf |
| Australian Government Bonus payments | - | _hifboni | _hifbonf |
| Australian Government income support payments | - | _hifisi | _hifisf |
| Australian Government non-income support payments | - | _hifnisi | _hifnisf |
| Australian public transfers | - | _hifapti | _hifaptf |
| Non-income support other than family payments | - | _hifonii | _hifonif |
| Other regular public payments | - | _hifrpi | _hifrpf |

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Other Australian Government benefits, not enough information (NEI) to classify | - | _hifobi | _hifobf |
| Foreign government pensions | - | _hiffpi | _hiffpf |
| Business income | - | _hibifip, _hibifin | _hibiff |
| Investments | - | _hifinip, _hifinin | _hifinf |
| Regular private pensions | - | _hifppi | _hifppf |
| Regular private transfers | - | _hifpti | _hifptf |
| Gross regular income | - | _hifefp, _hifefn | _hifeff |
| Gross total income | - | _hifeftp, _hifeftn | _hifeftf |
| Regular market income | - | _hifmkip, _hifmkin | _hifmktf |
| Disposable regular income | - | _hifdip, _hifdin | _hifdif |
| Disposable total income | - | _hifditp, _hifditn | _hifditf |
| Regular private income | - | _hifpiip, _hifpiin | _hifpif |
| Irregular income | - | _hifwfli | _hifwflf |

${ }^{1}$ From wave 10 onwards.
${ }^{2}$ From wave 17 onwards.
${ }^{3}$ The financial year variables for superannuation/annuity payments, workers compensation and redundancy and severance payments (_oifsupa, _oifwkca and _oifrsva respectively) are not derived variables, and hence take the value -1 for individuals who were not asked these questions.

# 4.26. Wealth 

### 4.26.1. Wealth Model

A wealth module has been incorporated into the questionnaires every fourth wave since wave 2. The Household Questionnaire contains most of the wealth questions and we endeavour to ask these of the person knowing the most about the household finances. These questions cover the following topics:

- Cash and equity investments, trust funds, life insurance;
- Home and other property assets and debts;
- Business assets and debts;
- Children's bank accounts; ${ }^{24}$
- Collectables and vehicles, and
- Overdue household bills (from wave 6 only); ${ }^{25}$
- Outstanding loans made to others. ${ }^{26}$

[^0]
[^0]:    ${ }^{24}$ That is, bank accounts of people in the household aged under 15.
    ${ }^{25}$ Overdue household bills were not obtained in wave 2. It was assumed that this was captured in the 'any other debt' question asked in wave 2 (though perhaps not well).
    ${ }^{26}$ Included from wave 22.

Also, each respondent was asked some questions about their personal wealth in the Person Questionnaire, including:

- Bank accounts and credit card debt;
- Superannuation;
- HECS debt; and
- Other personal debts. ${ }^{27}$

Figure 4.9 shows how the wealth components are combined to form the total household wealth. The boxes with the broken lines highlight the variables that come from the Person Questionnaire. From Release 6, the imputation for non-respondents has been conducted at the wealth component level, so the household-level components are the sum of all persons in the household. ${ }^{28}$

[^0]
[^0]:    ${ }^{27}$ In wave 2, other personal debts were asked as a single aggregate item; from wave 6 onwards other personal debts were obtained at a more disaggregated level and overdue personal bills were also explicitly asked for.
    ${ }^{28}$ For Release 2 to 5, please note that the imputation for non-respondents was only conducted at the total assets and debts level. As a result, the household-level components that summed these person-level components were just the sum of responding persons only. This will explain some of the differences observed for these variables between releases.

Figure 4.9: Wealth model (household-level)
    Part 1: Calculation of Total Assets (_hwassei, flag_hwassef)

    Total assets are the sum of Financial Assets and Non-financial Assets.

    A. Calculation of Financial Assets (_hwfini, flag_hwfinf)
    This is the sum of the following components:

        Bank accounts (_hwtbani, flag_hwtbanf), which includes:

            Joint bank accounts (_hwjbani, flag_hwjbanf)

            Own bank accounts (_hwobani, flag_hwobanf)

            Children's bank accounts (_hwcbani, flag_hwcbanf)

        Superannuation (_hwsupei, flag_hwsupef), which includes:

            Superannuation - retirees (_hwsupri, flag_hwsuprf)

            Superannuation - non retirees (_hwsupwi, flag_hwsupwf)

        Cash investments (_hwcaini, flag_hwcainf)

        Equity investments (_hweqini, flag_hweqinf)

        Trust funds (_hwtrusi, flag_hwtrusf)

        Life insurance (_hwinsui, flag_hwinsuf)

        Outstanding loans made to others (_hwlnoti, flag_hwlnotf)

    B. Calculation of Non-financial Assets (_hwnfii, flag_hwnfif)
    This is the sum of the following components:

        Property assets (_hwtpvi, flag_hwtpvf), which includes:

            Home asset (_hwhmvai, flag_hwhmvaf)

            Other property assets (_hwopvai, flag_hwopvaf)

        Business assets (_hwbusvi, flag_hwbusvf)

        Collectibles (_hwcolli, flag_hwcollf)

        Vehicles (_hwvechi, flag_hwvechf)

    Part 2: Calculation of Total Debts (_hwdebti, flag_hwdebtf)

    Total debts are the sum of all listed debt components.

    A. Components of Total Debts

        Credit card debt (_hwccdti, flag_hwccdtf), which includes:

            Joint credit cards (_hwjccdi, flag_hwjccdf)

            Own credit cards (_hwoccdi, flag_hwoccdf)

        Property debt (_hwtpdi, flag_hwtpdf), which includes:

            Home debt (_hwhmdti, flag_hwhmdtf)

            Other property debt (_hwopdti, flag_hwopdtf)

        HECS debt (_hwhecdi, flag_hwhecdf)

        Other personal debt* (_hwothdi, flag_hwothdf)

        Business debt (_hwbusdi, flag_hwbusdf)

        Overdue HH bills* (_hwobdti, flag_hwobdtf)

    Part 3: Calculation of Net Worth (=_hwnwip - _hwnwin, flag_hwnwf)

    Net worth is calculated by subtracting total debts from total assets.

        Start with Total assets (from Part 1).

        Subtract Total debts (from Part 2).

        The result is Net worth.

    Notes on Variables (from the diagram)

        Only the names of the imputed variables and their flags are provided.

        Variables in solid boxes are derived from the Household Questionnaire. Variables in broken line boxes are household-level variables derived by summing the equivalent components for adults in the household.

        Item non-response in the Household Questionnaire has been imputed by linking household longitudinally where possible.

        Item non-response for respondents, together with unit non-response for non-respondents in households where there was at least one respondent, has been imputed at the component level.

        (=_*p - _*n): In HILDA, variables that can legitimately be negative are supplied as two separate variables: one for positive values (suffix 'p') and one for negative values (suffix 'n'). The final value is the difference between them.

        Net equity variables (not shown) have been calculated for business, home, other property, and total property.

Several equity variables (assets less debts) not described in the previous figure are provided on the Household File. These are business equity, home equity, other property equity, and total property equity. These variables, together with the unimputed versions of the sub-totals described in Figure 4.9 are provided in Table 4.25 (variables relating directly to the wealth imputation are provided later in Table 4.28).

Table 4.25: Other derived wealth variables at household-level

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Business equity (weighted top-code) | _hwbusep, <br> _hwbusen | _hwbeip, <br> _hwbein | _hwbef |
| Home equity (weighted top-code) | _hwhmeqp, <br> _hwhmeqn | _hwhmeip, <br> _hwhmein | _hwhmef |
| Other property equity (weighted top-code) | _hwopeqp, <br> _hwopeqn | _hwopeip, <br> _hwopein | _hwopef |
| Total property equity (weighted top-code) | _hwtpeqp, <br> _hwtpeqn | _hwtpeip, <br> _hwtpein | _hwtpef |
| Total property value (weighted top-code) | _hwtpval |  |  |
| Home loans: <br> - from financial institution <br> - from other source (friend, relative etc.) <br> - secured against property | _hwhmhl, <br> _hwhmol, <br> _hwhmeql |  |  |
| Total property debt (weighted top-code) | _hwtpdt |  |  |
| Total credit card debt | _hwccdt |  |  |
| Retiree's superannuation | _hwsuprt |  |  |
| Total superannuation (weighted top-code) | _hwsuper |  |  |
| Total bank accounts (weighted top-code) | _hwtbank |  |  |
| Household financial assets (weighted top-code) | _hwfin |  |  |
| Household non-financial assets (weighted top-code) | _hwnfin |  |  |

# 4.26.2. Wealth Imputation Method 

The imputation method adopted for the wealth data takes advantage of five observation points (collected every four waves from wave 2). A summary of the steps in the imputation process is provided below:

- Step 1 - Create a longitudinal household identifier. For variables imputed at the household-level, households are linked longitudinally if they had common membership and any additional household members were children (defined for this purpose to be under 18 years of age) and any missing household members were children or deceased. ${ }^{29}$
- Step 2 - Nearest Neighbour Regression imputation of zeros. The predicted values from a regression model are used to identify a donor from which to flag zero or non-zero imputes for the recipient. This is essentially a filter process to decide whether the case has the asset or debt.

[^0]
[^0]:    ${ }^{29}$ _hwlink is an indicator variable for whether the household could be linked to a household four waves later.

- Step 3 - Nearest Neighbour Regression imputation of non-zero amounts. The predicted values from a regression model are used to identify a donor from which the reported value is taken as the imputed value for the recipient. The models and donor pools are restricted to cases with non-zero amounts.
- Step 4 - Little and Su imputation. This method incorporates (via a multiplicative model) the trend across waves (column effect), the recipient's departure from the trend (row effect), and a residual effect donated from another case with complete wealth information for that component (residual effect). Wherever possible, the Little and Su imputation replaces the Nearest Neighbour Regression imputation. The zero or non-zero determination from step 2 is observed.
Imputation classes were used for some variables to ensure the donors and recipients match on a small number of characteristics (typically wealth bands and filter variables).
Note that the household-level wealth variables for house value (_hsvalue) and house debt (_hsdebt) were collected in all waves and have been imputed via the same approach outlined above. _hhlink is an indicator variable showing whether a household was linked to another household in the next wave for the purposes of imputing house value and debt. ${ }^{30}$
A detailed description of the imputation process for wealth variables is provided by Hayes and Watson (2009). Appendix 2 provides an extract from this paper which details the Nearest Neighbour Regression method and Little and Su method.
Table 4.26 and Table 4.27 show the percentage of missing cases that were imputed by each imputation method. ${ }^{31}$ In the first table the percentages are summarized across all wealth variables that have been imputed. As with income it is preferable to have all records imputed by the Little and Su method but, with a limited number of waves of wealth data, sufficient information was not always available. Non-respondents in the enumerated person group were less likely to be imputed by the Little and Su method (for similar reasons as in income imputation) and any households not linked between waves were imputed via the Nearest Neighbour Regression method. In wave 11 and 23, a Top-Up sample was included.
Table 4.28 shows a higher percentage of records imputed via the Little and Su method for house value and debt due to better household linking between consecutive waves (rather than across the five waves used in the imputation of other wealth variables).

[^0]
[^0]:    ${ }^{30}$ From Release 18, households are no longer linked to the next wave if they moved for the purposes of house value and house debt.
    ${ }^{31}$ For the proportion of cases which are missing, see Table 6.4 and Table 6.5

Table 4.26: Percentage of missing cases imputed by imputation method (wealth), waves 2, 6, 10, 14, 18, and 22

|  Imputation Method | Wave 2 | Wave 6 | Wave 10 | Wave 14* | Wave 18 | Wave 22  |
| --- | --- | --- | --- | --- | --- | --- |
|  Person-level wealth items (responding persons) |  |  |  |  |  |   |
|  Nearest Neighbour | 33.0 | 30.2 | 27.8 | 31.7 | 26.1 | 30.0  |
|  Little \& Su | 67.0 | 69.8 | 72.2 | 68.3 | 73.9 | 70.0  |
|  Person-level wealth items (enumerated persons) |  |  |  |  |  |   |
|  Nearest Neighbour | 65.5 | 52.4 | 47.4 | 51.6 | 48.7 | 58.2  |
|  Little \& Su | 34.5 | 47.6 | 52.6 | 48.4 | 51.3 | 41.8  |
|  Household-level wealth items |  |  |  |  |  |   |
|  Nearest Neighbour | 54.4 | 37.4 | 46.6 | 52.5 | 46.8 | 57.4  |
|  Little \& Su | 45.6 | 62.7 | 53.4 | 47.5 | 53.2 | 42.6  |

[^0] [^0]: * In wave 11, a Top-Up sample was included, resulting in a higher use of the Nearest Neighbour method in wave 14.

Table 4.27: Percentage of missing cases imputed by imputation method (home value and home debt), waves 1 - 23

|  Imputation Method | Wave |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | $11^{*}$ | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |   |
|  Home value (households) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest
Neighbour | 28.5 | 6.1 | 10.0 | 10.1 | 10.3 | 12.2 | 9.9 | 9.4 | 10.7 | 13.2 | 19.5 | 15.7 | 17.9 | 12.3 | 16.3 | 18.2 | 11.0 | 11.4 | 13.0 | 12.9 | 14.2 | 16.7 | 35.8 |   |
|  Little \& Su | 71.5 | 93.9 | 90.0 | 89.9 | 89.7 | 87.8 | 90.1 | 90.6 | 89.3 | 86.8 | 80.5 | 84.3 | 82.1 | 87.7 | 83.7 | 81.8 | 89.0 | 88.6 | 87.0 | 87.1 | 85.8 | 83.3 | 64.2 |   |
|  Number imputed | 312 | 378 | 269 | 189 | 156 | 196 | 121 | 139 | 168 | 234 | 220 | 217 | 201 | 235 | 166 | 170 | 173 | 219 | 162 | 139 | 183 | 264 | 148 |   |
|  Home debt (households) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest
Neighbour | 35.4 | 18.0 | 21.1 | 23.4 | 22.5 | 16.3 | 14.9 | 20.6 | 26.4 | 22.4 | 28.0 | 20.7 | 25.7 | 21.1 | 28.8 | 28.4 | 17.8 | 18.6 | 22.0 | 21.8 | 24.9 | 21.1 | 47.9 |   |
|  Little \& Su | 64.6 | 82.0 | 78.9 | 76.6 | 77.5 | 83.7 | 85.1 | 79.4 | 73.6 | 77.6 | 72.0 | 79.3 | 74.3 | 78.9 | 71.2 | 71.6 | 82.2 | 81.4 | 78.0 | 78.2 | 75.1 | 78.9 | 52.1 |   |
|  Number imputed | 181 | 133 | 109 | 107 | 111 | 104 | 114 | 102 | 148 | 170 | 239 | 217 | 210 | 204 | 153 | 183 | 174 | 204 | 168 | 165 | 201 | 209 | 165 |   |

- In wave 11 and 23, a Top-Up sample was added

# 4.26.3. Imputed Wealth Variables 

Table 4.28 outlines the imputed wealth variables included on the files in the wealth waves. Further, as mentioned earlier, home value, _hsvalue, and home debt, _hsdebt, have been imputed in all waves (_hsvalui and _hsdebti) and the imputation flag provided (_hsvaluf and _hsdebtf). _hsvalue differs from _hwhmval in that it is the total value of the home, whereas _hwhmval is the share owned by the household members (which is just collected in the wealth waves). Likewise, _hsdebt is the total debt on the home and _hwhmdt the share owed by the household members (which is just collected in the wealth waves).

Table 4.28: Imputed wealth variables

|  | Pre-imputed | Post-imputed | Flag |
| :--: | :--: | :--: | :--: |
| Responding person file |  |  |  |
| Assets |  |  |  |
| Joint bank accounts | _pwjbank | _pwjbani | _pwjbanf |
| Own bank accounts | _pwobank | _pwobani | _pwobanf |
| Superannuation - retirees | _pwsuprt | _pwsupri | _pwsuprf |
| Superannuation - non-retirees | _pwsupwk | _pwsupwi | _pwsupwf |
| Debts |  |  |  |
| HECS debt | _pwhecdt | _pwhecdi | _pwhecdf |
| Joint credit cards | _pwjccdt | _pwjccdi | _pwjccdf |
| Own credit cards | _pwoccdt | _pwoccdi | _pwoccdf |
| Other personal debt | _pwothdt | _pwothdi | _pwothdf |
| Enumerated person file |  |  |  |
| Assets |  |  |  |
| Joint bank accounts | - | _pwjbani | _pwjbanf |
| Own bank accounts | - | _pwobani | _pwobanf |
| Superannuation - retirees | - | _pwsupri | _pwsuprf |
| Superannuation - non-retirees | - | _pwsupwi | _pwsupwf |
| Debts |  |  |  |
| HECS debt | - | _pwhecdi | _pwhecdf |
| Joint credit cards | - | _pwjccdi | _pwjccdf |
| Own credit cards | - | _pwoccdi | _pwoccdf |
| Other personal debt | - | _pwothdi | _pwothdf |

|  | Pre-imputed | Post-imputed | Flag |
| :-- | :-- | :-- | :-- |

# Household File 

## Assets

| Joint bank accounts | _hwjbank | _hwjbani | _hwjbanf |
| :-- | :-- | :-- | :-- |
| Own bank accounts | _hwobank | _hwobani | _hwobanf |
| Children's bank accounts | _hwcbank | _hwcbani | _hwcbanf |
| Superannuation - retirees | _hwsuprt | _hwsupri | _hwsuprf |
| Superannuation - non-retirees | _hwsupwk | _hwsupwi | _hwsupwf |
| Business assets | _hwbusva | _hwbusvi | _hwbusvf |
| Cash investment | _hwcain | _hwcaini | _hwcainf |
| Equity investment | _hweqinv | _hweqini | _hweqinf |
| Collectibles | _hwcoll | _hwcolli | _hwcollf |
| Home asset | _hwhmval | _hwhmvai | _hwhmvaf |
| Other property assets | _hwopval | _hwopvai | _hwopvaf |
| Life insurance | _hwinsur | _hwinsui | _hwinsuf |
| Trust funds | _hwtrust | _hwtrusi | _hwtrusf |
| Vehicles value | _hwvech | _hwvechi | _hwvechf |
| Total household assets | _hwasset | _hwassei | _hwassef |

## Debts

HECS debt
Joint credit cards
Own credit cards
Other personal debt
Business debt
House debt
Other property debt
_hwhecdt
_hwjccdt
_hwoccdt
_hwothdt
_hwbusdt
_hwhmdt
_hwhmdti
_hwopdt
_hwhecdi
_hwjccdi
_hwoccdi
_hwothdi
_hwbusdi
_hwhmdti
_hwopdti
_hwhecdf
_hwjccdf
_hwoccdf
_hwothdf
_hwbusdf
_hwhmdtf
_hwopdtf

|  | Pre-imputed | Post-imputed | Flag |
| :-- | :--: | :--: | :--: |
| Overdue household bills ${ }^{1}$ | _hwobdt | _hwobdti | _hwobdtf |
| Outstanding loans to others ${ }^{2}$ | _hwlnoth | _hwlnoti | _hwlnotf |
| Total household debts | _hwdebt | _hwdebti | _hwdebtf |
| Net worth | _hwnetwp, _hwnetwn | _hwnwip, _hwnwin | _hwnwf |

${ }^{1}$ Variable not in wave 2.
${ }^{2}$ Variable added from wave 22.

# 4.27. Expenditure 

In every wave, the HILDA Survey collects housing expenditure (on rent and mortgage repayments) in the Household Questionnaire. The household expenditure on groceries, food and meals eaten outside the home were collected in the Household Questionnaire for waves 1, 3-5, and 11 onwards. Household expenditure on a wide range of goods and services were first collected in the wave 5 Self-Completion Questionnaire. The list of items collected was expanded to include consumer durables from wave 6 and some were dropped in wave 11.
While the person in the household responsible for the household bills was asked to complete the household-level expenditure questions in the SCQ, sometimes more than one person in a household provided answers. The variables with the prefix _hx average the responses across all individuals who provided a response to these expenditure questions (the responses from dependent students who stated they are not responsible for the household bills are excluded).

### 4.27.1. Imputation Method

A summary of the steps in the imputation process is provided below:

- Step 1 - Create a longitudinal household identifier. For variables imputed at the household-level, households are linked longitudinally if they had common membership ${ }^{32}$. Deaths and births, for the purposes of expenditure imputation, are counted as membership changes.
- Step 2 - Identify lumpy expenditure items. Some items (such as cars, white goods, etc.) are unlikely to be purchased each year, so need to be treated differently in the imputation process.
- Step 3 - Carryover zeros. The population carryover method is used to determine zero and non-zero expenditure flags for non-lumpy expenditure items prior to any other imputation. Lumpy expenditure items were excluded from this step.
- Step 4 - Nearest Neighbour Regression imputation of zeros. The predicted values from a regression model are used to identify a donor from which to flag zero or non-zero imputes for the recipient. This is essentially a filter process to decide whether the case has the expense or not.
- Step 5 - Nearest Neighbour Regression imputation of non-zero amounts. The predicted values from a regression model are used to identify a donor from which the reported value is taken as the imputed value for the recipient. The models and donor pools are restricted to cases with non-zero amounts. For households

[^0]
[^0]:    ${ }^{32}$ Households that can be linked longitudinally to the subsequent wave for the purposes of expenditure imputation are flagged in _hylink.

without any expenditure data reported in the SCQ, a single donor for all expenditure variables collected in the SCQ was used.

- Step 6 - Little and Su imputation. This method incorporates (via a multiplicative model) the trend across waves (column effect), the recipient's departure from the trend (row effect), and a residual effect donated from another case with complete expenditure information for that component (residual effect). Only cases that have been enumerated in more than one wave, longitudinally linked, and have at least one wave of non-zero data available can be imputed via this method. For the lumpy expenditure items, the donors selected had to have the same zero pattern for the non-missing waves as the recipients. Wherever possible, the Little and Su imputation replaces the Nearest Neighbour Regression imputation. The zero or non-zero determination from steps 3 and 4 is observed.

Imputation classes were used for some variables to ensure the donors and recipients matched on a small number of characteristics (typically equivalised household disposable income bands and the age group of the highest income earner were used).
A full description of the imputation process for the expenditure variables is provided by Sun (2010). Appendix 2 of this User Manual provides an extract from Hayes and Watson (2009) which details the Nearest Neighbour Regression method, the Little and Su method and the Population Carryover method.
Table 4.29 shows the percentage of missing cases that were imputed by each imputation method. ${ }^{33}$ Ideally all the records should be imputed by a longitudinal imputation method, such as the Little and Su method or the Carryover method. The households which cannot be linked between waves were imputed by the Nearest Neighbour Regression method regardless of their situation. For the housing expenditure variables (rent payment, mortgage repayment and second mortgage repayment), which have been collected in all waves so far, the majority of cases were imputed by the Little and Su method. For the expenditure items collected from wave 6 onwards where we have fewer waves of data available, about 30 percent of the cases were imputed by the Nearest Neighbour Regression method.

[^0]
[^0]:    ${ }^{33}$ For the proportion of cases which are missing, see Table 6.8

Table 4.29: Percentage of missing cases imputed by imputation method (expenditure), waves 1 - 23

|  Imputation method | Wave |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |   |
|  Housing and work-related child care expenditure variables (collected in all waves in the Household Questionnaire) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | 45.6 | 12.7 | 17.8 | 18.2 | 11.9 | 23.3 | 14.7 | 20.6 | 20.9 | 22.8 | 16.2 | 17.5 | 19.6 | 18.6 | 19.5 | 20.0 | 15.4 | 20.2 | 20.0 | 15.8 | 23.2 | 13.6 | 37.2 |   |
|  Little \& Su | 46.6 | 71.4 | 75.1 | 77.7 | 79.4 | 72.2 | 76.6 | 75.3 | 67.2 | 61.8 | 69.1 | 72.6 | 68.1 | 71.8 | 70.7 | 69.7 | 73.5 | 69.9 | 69.5 | 72.8 | 65.0 | 67.7 | 57.8 |   |
|  Carryover | 7.8 | 15.9 | 7.0 | 4.1 | 8.8 | 4.5 | 8.7 | 4.1 | 11.9 | 15.5 | 14.7 | 9.9 | 12.3 | 9.6 | 9.9 | 10.3 | 11.1 | 9.9 | 10.5 | 11.4 | 11.9 | 18.7 | 5.0 |   |
|  Non-work-related child care expenditure variables (collected in the Household Questionnaire from wave 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | - | 63.9 | 40.0 | 55.6 | 72.7 | 50.0 | 71.4 | 71.4 | 55.7 | 47.4 | 56.3 | 54.8 | 60.5 | 40.7 | 32.3 | 72.1 | 38.7 | 12.0 | 59.3 | 66.7 | 58.2 | 61.9 | 75.7 |   |
|  Little \& Su | - | 22.2 | 20.0 | 33.3 | 27.3 | 50.0 | 23.8 | 19.1 | 25.4 | 52.6 | 34.4 | 35.5 | 32.6 | 59.3 | 61.3 | 27.9 | 58.1 | 72.0 | 37.0 | 26.7 | 40.0 | 33.3 | 18.9 |   |
|  Carryover | - | 13.9 | 40.0 | 11.1 | 0.0 | 0.0 | 4.8 | 9.5 | 18.9 | 0.0 | 9.4 | 9.7 | 7.0 | 0.0 | 6.5 | 0.0 | 3.2 | 16.0 | 3.7 | 6.7 | 1.8 | 4.8 | 5.4 |   |
|  Weekly household expenditure variables (collected in wave 1, 3-5, 11+ in the Household Questionnaire) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | 55.9 | - | 25.7 | 14.4 | 27.8 | - | - | - | - | - | 32.9 | 13.6 | 19.7 | 12.4 | 13.0 | 12.1 | 9.6 | 10.2 | 6.1 | 9.0 | 15.7 | 11.5 | 29.3 |   |
|  Little \& Su | 43.1 | - | 67.3 | 79.0 | 66.3 | - | - | - | - | - | 62.8 | 77.8 | 70.0 | 80.9 | 79.3 | 77.3 | 83.6 | 81.0 | 84.0 | 79.3 | 74.1 | 73.7 | 61.5 |   |
|  Carryover | 1.0 | - | 7.0 | 6.5 | 5.9 | - | - | - | - | - | 4.4 | 8.6 | 10.3 | 6.7 | 7.7 | 10.7 | 6.8 | 8.8 | 9.9 | 11.7 | 10.2 | 14.9 | 9.2 |   |
|  Annualised household expenditure variables (collected in the Self-Completion Questionnaire from wave 5) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | - | - | - | - | 49.4 | 34.2 | 31.1 | 31.1 | 32.4 | 31.6 | 33.3 | 30.3 | 30.5 | 29.9 | 29.7 | 29.3 | 29.1 | 27.4 | 26.3 | 28.5 | 29.3 | 27.0 | 42.2 |   |
|  Little \& Su | - | - | - | - | 37.8 | 44.9 | 49.8 | 48.9 | 48.6 | 50.0 | 50.1 | 51.0 | 51.7 | 52.1 | 51.8 | 52.5 | 51.0 | 54.1 | 50.4 | 48.7 | 47.1 | 47.2 | 41.5 |   |
|  Carryover | - | - | - | - | 12.9 | 21.0 | 19.2 | 20.0 | 19.1 | 18.4 | 16.5 | 18.7 | 17.9 | 18.0 | 18.5 | 18.2 | 20.0 | 18.5 | 23.3 | 22.8 | 23.7 | 25.8 | 16.3 |   |

|   | Wave |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Imputation method | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |  |   |
|  Annualised household expenditure variables (collected in the Self-Completion Questionnaire from wave 6) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | - | - | - | - | - | 49.2 | 31.0 | 30.1 | 30.4 | 29.6 | 31.8 | 29.3 | 29.9 | 28.1 | 28.7 | 28.6 | 28.3 | 27.2 | 24.9 | 28.5 | 29.4 | 26.9 | 50.7 |  |   |
|  Little \& Su | - | - | - | - | - | 39.6 | 52.0 | 53.2 | 52.8 | 54.2 | 53.5 | 53.8 | 54.1 | 55.8 | 54.5 | 54.5 | 53.1 | 55.6 | 53.9 | 49.4 | 48.0 | 48.4 | 49.4 |  |   |
|  Carryover | - | - | - | - | - | 11.2 | 17.0 | 16.7 | 16.8 | 16.1 | 14.7 | 16.9 | 16.0 | 16.1 | 16.8 | 16.9 | 18.6 | 17.3 | 21.3 | 22.1 | 22.6 | 24.7 | - |  |   |
|  Annualised household expenditure variables (collected in waves 6-10 in the Self-Completion Questionnaire from wave 6) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  Nearest Neighbour | - | - | - | - | - | 88.2 | 84.0 | 84.2 | 84.2 | 87.8 | - | - | - | - | - | - | - | - | - | - | - | - | - | - |   |
|  Little \& Su | - | - | - | - | - | 11.8 | 16.0 | 15.8 | 15.8 | 12.2 | - | - | - | - | - | - | - | - | - | - | - | - | - | - |   |
|  Carryover | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |   |

# 4.27.2. Imputed Household Expenditure Variables 

All expenditure imputation was undertaken at the household-level. Both the pre- and postimputed variables are available in the datasets, along with imputation flags. Table 4.30 provides an overview of the pre- and post-imputed expenditure variables and the waves in which they are available.

Table 4.30: Imputed household expenditure variables

|  | Wave | Pre- <br> imputed ${ }^{1}$ | Post- <br> imputed | Flag |
| :--: | :--: | :--: | :--: | :--: |
| Usual payments/repayments per month (Collected in the HQ) |  |  |  |  |
| Rent | $1+$ | _hsrnt | _hsrnti | _hsrntfg |
| First mortgage | $1+$ | _hsmg | _hsmgi | _hsmgfg |
| Second mortgage | $1+$ | _hssI | _hssli | _hssifg |
| Weekly household expenditure (Collected in the HQ) |  |  |  |  |
| All groceries | $\begin{aligned} & 1,3-5, \\ & 11+ \end{aligned}$ | _xpgroc | _xpgroci | _xpgrocf |
| Groceries for food and drink | $\begin{aligned} & 1,3-5, \\ & 11+ \end{aligned}$ | _xpfood | _xpfoodi | _xpfoodf |
| Meals eaten outside the home | $\begin{aligned} & 1,3-5, \\ & 11+ \end{aligned}$ | _xposml | _xposmli | _xposmlf |
| Total cost of child care, all school age children, during school holidays, across all types of care, while parents work | $1+$ | _chctc | _chctci | _chctcf |
| Total cost of child care, all not yet at school children, across all types of care, while parents work | $1+$ | _cpctc | _cpctci | _cpctcf |
| Total cost of child care for all school age children during term, across all types of care, while parents work | $1+$ | _csctc | _csctci | _csctcf |
| Total cost of child care for all not yet at school children across all types of care, not employment related. | $2+$ | _npctc | _npctci | _npctcf |
| Total cost of child care for all school age children across all types of care, not employment related | $2+$ | _nsctc | _nsctci | _nsctcf |
| Annualised household expenditure (Collected in the SCQ) ${ }^{1}$ |  |  |  |  |
| Groceries | $5+$ | _hxygroc | _hxygrci | _hxygrcf |
| Alcohol | $5+$ | _hxyalc | _hxyalci | _hxyalcf |
| Cigarettes and tobacco | $5+$ | _hxycig | _hxycigi | _hxycigf |
| Public transport and taxis | $5+$ | _hxypubt | _hxypbti | _hxypbtf |
| Meals eaten out | $5+$ | _hxymeal | _hxymli | _hxymlf |
| Leisure activities | 5 | _hxyhsge | _hxyhsgi | _hxyhsgf |
| Motor vehicle fuel | $5+$ | _hxymvf | _hxymvfi | _hxymvff |
| Men's clothing and footwear | $6+$ | _hxymcf | _hxymcfi | _hxymcff |

|  | Wave | Pre- <br> imputed ${ }^{1}$ | Post- <br> imputed | Flag |
| :--: | :--: | :--: | :--: | :--: |
| Women's clothing and footwear | $6+$ | _hxywcf | _hxywcfi | _hxywctf |
| Children's clothing and footwear | $6+$ | _hxyccf | _hxyccfi | _hxyccff |
| Clothing and footwear | 5 | _hxyclth | _hxyclti | _hxycltf |
| Telephone rent and calls | 5 | _hxytel | _hxytli | _hxytlf |
| Telephone rent and calls, internet charges | $6+$ | _hxyteli | _hxytlii | _hxytlif |
| Holidays and holiday travel costs | $5-10$ | _hxyhol | _hxyholi | _hxyholf |
| Private health insurance | $5+$ | _hxyphi | _hxyphii | _hxyphif |
| Other insurances | $6-22$ | _hxyoi | _hxyoii | _hxyoif |
| Home and contents insurance | $23+$ | _hxyhci | _hxyhcii | _hxyhcif |
| Other insurance such as motor vehicle insurance | $23+$ | _hxyoth | _hxyothi | _hxyothf |
| Fees paid to health practitioner | $6+$ | _hxyhltp | _hxyhlpi | _hxyhlpf |
| Medicines, prescriptions and pharmaceuticals | $6+$ | _hxyphrm | _hxyphmi | _hxyphmf |
| Health care | 5 | _hxyhlth | _hxyhthi | _hxyhthf |
| Electricity bills | 5 | _hxyelec | _hxyelei | _hxyelef |
| Gas bills | 5 | _hxygas | _hxygasi | _hxygasf |
| Other heating fuel | 5 | _hxyohf | _hxyohfi | _hxyohff |
| Electricity, gas bills and other heating fuel | $6+$ | _hxyutil | _hxyutli | _hxyutlf |
| Repairs, renovation and maintenance to home | $5+$ | _hxyhmrn | _hxyhmri | _hxyhmrf |
| Motor vehicle repairs and maintenance | $5+$ | _hxymvr | _hxymvri | _hxymvrf |
| Education fees | $5+$ | _hxyeduc | _hxyedci | _hxyedcf |
| Buying brand new vehicles | $6-10$ | _hxyncar | _hxyncri | _hxyncrf |
| Buying used vehicles | $6-10$ | _hxyucar | _hxyucri | _hxyucrf |
| Computers and related services | $6-10$ | _hxycomp | _hxycmpi | _hxycmpf |
| Audio visual equipment | $6-10$ | _hxytvav | _hxytvi | _hxytvf |
| Household appliance | $6-10$ | _hxywg | _hxywgi | _hxywgf |
| Furniture | $6-10$ | _hxyfurn | _hxyfrni | _hxyfrnf |
| Donations to charities or other organisations | $20+$ | _hxychar | _hxychri | _hxychrf |
| Local council rates for home | $22+$ | _hxylcr | _hxylcri | _hxylcrf |
| Owners corporation or strata fees for home | $22+$ | _hxyocf | _hxyocfi | _hxyocff |

[^0]
[^0]:    ${ }^{1}$ The household-level responses provided by each person in the household responsible for household expenditure are provided in equivalent variables to the pre-imputed household expenditure variables from the SCQ (_hx is replaced by _xp to give variables _xpgroc to _xpyocf). Most users will use the _hx variables.

# 4.28. Weights 

### 4.28.1. Cross-Sectional Weights

## Wave 1

Wave 1 is essentially a complex cross-sectional survey. The initial (or design) weights are derived from the probability of selecting the households into the sample. These household weights are adjusted according to information collected about all selected households (both responding and non-responding) and then calibrated so that weighted household estimates from the HILDA Survey match several known household-level benchmarks.
The person-level weights are based on the household-level weights, with adjustments made based on information collected about all the people listed in the responding households. These weights are also calibrated to ensure that the weighted person estimates match several known person-level benchmarks.
More information about the weighting procedure can be found in Watson (2012). See the section below for a description of the benchmarks used.

## Waves 2 to 10

From wave 2 to 10, the 'selection' of the sample is dependent on the wave 1 responding sample and the household and individual attrition after wave 1. The cross-sectional weights for wave 2 onwards include temporary members into the sample (i.e., those people who are part of the sample only because they currently live with a continuing sample member). The underlying probability of selection for these households is amended to account for the various pathways into the relevant wave household. Following this, non-response adjustments are made which require within-sample modelling of non-response probabilities and calibration to known population estimates at both the household and person-level.
The weighting process for wave 2 to 10 is detailed in Watson (2012). See the section below for a description of the benchmarks used.

## Wave 11 to 22

In wave 11, we added a Top-Up sample and the cross-sectional weights integrate the Main sample and the Top-Up sample. In both samples the initial weights are calculated as described above, followed by a non-response adjustment. These weights are then integrated for the parts of each sample that represents the same portion of the population (i.e. the Australian population apart from those who arrived in Australia after 2001). A final calibration step ensures the HILDA estimates match known population estimates. See Watson (2012) for details. From wave 12 onwards, an attrition adjustment is made from wave 1 for the Main sample and from wave 11 for the Top-Up sample (as described in the section above on the weights for waves 2 to 10). The temporary sample members currently living with permanent sample members are included in the cross-sectional weights applicable for the wave.

## Wave 23 onwards

In wave 23, we added a small Immigrant Top-Up sample. The cross-sectional weights integrate the Main sample, the 2011 Top-Up sample and the Immigrant Top-Up sample in the same way as described earlier. Further Immigrant Top-Up samples will occur in waves 24 and 25 .

### 4.28.2. Longitudinal Weights

By comparison, the construction of longitudinal weights is more straightforward and only include an adjustment for attrition and benchmarking back to the initial wave characteristics. The longitudinal weights are described in Watson (2012).

We have provided longitudinal weights for the balanced panel of (PQ) responding persons, SCQ responding persons and enumerated persons from every wave to every other wave and for the balanced panel of any combination of a pair of waves. These weights adjust for attrition from the initial wave and are benchmarked back to the key characteristics of the initial wave. ${ }^{34}$ For instance if you were interested in a panel of respondents from waves 2 through 6 , the weight provided for this panel would adjust for attrition from the balanced panel from wave 2 to 6 and would ensure key characteristics of the wave 2 population (allowing for deaths and overseas movers) are matched.

# 4.28.3. Benchmarks 

The benchmarks used in the weighting process are listed Table 4.31. ${ }^{35}$ Note that very remote parts of New South Wales, Queensland, South Australia, Western Australia and the Northern Territory have been excluded from the benchmarks, which is in line with the practice adopted in similar large-scale surveys run by the ABS. As a result, a small number of cases may have zero weights. Further, the benchmarks also exclude people living in non-private dwellings, so people that move into these dwellings after wave 1 are given zero cross-sectional weights. There are also a small number of households given zero crosssectional weights in wave 11 onwards resulting from the integration of the main and Top-Up samples. More details are provided in Watson (2012).

Table 4.31: Benchmarks used in weighting

|  | Household weights | Enumerated person weights | Responding person weights | SCQ person weights |
| :--: | :--: | :--: | :--: | :--: |
| Cross-sectional weights | - Number of adults by number of children <br> - State by part of State <br> Determined jointly with enumerated person weights | - Sex by broad age <br> - State by part of State <br> - Labour force status <br> - Marital status Determined jointly with household weights | - Sex by broad age <br> - State by part of State <br> - State by labour force status <br> - Marital status <br> - Household composition (number of adults and children) | - Sex by broad age <br> - State by part of State <br> - State by labour force status <br> - Marital status <br> - Household composition (number of adults and children) |

[^0]
[^0]:    ${ }^{34}$ Deaths and overseas movers are included as 'responses' in the balanced panel, so benchmarking to the key characteristics of the initial wave allows for the chance that some non-respondents who are no longer issued to field die or move overseas in later waves.
    ${ }^{35}$ The Australian Bureau of Statistics provide almost all of the benchmarks used in the weighting process. The Labour Force Estimates team provide the estimates for labour force status and marital status, and the Demography Section provide the household estimates and the remaining person estimates. The ABS revised these benchmarks to take into account the data from each Census. The 2021 and 2016 Census data resulted in a 5-year rebasing of estimates (ABS, 2018 (Feature article), 2022). The 2011 Census data resulted in a 20-year recasting of the person and household estimates (ABS, 2013 (Feature article 2)) and this eliminated the need for the HILDA team to make any adjustment to the household estimates between 2001 to 2006 which was previously described in Watson (2012). The ABS have further refined the full series of household estimates for greater longitudinal consistency. The marital status benchmarks have been smoothed by the HILDA team by taking the average of the estimates for wave $t$ and $t-1$. Finally, a non-ABS benchmark of the population estimate of matched deaths from the initial cross-section of the balanced panel was added to the longitudinal weights.

|  | Household weights | Enumerated person weights | Responding person weights | SCQ person weights |
| :--: | :--: | :--: | :--: | :--: |
| Longitudinal weights | Not applicable | - Sex by broad age | - Sex by broad age | - Sex by broad age |
|  |  | - State by part of State | - State by part of State | - State by part of State |
|  |  | - Labour force status <br> - Marital status | - State by labour force status | - State by labour force status |
|  |  | - Household composition (number of adults and children) | - Marital status <br> - Household composition (number of adults and children) | - Marital status <br> - Household composition (number of adults and children) |
|  |  | - Matched deaths | - Matched deaths | - Matched deaths |

# 4.28.4. Replicate Weights 

Replicate weights have been provided for users to calculate standard errors that take into account the complex sample design of the HILDA Survey. These weights can be used by the SAS SURVEY procedures, the STATA 'svy' commands, or the SPSS complex samples procedures (more detail is provided below in the section on Calculating Standard Errors), or you can write your own routine to use these weights. Weights for 45 replicate groups are provided.

### 4.28.5. Weights Provided on the Data Files

Table 4.32 a list of the weights provided in the data files together with a description of those weights. The longitudinal weights provided on the enumerated and responding person files are for the balanced panel from wave 1 to each wave, though other longitudinal weights are provided on the Longitudinal Weights File. Since Release 14, cross-sectional SCQ responding person weights are included in the datasets and these are applicable to variables collected in the SCQ. Longitudinal SCQ responding person weights have been provided since Release 19.
Irrespective of the modifications made in how the weights are constructed, some changes are expected to the weights with each new release. There are three reasons for this. Firstly, corrections may be made to age and sex variables when these are confirmed with individuals in subsequent wave interviews. Secondly, the benchmarks are updated from time to time. Thirdly, duplicate or excluded people in the sample may be identified after the release (very occasionally).

Table 4.32: Weights

| Weights | Description |
| :--: | :--: |
| Household File |  |
| _hhwth ${ }^{1}$ | The household weight is the cross-section population weight for all households responding in the relevant wave. Note the sum of these household weights for wave 1 is approximately 7.4 million. |
| _hhwths | This is the cross-section household population weight rescaled to the sum of the sample size for the relevant wave (i.e. 7682 responding households in wave 1). Use this weight when the statistical package requires the weights to sum to the sample size. |
| _rwh1 to _rwh45 | Cross-section household population replicate weights. |
| Enumerated Person File |  |
| _hhwte ${ }^{1}$ | The enumerated person weight is the cross-section population weight for all people who are usual residents of the responding households in the relevant wave (this includes children, non-respondents and respondents). The sum of these enumerated person weights for wave 1 is 19.0 million. |
| _hhwtes | This is the cross-section enumerated person population weight rescaled to the sum of the sample size for the relevant wave (i.e. for wave 1, 19,914 enumerated persons). Use this weight when the statistical package requires the weights to sum to the sample size. |
| _Inwte | This longitudinal enumerated person weight is the longitudinal population weight for all people who were enumerated (i.e. in responding households) each wave from wave 1 to the wave where this variable resides. This weight applies to the following people in responding households: children, nonrespondents, intermittent respondents, and full respondents. <br> blnwte is for the balanced panel of enumerated persons from wave 1 to 2 clnwte is for the balanced panel from wave 1 to 3 dlnwte is for the balanced panel from wave 1 to $4 \ldots$ <br> These variables are also on the Longitudinal Weights File, but are named differently: wlea_b, wlea_c, wlea_d... |
| _rwe1 to _rwe45 | Cross-section enumerated person population replicate weights. |
| _rwlne1 to _rwlne45 | Longitudinal enumerated person population replicate weights. |
| Responding Person File |  |
| _hhwtrp ${ }^{1}$ | The responding person weight is the cross-section population weight for all people who responded in the relevant wave (i.e. they provided an individual interview). The sum of these responding person weights for wave 1 is 15.0 million. |
| _hhwtsc ${ }^{1}$ | The SCQ responding person weight is the cross-section population weight for all people who responded to the SCQ in the relevant wave (i.e. they provided a self-completion questionnaire). The sum of these responding person weights for wave 1 is 15.0 million. |
| _hhwtrps | This is the cross-section responding person population weight rescaled to sum to the number of responding persons in the relevant wave (i.e. 13,969 in wave 1). Use this weight when the statistical package requires the sum of the weights to be the sample size. |
| _hhwtscs | This is the cross-section SCQ responding person population weight rescaled to sum to the number of responding persons in the relevant wave (i.e. 13,058 in wave 1). Use this weight when the statistical package requires the sum of the weights to be the sample size. |

| Weights | Description |
| :--: | :--: |
| _lnwtrp | This longitudinal responding person weight is the longitudinal population weight for all people responding (i.e. provided an interview) each wave from wave 1 to the wave where this variable resides. <br> blnwtrp is for the balanced panel of respondents from wave 1 to 2 <br> clnwtrp is for the balanced panel from wave 1 to 3 <br> dlnwtrp is for the balanced panel from wave 1 to 4... <br> These variables are also on the Longitudinal Weights File, but are named differently: wlra_b, wlra_c, wlra_d, ... |
| _rwrp1 to _rwrp45 | Cross-sectional responding person population replicate weights (for people who provided an individual interview). |
| _rwsc1 to _rwsc45 | Cross-sectional SCQ responding person population replicate weights (for people who provided a Self-Completion Questionnaire). |
| _rwlnr1 to _rwlnr45 | Longitudinal responding person population replicate weights. |
| Longitudinal Weights File |  |
| wlet1_tn | Longitudinal enumerated person weight for the balanced panel of all people who were enumerated (i.e. part of a responding household) each wave from wave $t 1$ to $t n$. Wave letters are used in place of $t 1$ and $t n$. For example, wlec_ $f$ is the longitudinal enumerated person weight for the balanced panel from wave 3 to 6 . |
| wlet1tn | Longitudinal enumerated person weight for the balanced panel of all people who were enumerated (i.e. part of a responding household) in wave $t 1$ and $t n$. Wave letters are used in place of $t 1$ and $t n$. The paired longitudinal weights do not restrict individuals in any way based on their response status in waves between $t 1$ and $t n$. For example, wlecf is the longitudinal enumerated person weight for the balanced panel of enumerated people in wave 3 and 6 (they may or may not have been enumerated in intervening waves). |
| wleb__j, wlef__n, wlej__r, wlen__v, wleb__n, wlef__r, wlej__v, wleb__r, wlef__v, wleb__v | Longitudinal enumerated person weight for the balanced panel of all people who were enumerated when the wealth module was asked (b__j denotes waves 2, 6 and 10, f__n denotes waves 6,10,14, b__n denotes waves 2, 6, 10 and 14 , etc.). Note the use of a double underscore in the variable name. |
| wlrt1_tn | Longitudinal responding person weight for the balanced panel of all people who were interviewed each wave from wave $t 1$ to $t n$. Wave letters are used in place of $t 1$ and $t n$. For example, wlrc_f is the longitudinal responding person weight for the balanced panel of respondents from wave 3 to 6 . |
| wlrt1tn | Longitudinal responding person weight for the balanced panel of all people who were interviewed in wave $t 1$ and $t n$. Wave letters are used in place of $t 1$ and $t n$. The paired longitudinal weights do not restrict individuals in any way based on their response status in waves between $t 1$ and $t n$. For example, wlrcf is the longitudinal responding person weight for the balanced panel of respondents in wave 3 and 6 (they may or may not have been responding in intervening waves). |
| wlrb__j, wlrf__n, wlri__r, wlrn__v, wlrb__n, wlrf__r, wlri__v, wlrb__r, wlrf__v, wlrb__v | Longitudinal responding person weight for the balanced panel of all people who were interviewed when the wealth module was asked (b__j denotes waves 2, 6 and 10, f__n denotes waves 6,10 , and 14 , b__n denotes waves $2,6,10$ and 14 , etc.). Note the use of a double underscore in the variable name. |
| wlrc__k, wlrg__o, wlrk__s, wlro__w, wlrc__o, wlrg__s, wlrk__w, wlrc__s, wlrg__w, wlrc__w | Longitudinal responding person weight for the balanced panel of all people who were interviewed in the years the retirement module was asked (c__k denotes waves 3, 7 and 11, g__o denotes waves 7, 11 and 15, c__o denotes waves 3, 7,11 and 15, etc.). Note the double underscore in the variable name. |

| Weights | Description |
| :--: | :--: |
| wlre__k, wlrh__o, wlrk__s, wlro__w, wlre__o, wlrh__s, wlrk__w, wlre__s, wlrh__w, wlre__w, wlre__w | Longitudinal responding person weight for the balanced panel of all people who were interviewed in the years the fertility module was asked (e__k denotes waves 5,8 and 11, h__o denotes waves 8,11 and 15 , and e__k denotes waves $5,8,11$ and 15 , etc.). Note the double underscore in the variable name. Note also that from wave 11 the fertility module and the retirement module are run together, so see above for applicable weights in this timeframe (i.e., wlrk__s). |
| wlri__q, wlrg__u, wlri__u | Longitudinal responding person weight for the balanced panel of all people who were interviewed in the years the health module was asked (i__q denotes waves 9, 13 and 17, q__u denotes waves 13, 17 and 21, i__u denotes waves $9,13,17$ and 21). Note the double underscore in the variable name. |
| wlrl__t | Longitudinal responding person weight for the balanced panel of all people who were interviewed in the years the education module was asked (1__t denotes waves 12, 16 and 20). Note the double underscore in the variable name. |
| wlst1_tn | Longitudinal SCQ responding person weight for the balanced panel of all people who completed an SCQ each wave from wave $t 1$ to $t n$. Wave letters are used in place to $t 1$ and $t n$. For example, wlsc_f is the longitudinal SCQ responding person weight for the balanced panel of SCQ respondents from wave 3 to 6 . |
| wlst1tn | Longitudinal SCQ responding person weight for the balanced panel of all people who completed an SCQ in wave $t 1$ and $t n$. Wave letters are used in place of $t 1$ and $t n$. The paired longitudinal weights do not restrict individuals in any way based on their response status in waves between $t 1$ and $t n$. For example, wlrcf is the longitudinal SCQ responding person weight for the balanced panel of SCQ respondents in wave 3 and 6 (they may or may not have provided an SCQ in intervening waves). |

# Longitudinal Replicate Weights File ${ }^{2}$ 

wlet1_tn1 to
wlet1_tn45
wlet1tn1 to wlet1tn45
wlet1__tn1 to
wlet1__tn45
wlrtt_tn1 to wlrt1tn45
wlrtt1tn1 to wlrt1tn45
wlrtt__tn1 to
wlrtt__tn45
wlst1tn1 to wlst1tn45 Longitudinal enumerated person replicate weights for the balanced panel from t1 to $t n$.
Longitudinal enumerated person replicate weights for the balanced panel for selected waves (relating to the repeat of specific modules) from $t 1$ to $t n$.
Longitudinal responding person replicate weights for the balanced panel from t1 to $t n$.
Longitudinal responding person replicate weights for the balanced panel for $t 1$ and $t n$.
Longitudinal responding person replicate weights for the balanced panel for selected waves (relating to the repeat of specific modules) from $t 1$ to $t n$.
Longitudinal SCQ responding person replicate weights for the balanced panel from $t 1$ to $t n$.
Longitudinal SCQ responding person replicate weights for the balanced panel for $t 1$ and $t n$.

[^0]
[^0]:    ${ }^{1}$ To help users identify what effect the inclusion of the Top-Up sample has on the cross-sectional estimates, we have also provided four weights in wave 11 onwards that exclude the Top-Up sample ( hhwthm, hhwterm, hhwtrpm, hhwtscm).
    ${ }^{2}$ The Longitudinal Replicate Weights File is available on request. Please submit your query via Dataverse.

# 4.28.6. Advice on Using Weights 

## Which Weight to Use

For some users, the array of weights on the dataset may seem confusing. This section provides examples of when it would be appropriate to use the different types of weights.
If you want to make inferences about the Australian population from frequencies or crosstabulations of the HILDA sample, then you will need to use weights. If you are only using information collected during the wave 4 interviews (either at the household-level or personlevel) then you would use the wave 4 cross-section weights. Similarly, if you are only using wave 3 information, then you would use the wave 3 cross-section weights, and so on. If you want to infer how people have changed across the five years between waves 1 and 6 (and you are interested in outcomes for waves 2 through to 5 as well), then you would use the longitudinal weights for the balanced panel from wave 1 to 6 . If you are only interested in the 5 -year differences between waves 1 and 6 and are not interested in the intervening waves, then you would use the longitudinal weights for the paired wave panel for wave 1 and 6. Paired wave panel weights are preferred over balanced panel weights where possible to avoid dropping cases unnecessarily.
The following five examples show how the various weights may be used to answer questions about the population:

- What proportion of households rent in 2003? We would use the cross-section household weight for wave 3, chhwth, and obtain a weighted estimate of proportion of households that were renting as at the time of interview.
- How many people live in poor households in 2002? We are interested in the number of individuals with a certain household characteristic, such as having low equivalised disposable household incomes. We would use the cross-section enumerated person weight for wave 2, bhhwte, and count the number of enumerated people in households with poorest 10 per cent of equivalised household incomes. (We do not need to restrict our attention to responding persons only as total household incomes are available for all households after the imputation process. We also want to include children in this analysis and not just limit our analysis to those aged 15 year or older.)
- What is the average salary of professionals in 2003? This is a question that can only be answered from the Responding Person File or Combined File using the cross-section responding person weight for wave 3, chhwtrp. We would identify those reportedly working in professional occupations and take the weighted average of their wages and salaries.
- What proportion of people are overweight in 2009? This question is asked in the Self-Completion Questionnaire. We would use the cross-sectional SCQ responding person weight for wave 14, ihhwtsc (found in the Responding Person File or the Combined File).
- For how many years have people been poor between 2001 and 2006? We might define the 'poorest' 10 per cent of households as having the lowest equivalised household incomes in each wave. We could then calculate how many years' people were poor between wave 1 and wave 6 and apply the longitudinal enumerated person weight (flnwte or equivalently wlea_f) for those people enumerated every wave between wave 1 and 6 .

- What proportion of people have changed their employment status between 2002 and 2007? This question can only be answered by considering the responding persons in both waves. We would use the longitudinal responding person weight for the pair of waves extracted from the Longitudinal Weights File (wlrbg) and construct a weighted cross-tabulation of the employment status of respondents in wave 2 against the employment status of respondents in wave 7.
As the HILDA sample progresses over time, it cannot mimic the population in one important way, being the immigration of individuals after 2001. The addition of the Top-Up sample in wave 11 has helped reduced the bias that this has caused in the estimates. This may result in large changes in some cross-sectional estimates between waves 10 and 11 that are associated with immigration (for example, country of birth, or migration history). See Watson (2012) for further details. The introduction of the Immigrant Top-Up samples in wave 23 (and 24-25) will help to reduce the bias in later years.
When constructing regression models, the researcher needs to be aware of the sample design and non-response issues underlying the data and will need to take account of this in some way.
We have developed a decision tree that users may find helpful in deciding which type of weight to use (for example in descriptive statistics or when comparing unweighted and weighted analyses). See Figure 4.10. We encourage your feedback if you find some of the questions difficult to answer or if you have suggestions for improvement.

# Which weight should I choose? Figure 4.10
Of course. Here is the information from the flowchart converted into a text-based diagram.

Follow the questions below to determine the correct weight for your analysis.

**1. Am I using data from one wave only?**
*   **YES:** Proceed to the **"Cross-sectional weights"** section below.
*   **NO:** Go to question 2.

**2. Am I (or the method that I am using for my analysis is) adding data from one wave to the record of another?**
*(e.g. via lag or lead variables, transitions or changes over time. (Y for fixed effects and random effects, and N for standard pooled OLS))*
*   **NO:** Proceed to the **"Cross-sectional weights"** section below.
*   **YES:** Go to question 3.

**3. Am I using only two observations per person with a consistent time gap?**
*(e.g. a 1-wave gap, or a 4-wave gap?)*
*   **YES:** Proceed to the **"Paired wave longitudinal weights"** section below.
*   **NO:** Go to question 4.

**4. Am I estimating growth or change for a cohort?**
*(e.g. modelling growth trajectories, estimating number of years in a certain state (e.g. retired or poor), or modelling fixed or random effects)*
*   **YES:** Proceed to the **"Full balanced longitudinal weights"** section below.
*   **NO:** Email hilda-inquiries@unimelb.edu.au if you would like some assistance with working out which weight to apply to your particular example.

---

### **Weight Selection Details**

#### **Cross-sectional weights**
*   **If you are using any data from the SCQ:**
    *   **YES:** Use the **SCQ weights (_hhwtsc)**
*   **If NO, are you using any data from the PQ?**
    *   **YES:** Use the **RP weights (_hhwtrp)**
*   **If NO, are you only using data from the HF or HQ at the household level?**
    *   **YES:** Use the **HH weights (_hhwth)**
*   **If NO, are you only using data from the HF or HQ at the person level?**
    *   **YES:** Use the **EP weights (_hhwte)**

#### **Paired wave longitudinal weights**
*   **If you are using any data from the SCQ:**
    *   **YES:** Use the **SCQ paired weights (_wlsrt1tn)**
*   **If NO, are you using any data from the PQ?**
    *   **YES:** Use the **RP paired weights (_wlrt1tn)**
*   **If NO, are you only using data from the HF or HQ at the person level?**
    *   **YES:** Use the **EP paired weights (_wlet1tn)**

#### **Full balanced longitudinal weights**
*   **If you are using any data from the SCQ:**
    *   **YES:** Use the **SCQ full balanced weights (_wlst1_tn)**
*   **If NO, are you using any data from the PQ?**
    *   **YES:** Use the **RP full balanced weights (_wlrt1_tn, or _wlrt1__tn for rotating modules)**
*   **If NO, are you only using data from the HF or HQ at the person level?**
    *   **YES:** Use the **EP full balanced weights (_wlet1_tn, or _wletj__tn for rotating modules)**

---

### **Definitions**
*   **SCQ:** Self-Completion Questionnaire
*   **PQ:** Person Questionnaire
*   **HF:** Household Form
*   **HQ:** Household Questionnaire
*   **t1:** start of panel of interest
*   **tn:** end of panel of interest


# Calculating Standard Errors 

The HILDA Survey has a complex survey design that needs to be taken into account when calculating standard errors. It is:

- clustered - 488 areas were originally selected in wave 1, plus a further 125 areas selected for the Top-Up sample, from which households were chosen and people are clustered within households;
- stratified - the 613 areas were selected from a frame of areas stratified by State and part of State; and
- unequally weighted - the households and individuals have unequal weights due to some irregularities in the selection of the sample in wave 1 and the nonrandom non-response in wave 1 and the non-random attrition in later waves.
Some options available for the calculation of appropriate standard errors and confidence intervals include:
- Standard Error Tables - Based on the wave 1 data, approximate standard errors have been constructed for a range of estimates (see Horn, 2004). Similar tables for later waves have not been produced.
- Use the SPSS add-on module "SPSS Complex Samples" (available from SPSS Release 12). The add-on module produces standard errors via the Taylor Series approximation. SPSS does not have a built-in feature to handle replicates weights at this time.
- Use SAS procedures SURVEYMEANS, SURVEYREG, SURVEYFREQ, SURVEYLOGISTIC, and SURVEYPHREG (SURVEYFREQ and SURVEYLOGISTIC are included in SAS Version 9 onwards and SURVEYPHREG is included since Version 9.3). Since the release of SAS Version 9, you can calculate standard errors via Taylor Series approximation or the Jackknife method. Alternatively, there is a SAS macro has been provided by one of our users in the program library that applies the Jackknife method.
- Use the GREGWT macro in SAS - Some users within DSS, ABS and other organisations may have access to the GREGWT macro that can be used to construct various population estimates. The macro uses the Jackknife method to estimate standard errors using the replicate weights.
- Use the 'svy' commands in STATA - Stata has a set of survey commands that deal with complex survey designs. Using the 'svyset' commands, the clustering, stratification and weights can be assigned. You can request the standard errors be calculated using the Jackknife method using 'svy' and the replicate weights. Various statistical procedures are available within the suite of 'svy' commands including means, proportions, tabulations, linear regression, logistic regression, probit models and a number of other commands.
A User Guide for calculating the standard errors in HILDA is provided as part of our technical paper series (see Hayes, 2008). Example code is provided in SAS, SPSS and Stata. Also see programs 18 to 21 in the program library described in Section 3.7.

To assist you in the calculation of appropriate standard errors, the wave 1 area (cluster), and proxy stratification variables have been included all files. These are listed in Table 4.33 and need to be specified for the standard error calculations using the Taylor Series approximation method as suggested above. Any new entrants to the household are assigned to the same sample design information as the permanent sample member they join.

Table 4.33: Sample design variables

| Variable | Description | Design element |
| :-- | :-- | :-- |
| xhhraid | DV: randomised area id | Cluster |
| xhhstrat | DV: Wave 1 Strata | Proxy stratification ${ }^{1}$ |

${ }^{1}$ As of Release 6 the proxy stratification variable has replaced the major statistical region as the variable to be used in the Taylor Series approximation method. The revised stratification variable is essentially a collapsed area unit variable that approximates both the effect of the systematic selection and stratification of the survey selection better than only using the variable for the major statistical region.
Also, a few users may be interested in the sample design weight in wave 1 before any benchmark or non-response adjustments have been made. This is available on the Household File as ahhwtdsn.