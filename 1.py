import pandas as pd

df = pd.read_csv('data/raw/crime_incidents_messy.csv')
print(df.head())

df = pd.read_csv('data/cleaned/cleaned_crime_dataset.csv')
print(df.head())