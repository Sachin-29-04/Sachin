import pandas as pd

data = {
    'A': ['2024-06-01', '2024-07-15', '2025-01-10'],
    'B': ['2025-06-25', '2025-06-20', '2025-06-26']
}

df = pd.DataFrame(data)
print(df)

df['A'] = pd.to_datetime(df['A'])
df['B'] = pd.to_datetime(df['B'])
print(df["A"].dtype)


df['year'] = df['A'].dt.year
df['month'] = df['A'].dt.month
df['day'] = df['A'].dt.day_name()


df['B-A'] = (df['B'] - df['A']).dt.days


df['C'] = df['B'] + pd.DateOffset(days=7)




print(df)