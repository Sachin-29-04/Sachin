import pandas as pd

df=pd.read_csv("leads-100.csv")

print(df)
print(df.to_string())

print(df.head(10))

print(df.info())

print(df.describe())

print(df.shape)

print(df.columns)

print(df.isna().sum())


df = df.drop(columns=['Phone 2', 'Email 2', 'Notes'])

df['Website'] = df['Website'].fillna('No Website')


df['Full Name'] = df['First Name'] + ' ' + df['Last Name']

print(df['Deal Stage'].value_counts())

print(df)

print(df.to_string())