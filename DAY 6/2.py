import pandas as pd


df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [90, 80, 70]})


result = df1.merge(df2, on='ID', how='inner')
print(result)

#left join
result=df1.merge(df2,on="ID",how="left")
print(result)

result=df2.merge(df1,on="ID",how="left")
print(result)

#right join
result=df1.merge(df2,on="ID",how="right")
print(result)

result=df2.merge(df1,on="ID",how="right")
print(result)


#index based join
result=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(result)

result=df2.join(df1,lsuffix="_left",rsuffix="_right")
print(result)


