# 🧹 Messy Crime Dataset Cleaning Project

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458.svg)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Data Cleaning](https://img.shields.io/badge/Focus-Data%20Cleaning-red.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## 📌 Project Overview

This project focuses on **data cleaning and preprocessing** of a real-world messy dataset containing crime records.  
The dataset was intentionally designed with inconsistencies, missing values, duplicates, and formatting issues to simulate real-world data challenges.

The main goal was to transform raw, unstructured data into a **clean, analysis-ready dataset** suitable for exploratory data analysis (EDA) and machine learning tasks.

Dataset source:  
https://www.kaggle.com/datasets/sananshaikh/messy-crime-dataset-for-data-cleaning-practice

---

## 🎯 Objectives

- Identify and handle missing values
- Remove duplicate records
- Standardize inconsistent categorical values
- Fix data type issues (dates, numbers, strings)
- Clean and normalize text fields
- Prepare dataset for further analysis (EDA / ML-ready format)

---

## 🛠️ Tools & Technologies

- Python 🐍
- Pandas
- NumPy
- Jupyter Notebook

---

## 📊 Dataset Description

The dataset contains crime incident records with the following typical issues:

- Missing or null values in multiple columns  
- Duplicate entries  
- Inconsistent formatting (capitalization, spelling variations)  
- Mixed data types in numeric and categorical columns  

The dataset simulates real-world data quality problems commonly found in public safety and reporting systems.

---

## 🔧 Data Cleaning Steps

### 1. Data Loading & Inspection
- Loaded dataset using Pandas
- Checked structure using `.info()` and `.describe()`
- Identified missing values and duplicates

### 2. Handling Missing Values
- Removed or imputed missing entries depending on column importance
- Ensured consistency across key fields

### 3. Removing Duplicates
- Detected duplicate rows
- Removed redundant records to ensure data integrity

### 4. Standardization
- Unified categorical values (e.g., "male", "m", "MALE" → "Male")
- Fixed inconsistent text formatting

### 5. Text Cleaning
- Removed unnecessary whitespace and special characters
- Normalized string values for consistency

---

## 📈 Results

After cleaning:

- Dataset became fully structured and consistent
- Missing values significantly reduced or handled
- Duplicate rows removed
- Data types standardized
- Dataset ready for EDA and further analysis

## 🔄 Before / After Data Cleaning

One of the key parts of this project is demonstrating the **impact of data cleaning** on raw messy data.

### 📥 Before Cleaning (Raw Dataset)

The original dataset contained multiple issues:

- ❌ Missing values across important columns  
- ❌ Duplicate rows  
- ❌ Inconsistent text formatting (e.g. "male", "Male", "MALE")  
- ❌ Mixed data types in numeric fields  
- ❌ Unstructured and inconsistent date formats  
- ❌ Extra spaces and special characters in text fields  

Example (raw data snapshot):

| victim_gender | victim_phone | weapon_used | severity | case_status | resolution | num_arrests | property_loss_usd | reported_online |
|---------------|--------------|-------------|----------|-------------|------------|-------------|-------------------|-----------------|
| Unknown | 6223265920 | Firearm | 2 | Open | No Arrest | NaN | NaN | True |
| NaN | 241-973-4826 | Firearm | 3 | NaN | NaN | 2.0 | 44839.49 | yes |
| Other | 244-584-7696 | KNIFE | 1 | CLOSED | warning | 2.0 | 15963.38 | YES |
| NaN | 5021227484 | hands | Low | Resolved | NaN | 5.0 | 48680.14 | False |
| M | 9698766873 | Unarmed | MEDIUM | Closed | Warning Issued | 2.0 | 23513.01 | YES |

---

### 📤 After Cleaning (Processed Dataset)

After preprocessing, the dataset became:

- ✅ No duplicate rows  
- ✅ Missing values handled (removed or imputed)  
- ✅ Standardized categorical values  
- ✅ Correct data types across all columns  
- ✅ Normalized text fields  

---

### 📊 Impact Summary

| Metric | Before | After |
|--------|--------|-------|
| Missing values | High | Reduced / handled |
| Duplicates | Present | Removed |
| Data consistency | Low | High |
| Analysis readiness | ❌ Not usable | ✅ Fully ready |

---

### 💡 Key Insight

This step clearly shows that **data cleaning is not just preprocessing — it directly determines whether data is usable for analysis or ML models.**

---

## 📁 Project Structure
```
├───data
│   ├───cleaned
│   │   └───cleaned_crime_dataset.csv
│   └───raw
│       └───crime_incidents_messy.csv
├───notebooks
│   ├───data_cleaning.ipynb
│   └───.ipynb_checkpoints
├───screenshots
├── README.md
└── requirements.txt
```

---

## 💡 Key Learnings

- Real-world datasets are often messy and require extensive preprocessing
- Data cleaning is a critical step before any meaningful analysis
- Pandas provides powerful tools for handling inconsistent data efficiently
- Attention to detail significantly improves dataset quality

---

## 🚀 Future Improvements

- Add automated data validation checks
- Perform exploratory data analysis (EDA)
- Build a simple dashboard for crime trends
- Extend pipeline into a reusable data cleaning module

---

## 📌 Author

Ali (compuser21) — Aspiring Data Analyst / ML Engineer  
Focus: Data Analysis, Machine Learning, and Real-world Data Projects

---

## 📎 Dataset Source

- Kaggle: Messy Crime Dataset for Data Cleaning Practice  
https://www.kaggle.com/datasets/sananshaikh/messy-crime-dataset-for-data-cleaning-practice
