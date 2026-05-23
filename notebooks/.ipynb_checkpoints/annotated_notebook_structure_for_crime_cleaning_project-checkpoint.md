# Crime Dataset Cleaning Notebook Structure

---

## Cell 1 — Project Introduction (Markdown)

```markdown
# Crime Dataset Data Cleaning & Preprocessing Project

This project focuses on cleaning and preprocessing a messy crime incidents dataset using Python and Pandas.

## Project Objectives
- Handle missing values
- Remove duplicate records
- Standardize inconsistent categorical data
- Clean phone numbers and text fields
- Prepare the dataset for future analysis and machine learning
```

---

## Cell 2 — Importing Libraries (Markdown)

```markdown
## Importing Libraries

The required Python libraries for data manipulation and analysis are imported below.
```

## Your Code

```python
import numpy as np
import pandas as pd

df = pd.read_csv('../data/raw/crime_incidents_messy.csv')
```

---

## Cell 3 — Dataset Preview (Markdown)

```markdown
## Dataset Overview

Displaying the first few rows of the dataset to inspect the available columns and identify obvious inconsistencies.
```

## Your Code

```python
df.head()
```

---

## Cell 4 — Dataset Information (Markdown)

```markdown
## Checking Dataset Information

The `.info()` method is used to inspect data types and identify columns containing missing values.
```

## Your Code

```python
df.info()
```

---

## Cell 5 — Statistical Summary (Markdown)

```markdown
## Statistical Summary

Basic statistical analysis is performed to better understand numerical columns and detect potential anomalies or outliers.
```

## Your Code

```python
df.describe()
```

---

## Cell 6 — Missing Values Inspection (Markdown)

```markdown
## Checking Missing Values

The number of missing values in each column is calculated to determine which columns require cleaning or imputation.
```

## Your Code

```python
df.isnull().sum()
```

---

## Cell 7 — Removing Duplicates (Markdown)

```markdown
## Removing Duplicate Records

Duplicate rows are removed to improve data quality and prevent repeated observations from affecting future analysis.
```

## Your Code

```python
df = df.drop_duplicates()
```

---

## Cell 8 — Resetting Index (Markdown)

```markdown
## Resetting the Index

The DataFrame index is reset after removing duplicate rows to maintain a clean sequential index.
```

## Recommended Improvement

```python
df = df.reset_index(drop=True)
```

---

## Cell 9 — Cleaning Crime Type Values (Markdown)

```markdown
## Standardizing Crime Type Values

Crime type labels are normalized into a consistent title format to improve categorical consistency.
```

## Your Code

```python
df['crime_type'] = df['crime_type'].str.lower().str.title()
df
```

---

## Cell 10 — Cleaning District Names (Markdown)

```markdown
## Standardizing District Names

District values are converted into a consistent text format to avoid duplicated categories caused by inconsistent capitalization.
```

## Your Code

```python
df['district'] = df['district'].str.lower().str.title()
df
```

---

## Cell 11 — Handling Missing Values (Markdown)

```markdown
## Handling Missing Values

Missing values are handled differently depending on the meaning of each column and the context of the data.
```

## Your Code

```python
df['latitude'] = df['latitude'].fillna('Unknown')
df['longitude'] = df['longitude'].fillna('Unknown')

df['badge_number'] = df['badge_number'].fillna('Unknown')

df['suspect_id'] = df['suspect_id'].fillna('Unknown')
df['suspect_first_name'] = df['suspect_first_name'].fillna('Unknown')
df['suspect_last_name'] = df['suspect_last_name'].fillna('Unknown')

df['suspect_gender'] = df['suspect_gender'].fillna('Unknown')
df['suspect_race'] = df['suspect_race'].fillna('Unknown')

df['victim_id'] = df['victim_id'].fillna('Unknown')
df['victim_first_name'] = df['victim_first_name'].fillna('Unknown')
df['victim_last_name'] = df['victim_last_name'].fillna('Unknown')
df['victim_gender'] = df['victim_gender'].fillna('Unknown')
df['victim_phone'] = df['victim_phone'].fillna('Unknown')
```

---

## Cell 12 — Handling Missing Age Values (Markdown)

```markdown
## Handling Missing Age Values

Missing age values are replaced using the average age to preserve the numerical distribution of the dataset.
```

## Your Code

```python
df['suspect_age'] = df['suspect_age'].fillna(df['suspect_age'].mean())
df['victim_age'] = df['victim_age'].fillna(df['victim_age'].mean())
```

---

## Cell 13 — Cleaning Weapon Information (Markdown)

```markdown
## Cleaning Weapon Information

Missing values in `weapon_used` likely indicate incidents where no weapon was involved. Missing values are replaced with `"Unarmed"`.
```

## Your Code

```python
df['weapon_used'] = df['weapon_used'].fillna('Unarmed')
df
```

---

## Cell 14 — Cleaning Case Information (Markdown)

```markdown
## Cleaning Case Information

Several case-related columns are standardized by replacing missing values with default placeholders or logical values.
```

## Your Code

```python
df['severity'] = df['severity'].fillna('Unknown')
df['case_status'] = df['case_status'].fillna('Unknown')
df['resolution'] = df['resolution'].fillna('Unknown')
df['num_arrests'] = df['num_arrests'].fillna('Unknown')
df['property_loss_usd'] = df['property_loss_usd'].fillna(0)
df['reported_online'] = df['reported_online'].fillna('Unknown')
```

---

## Cell 15 — Standardizing Gender Values (Markdown)

```markdown
## Standardizing Gender Values

Gender labels are normalized into consistent categories such as `"Male"` and `"Female"` to eliminate formatting inconsistencies.
```

## Your Code

```python
df['suspect_gender'] = df['suspect_gender'].replace({
    'm': 'Male',
    'M': 'Male',
    'f': 'Female',
    'F': 'Female'
})

df['suspect_gender'] = df['suspect_gender'].str.lower().str.title()


df['victim_gender'] = df['victim_gender'].replace({
    'm': 'Male',
    'M': 'Male',
    'f': 'Female',
    'F': 'Female'
})

df['victim_gender'] = df['victim_gender'].str.lower().str.title()
```

---

## Cell 16 — Formatting Phone Numbers (Markdown)

```markdown
## Formatting Phone Numbers

Phone numbers are reformatted into a consistent structure to improve readability and standardization.
```

## Your Code

```python
df['victim_phone'] = df['victim_phone'].str.replace('-', '')
df['victim_phone'] = df['victim_phone'].apply(lambda x: f'{x[0:3]}-{x[3:6]}-{x[6:]}' if x != 'Unknown' else x)
df
```

---

## Cell 17 — Standardizing Weapon Labels (Markdown)

```markdown
## Standardizing Weapon Labels

Weapon labels are converted into a consistent title-case format to improve categorical consistency.
```

## Your Code

```python
df['weapon_used'] = df['weapon_used'].str.lower().str.title()
df
```

---

## Cell 18 — Cleaning Severity Levels (Markdown)

```markdown
## Cleaning Severity Levels

Numeric severity codes are converted into readable categorical labels.
```

## Your Code

```python
df['severity'] = df['severity'].replace({
    '1': 'Low',
    '2': 'Medium',
    '3': 'High',
    '4': 'Critical'
})

df['severity'] = df['severity'].str.lower().str.title()
df
```

---

## Cell 19 — Standardizing Case Status (Markdown)

```markdown
## Standardizing Case Status

Case status values are normalized into a consistent text format.
```

## Your Code

```python
df['case_status'] = df['case_status'].str.lower().str.title()
df
```

---

## Cell 20 — Standardizing Resolution Labels (Markdown)

```markdown
## Standardizing Resolution Labels

Resolution values are cleaned and converted into a standardized title-case format.
```

## Your Code

```python
df['resolution'] = df['resolution'].str.lower().str.title()
df
```

---

## Cell 21 — Cleaning Online Reporting Values (Markdown)

```markdown
## Cleaning Online Reporting Values

Different representations of boolean values are converted into readable `"Yes"` and `"No"` categories.
```

## Your Code

```python
df['reported_online'] = df['reported_online'].fillna('No')

df['reported_online'] = df['reported_online'].str.lower().str.title()

df['reported_online'] = df['reported_online'].replace({
    'True': 'Yes',
    'False': 'No',
    '1': 'Yes',
    '0': 'No'
})

df
```

---

## Final Section — Project Conclusion (Markdown)

```markdown
# Project Conclusion

During this project:
- Missing values were handled
- Duplicate records were removed
- Categorical variables were standardized
- Text formatting inconsistencies were fixed
- Phone numbers were reformatted
- Overall data quality was improved

The dataset is now significantly cleaner and better prepared for exploratory data analysis and machine learning workflows.
```

