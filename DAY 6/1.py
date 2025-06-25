
import pandas as pd


data_set={"Col1":range(3),"Col2":["A","B","C"],
                "date":(["2025-06-20","2025-06-21","2025-06-22"])}
df=pd.DataFrame(data_set)

print(df)

print(df["date"].dtype)

df["date"]=pd.to_datetime(df["date"])

print(df["date"].dtype)


df1=pd.Series(["2025-06-20","2025-06-21","2025-06-22"])

print(df1)

print(df1.dtype)

df1=pd.to_datetime(df1)
print(df1)