# Series
import pandas as pd


data=["Alex","Tony","Peter","Ben"]

s=pd.Series(data)

print(s)
print(s[1])



data1={1:"A",2:"B",3:"C",4:"D"}

s1=pd.Series(data1)
print(s1)
print(s1[2])



data2={"A":100,"B":200,"C":300,"D":400}

s2=pd.Series(data2,dtype=float)
print(s2)
print(s2["B"])


