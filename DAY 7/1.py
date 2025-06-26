import pandas as pd


df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange', 'grape']})
print(df)

print("")

result = df[df['fruit'].str.contains('an')]
print(result)

print("")

result = df['fruit'].str.count('an')
print(result)

print("")

result = df[df['fruit'].str.match('a')]
print(result)

print("")

df1 = pd.DataFrame({'A': ['hello world', 'hii world']})
print(df1)
result1 = df1['A'].str.replace('world', 'friend')
print(result1)



