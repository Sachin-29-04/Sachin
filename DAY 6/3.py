import pandas as pd


df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'A': [9, 10], 'B': [11, 12]})


df4 = pd.concat([df1, df2, df3], ignore_index=True)

print(df4)

result=df4.merge(df3,on="A")
print(result)

result=df3.merge(df4,on="B")
print(result)

result=df4.join(df3,lsuffix="_left",rsuffix="_right")
print(result)