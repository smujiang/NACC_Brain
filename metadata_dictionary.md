# NACC MRI Metadata – Variable Dictionary

This file documents the main columns in the NACC metadata CSV that accompanies MRI brain images.  
Most variables come from the **NACC Uniform Data Set (UDS v3)**, with some derived variables and neuropathology variables.  
Authoritative definitions are available in:

- **UDS v3 Researchers Data Dictionary (RDD–UDS)**:contentReference[oaicite:0]{index=0}  
- **NP Researchers Data Dictionary (RDD–NP)**:contentReference[oaicite:1]{index=1}  
- **Description of NACC Derived Variables**:contentReference[oaicite:2]{index=2}  

Use this README as a quick reference; for precise coding rules and allowable values, always consult the official NACC documents.

---

## 1. Form-header and visit-level variables

| Column name | Description (short) |
|------------|----------------------|
| `NACCID`   | Random NACC subject ID used across all NACC datasets (UDS, imaging, NP, etc.).:contentReference[oaicite:3]{index=3} |
| `NACCADC`  | ID of Alzheimer’s Disease Center (ADC) where subject was seen.:contentReference[oaicite:4]{index=4} |
| `PACKET`   | Packet code indicating visit type (initial, follow-up, telephone packet, etc.).:contentReference[oaicite:5]{index=5} |
| `FORMVER`  | Version number of the UDS form used at that visit (integer part of the form version).:contentReference[oaicite:6]{index=6} |
| `VISITMO`  | Visit month (MM) from the UDS visit date.:contentReference[oaicite:7]{index=7} |
| `VISITDAY` | Visit day (DD) from the UDS visit date.:contentReference[oaicite:8]{index=8} |
| `VISITYR`  | Visit year (YYYY) from the UDS visit date.:contentReference[oaicite:9]{index=9} |
| `NACCVNUM` | UDS visit sequence number for that subject (1 = first/initial visit).:contentReference[oaicite:10]{index=10} |
| `NACCAVST` | Total number of all UDS visits ever completed by the subject (in-person + telephone).:contentReference[oaicite:11]{index=11} |
| `NACCNVST` | Total number of **in-person** UDS visits completed by the subject.:contentReference[oaicite:12]{index=12} |
| `NACCDAYS` | Days from initial UDS visit to the subject’s most recent visit (cross-sectional follow-up time).:contentReference[oaicite:13]{index=13} |
| `NACCFDYS` | Days from initial visit to **this** visit (longitudinal follow-up time).:contentReference[oaicite:14]{index=14} |
| `NACCCORE` | Indicator that the subject is part of the UDS “core” cohort (vs special/local cohorts); see RDD–UDS. |
| `NACCREAS` | Derived primary reason for coming to the ADC (e.g., memory concern, research volunteer).:contentReference[oaicite:15]{index=15} |
| `NACCREFR` | Derived principal referral source to the ADC (self-referral, clinic, study, etc.).:contentReference[oaicite:16]{index=16} |

---

## 2. Subject demographics (Form A1)

| Column name | Description |
|------------|-------------|
| `BIRTHMO`  | Subject’s month of birth (1–12).:contentReference[oaicite:17]{index=17} |
| `BIRTHYR`  | Subject’s year of birth (4-digit).:contentReference[oaicite:18]{index=18} |
| `SEX`      | Subject’s sex (typically 1 = male, 2 = female; see coding guide).:contentReference[oaicite:19]{index=19} |
| `HISPANIC` | Indicator of Hispanic/Latino ethnicity.:contentReference[oaicite:20]{index=20} |
| `HISPOR`   | Specific Hispanic origin (e.g., Mexican, Puerto Rican, other).:contentReference[oaicite:21]{index=21} |
| `HISPORX`  | Free-text “other Hispanic origin” if HISPOR is “other”.:contentReference[oaicite:22]{index=22} |
| `RACE`     | Primary race category.:contentReference[oaicite:23]{index=23} |
| `RACEX`    | Free-text “other race” if RACE indicates other.:contentReference[oaicite:24]{index=24} |
| `RACESEC`  | Second race (for multi-racial individuals).:contentReference[oaicite:25]{index=25} |
| `RACESECX` | Free-text “other second race” if RACESEC indicates other.:contentReference[oaicite:26]{index=26} |
| `RACETER`  | Third race (if reported).:contentReference[oaicite:27]{index=27} |
| `RACETERX` | Free-text “other third race” if RACETER indicates other.:contentReference[oaicite:28]{index=28} |
| `PRIMLANG` | Primary language spoken by the subject.:contentReference[oaicite:29]{index=29} |
| `PRIMLANX` | Free-text “other primary language” when PRIMLANG = other.:contentReference[oaicite:30]{index=30} |
| `EDUC`     | Years of formal education completed.:contentReference[oaicite:31]{index=31} |
| `MARISTAT` | Marital status (married, widowed, divorced, never married, etc.).:contentReference[oaicite:32]{index=32} |
| `NACCLIVS` | Derived living situation category (alone, with spouse/partner, facility, etc.).:contentReference[oaicite:33]{index=33} |
| `INDEPEND` | Functional independence level (independent vs requires assistance).:contentReference[oaicite:34]{index=34} |
| `RESIDENC` | Type of residence (private home, retirement community, nursing home, etc.).:contentReference[oaicite:35]{index=35} |
| `HANDED`   | Handedness (right, left, both).:contentReference[oaicite:36]{index=36} |

---

## 3. Co-participant (informant) demographics (Form A2)

| Column name | Description |
|------------|-------------|
| `INBIRMO`  | Informant’s month of birth.:contentReference[oaicite:37]{index=37} |
| `INBIRYR`  | Informant’s year of birth.:contentReference[oaicite:38]{index=38} |
| `INSEX`    | Informant’s sex.:contentReference[oaicite:39]{index=39} |
| `NEWINF`   | Whether the informant is new at this visit (not used at prior UDS visits).:contentReference[oaicite:40]{index=40} |
| `INHISP`   | Informant’s Hispanic/Latino ethnicity.:contentReference[oaicite:41]{index=41} |
| `INHISPOR` | Informant’s specific Hispanic origin.:contentReference[oaicite:42]{index=42} |
| `INHISPOX` | Free-text “other Hispanic origin” for informant.:contentReference[oaicite:43]{index=43} |
| `INRACE`   | Informant’s race.:contentReference[oaicite:44]{index=44} |
| `INRACEX`  | Free-text “other race” for informant.:contentReference[oaicite:45]{index=45} |
| `INRASEC`  | Informant’s second race.:contentReference[oaicite:46]{index=46} |
| `INRASECX` | Free-text “other second race” for informant.:contentReference[oaicite:47]{index=47} |
| `INRATER`  | Informant’s third race.:contentReference[oaicite:48]{index=48} |
| `INRATERX` | Free-text “other third race” for informant.:contentReference[oaicite:49]{index=49} |
| `INEDUC`   | Informant’s years of education.:contentReference[oaicite:50]{index=50} |
| `INRELTO`  | Informant’s relationship to the subject (spouse, child, friend, etc.).:contentReference[oaicite:51]{index=51} |
| `INRELTOX` | Free-text “other relationship”.:contentReference[oaicite:52]{index=52} |
| `INKNOWN`  | How long the informant has known the subject.:contentReference[oaicite:53]{index=53} |
| `INLIVWTH` | Whether the informant lives with the subject.:contentReference[oaicite:54]{index=54} |
| `INVISITS` | If not living together: frequency of **in-person** visits.:contentReference[oaicite:55]{index=55} |
| `INCALLS`  | If not living together: frequency of **telephone** contact.:contentReference[oaicite:56]{index=56} |
| `INRELY`   | Clinician’s judgment of informant reliability as a historian.:contentReference[oaicite:57]{index=57} |
| `NACCNINR` | Derived NIH race category for informant (harmonized).:contentReference[oaicite:58]{index=58} |

---

## 4. Family history of cognitive impairment (Form A3)

| Column name | Description |
|------------|-------------|
| `NACCFAM`  | Indicator that at least one first-degree relative has cognitive impairment or dementia.:contentReference[oaicite:59]{index=59} |
| `NACCMOM`  | Indicator that the subject’s **mother** had cognitive impairment/dementia.:contentReference[oaicite:60]{index=60} |
| `NACCDAD`  | Indicator that the subject’s **father** had cognitive impairment/dementia.:contentReference[oaicite:61]{index=61} |
| `NACCAM`   | Evidence for an Alzheimer’s disease (AD) mutation in the family (any specific AD mutation).:contentReference[oaicite:62]{index=62} |
| `NACCAMX`  | Free-text “other AD mutation” specification if NACCAM indicates “other”.:contentReference[oaicite:63]{index=63} |
| `NACCAMS`  | Source of evidence for AD mutation (genetic test, clinical report, etc.).:contentReference[oaicite:64]{index=64} |
| `NACCAMSX` | Free-text “other evidence source” for AD mutation.:contentReference[oaicite:65]{index=65} |
| `NACCFADM` | Evidence for a **dominantly inherited AD mutation** in the family.:contentReference[oaicite:66]{index=66} |
| `NACCFFTD` | Evidence for a frontotemporal lobar degeneration (FTLD) mutation in the family.:contentReference[oaicite:67]{index=67} |
| `NACCFM`   | Evidence for a **specific FTLD mutation** (e.g., MAPT, GRN, C9orf72, FUS).:contentReference[oaicite:68]{index=68} |
| `NACCFMX`  | Free-text “other FTLD mutation” if NACCFM indicates other mutation.:contentReference[oaicite:69]{index=69} |
| `NACCFMS`  | Source of evidence for FTLD mutation.:contentReference[oaicite:70]{index=70} |
| `NACCFMSX` | Free-text “other evidence source” for FTLD mutation.:contentReference[oaicite:71]{index=71} |
| `NACCOM`   | Evidence for a **non-AD, non-FTLD** genetic mutation associated with neurodegenerative disease.:contentReference[oaicite:72]{index=72} |
| `NACCOMX`  | Free-text “other mutation” corresponding to NACCOM.:contentReference[oaicite:73]{index=73} |
| `NACCOMS`  | Source of evidence for other mutation.:contentReference[oaicite:74]{index=74} |
| `NACCOMSX` | Free-text “other evidence source” for other mutation.:contentReference[oaicite:75]{index=75} |

---

## 5. Medication variables (Form A4G/A4D – grouped)

These variables describe whether the subject is currently taking any medications and, if a full A4 medication form is submitted, the individual drug codes.

| Column / pattern | Description |
|------------------|-------------|
| `ANYMEDS`        | Indicator that subject is currently taking **any** medications at the time of visit.:contentReference[oaicite:76]{index=76} |
| `DRUG1`–`DRUG40` | Encoded medication identifiers for up to 40 concurrent medications (correspond to rows on A4 form; the precise drug list is maintained by NACC’s medication lookup tool).:contentReference[oaicite:77]{index=77} |

---

## 6. Tobacco and alcohol history

| Column name | Description |
|------------|-------------|
| `TOBAC30`  | Smoked at least once in the **past 30 days** (yes/no). |
| `TOBAC100` | Smoked at least 100 cigarettes in lifetime. |
| `SMOKYRS`  | Approximate total years of smoking. |
| `PACKSPER` | Typical packs of cigarettes per day when smoking. |
| `QUITSMOK` | Has the subject quit smoking (and when). |
| `ALCOCCAS` | Drinks alcoholic beverages – indicator for any current alcohol use. |
| `ALCFREQ`  | Frequency of alcohol consumption (times per week/month). |

(Exact coding categories are in the UDS health history form A4H.:contentReference[oaicite:78]{index=78})

---

## 7. Cardiovascular / cerebrovascular history (subset)

These are a subset of the many CV / neurologic history variables present in your header:

| Column | Description |
|--------|-------------|
| `CVHATT`   | History of myocardial infarction (heart attack). |
| `HATTMULT` | Indicator of multiple prior heart attacks. |
| `HATTYEAR` | Year of most recent heart attack. |
| `CVAFIB`   | History of atrial fibrillation. |
| `CVANGIO`  | History of coronary angiography. |
| `CVBYPASS` | History of coronary artery bypass surgery. |
| `CVPACDEF` / `CVPACE` | History of pacemaker or implanted cardiac defibrillator. |
| `CVCHF`    | History of congestive heart failure. |
| `CVANGINA` | History of angina. |
| `CVHVALVE` | History of heart valve disease or surgery. |
| `CVOTHR` / `CVOTHRX` | Other cardiovascular conditions and free-text description. |
| `CBSTROKE` | History of clinically diagnosed stroke. |
| `STROKMUL` | Indicator that ≥2 strokes have occurred. |
| `NACCSTYR` | Year of most recent stroke. |
| `CBTIA`    | History of transient ischemic attack (TIA). |
| `TIAMULT`  | Multiple TIAs. |
| `NACCTIYR` | Year of most recent TIA. |

(Full cardiovascular/neurologic history list is in UDS health history forms.:contentReference[oaicite:79]{index=79})

---

## 8. Selected comorbidities and risk factors (subset)

Your header includes many comorbidity flags; the most commonly used in MRI/cognition analyses include:

| Column | Description |
|--------|-------------|
| `PD`, `PDYR`      | History and year of Parkinson disease diagnosis. |
| `SEIZURES`       | History of seizures. |
| `DIABETES`, `DIABTYPE` | History of diabetes and diabetes type. |
| `HYPERTEN`       | History of hypertension. |
| `HYPERCHO`       | History of hypercholesterolemia / hyperlipidemia. |
| `B12DEF`         | History of B12 deficiency. |
| `THYROID`        | History of thyroid disease. |
| `ARTHRIT`, `ARTHTYPE`, `ARTHTYPX` | History and type of arthritis (e.g., osteoarthritis, rheumatoid, other). |
| `INCONTU`, `INCONTF` | Urinary and fecal incontinence. |
| `APNEA`, `RBD`, `INSOMN`, `OTHSLEEP`, `OTHSLEEX` | Sleep apnea, REM behavior disorder, insomnia, and other sleep disorders (with free-text description). |
| `ALCOHOL`, `ABUSOTHR`, `ABUSX` | History of alcohol or other substance abuse and free-text description. |
| `PTSD`, `BIPOLAR`, `SCHIZ`, `DEP2YRS`, `DEPOTHR`, `ANXIETY`, `OCD`, `NPSYDEV` | Psychiatric history flags (PTSD, bipolar, schizophrenia, depression within 2 years, other depression, anxiety, OCD, neurodevelopmental disorders). |

---

## 9. Physical exam and vitals

| Column | Description |
|--------|-------------|
| `HEIGHT`, `WEIGHT` | Height (inches or cm per coding guide) and weight (lbs or kg). |
| `BPSYS`, `BPDIAS`  | Systolic and diastolic blood pressure. |
| `HRATE`           | Resting heart rate. |
| `VISION`, `VISCORR`, `VISWCORR` | Vision status uncorrected, corrected, and with correction. |
| `HEARING`, `HEARAID`, `HEARWAID` | Hearing status, use of hearing aids, and hearing with aids. |

---

## 10. Cognitive, functional, and behavioral measures (high-level)

Your header line includes a very large number of items from:

- **CDR® + NACC FTLD** (`MEMORY`, `ORIENT`, `JUDGMENT`, `COMMUN`, `HOMEHOBB`, `PERSCARE`, `CDRSUM`, `CDRGLOB`, `COMPORT`, `CDRLANG`, etc.).:contentReference[oaicite:80]{index=80}  
- **NPI-Q** (`NPIQINF`, `DEL`, `DELSEV`, `HALL`, `HALLSEV`, `AGIT`, `AGITSEV`, …, `APP`, `APPSEV`).:contentReference[oaicite:81]{index=81}  
- **GDS** (`NOGDS`, `SATIS`, `DROPACT`, …, `NACCGDS`).:contentReference[oaicite:82]{index=82}  
- **Function / IADL items** (`BILLS`, `TAXES`, `SHOPPING`, `GAMES`, `STOVE`, `MEALPREP`, `EVENTS`, `PAYATTN`, `REMDATES`, `TRAVEL`).:contentReference[oaicite:83]{index=83}  
- **Neurologic exam / parkinsonian signs** (`TRESTFAC`, `TRESTLHD`, `RIGDUPRT`, `TAPSRT`, `HANDMOVR`, `GAIT`, `POSSTAB`, `BRADYKIN`, etc.).:contentReference[oaicite:84]{index=84}  
- **Global cognitive status** (`COGSTAT`, `NORMCOG`, `DEMENTED`, `AMNDEM`, `NACCTMCI`, etc.).:contentReference[oaicite:85]{index=85}  
- **MMSE**, **MoCA**, **neuropsych test scores**, and other cognitive batteries (`MMSECOMP`, `NACCMMSE`, `MOCACOMP`, `NACCMOCA`, `CRAFTVRS`, `DIGFORCT`, `TRAILA`, `TRAILB`, `BOSTON`, `UDSVER*`, etc.).:contentReference[oaicite:86]{index=86}  

For each of these, the *short descriptor* in the RDD–UDS gives a concise interpretation (e.g., “CDR – memory domain rating”, “NPI-Q – delusions present?”, “GDS item: basically satisfied with life?”). Instead of repeating hundreds of items here, please refer to the Cognitive / Behavioral forms sections of the RDD–UDS.

---

## 11. Neuropathology (NP) variables (subset)

The latter part of your header contains NP variables from the NACC Neuropathology dataset (NP). Examples:

| Column | Description |
|--------|-------------|
| `NPFORMVER` | Neuropathology form version.:contentReference[oaicite:87]{index=87} |
| `NPSEX`     | Sex from NP dataset.:contentReference[oaicite:88]{index=88} |
| `NACCDAGE`  | Age at death (years).:contentReference[oaicite:89]{index=89} |
| `NACCMOD`, `NACCYOD`, `NACCINT` | Month & year of death, and days from last UDS visit to death.:contentReference[oaicite:90]{index=90} |
| `NPWBRWT`, `NPWBRF` | Whole brain weight and whether weight is fresh vs fixed.:contentReference[oaicite:91]{index=91} |
| `NPGRCCA`, `NPGRLA`, `NPGRHA`, `NPGRSNH`, `NPGRLCH` | Semi-quantitative gross atrophy / hypopigmentation ratings in cortex, lobes, hippocampus, substantia nigra, locus coeruleus.:contentReference[oaicite:92]{index=92} |
| `NACCAVAS`  | Gross atherosclerosis of circle of Willis.:contentReference[oaicite:93]{index=93} |
| `NPTAN`, `NPABAN`, `NPASAN`, `NPTDPAN` (+ `*X`) | Antibodies used for tau, amyloid-β, α-synuclein, and TDP-43 immunohistochemistry and “other, specify” text.:contentReference[oaicite:94]{index=94} |
| `NPTHAL`, `NACCBRAA`, `NACCNEUR`, `NPADNC` | Thal amyloid phase (A), Braak NFT stage (B), CERAD neuritic plaque density (C), and NIA-AA AD neuropathologic change.:contentReference[oaicite:95]{index=95} |
| `NACCVASC`, `NACCAMY`, `NPLINF`, `NPLAC`, `NPINF*`, `NPHEM*`, `NPOLD*`, `NACCMICR`, `NACCHEM` | Cerebrovascular and hemorrhagic lesion indicators and counts (large infarcts, lacunes, microinfarcts, hemorrhages, old infarcts by region, etc.).:contentReference[oaicite:96]{index=96} |
| `NACCARTE`, `NPWMR` | White-matter rarefaction, arteriosclerosis, and other vascular changes.:contentReference[oaicite:97]{index=97} |
| `NACCALZD`, `NACCALZP`, `PROBAD`, `POSSAD` | NP-based AD diagnoses and probability (definite/probable/possible AD).:contentReference[oaicite:98]{index=98} |
| `NACCLEWY`, `NPLBOD`, `NPPVASC`, `NPCVASC`, `NPPFTLD`, `NPCFTLD`, `NPPPRION`, `NPCPRION`, `NPPHIPP`, `NPCHIPP`, `NPPOTH*`, `NPCOTH*` | Summary NP diagnoses: Lewy body disease, vascular pathologies, FTLD, prion disease, hippocampal sclerosis, and other specified pathologies and their clinicopathologic correlations.:contentReference[oaicite:99]{index=99} |

For a complete variable-by-variable description of all NP fields in your header, use the NP RDD, which has a table “Section / Variable name / Short descriptor”.:contentReference[oaicite:100]{index=100}  

---

## 12. Genetic and biomarker variables

Near the end of your header are variables related to APOE genotype and biomarkers:

| Column | Description |
|--------|-------------|
| `NACCAPOE` | APOE genotype (coded categories such as ε3/ε3, ε3/ε4, ε4/ε4, etc.).:contentReference[oaicite:101]{index=101} |
| `NACCNE4S` | Number of APOE ε4 alleles (0, 1, 2).:contentReference[oaicite:102]{index=102} |
| `AMYLPET`, `AMYLCSF`, `FDGAD`, `TAUPETAD`, `CSFTAU`, `FDGFTLD`, `TPETFTLD`, `MRFTLD`, `DATSCAN`, `OTHBIOM`, `OTHBIOMX` | PET/CSF/MRI biomarker indicators for amyloid, tau, FDG, FTLD, DATScan, and other biomarkers with “other, specify” text.:contentReference[oaicite:103]{index=103} |

---

## 13. How to use this dictionary with MRI data

Typical linkage strategy for MRI + NACC metadata:

1. **Key link field:** `NACCID` – present in both the imaging table and your clinical CSV.  
2. Use `VISITYR`, `VISITMO`, `VISITDAY`, and `NACCVNUM` to align MRI acquisition with the closest clinical visit.
3. Subset the variables above (demographics, comorbidities, diagnoses, cognitive scores, NP) as covariates in your MRI analyses.

---

## 14. Extending this README

Header string includes **hundreds** of UDS and NP variables. Documenting every item line-by-line here would essentially reproduce the full NACC RDD. Instead, this README:

- Covers the variables most commonly used in imaging and survival/cognitive modeling.
- Groups large item banks (CDR, NPI-Q, GDS, neuro exam, neuropsych scores, full NP section) and points to the exact NACC sources where each item’s wording and coding are defined.:contentReference[oaicite:104]{index=104}  

