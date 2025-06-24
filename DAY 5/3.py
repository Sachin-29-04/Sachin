#data iteration

import pandas as pd

data_set=[[1,"Alex",21],[2,"Ben",20],[3,"Chris",19],[4,"Dwayne",18]]

df=pd.DataFrame(data_set,columns=["ID","Name","Age"],index=["P1","P2","P3","P4"])
print(df)


condition1=df["Age"]>=20
print(condition1)
print(df[condition1])

print(df["Name"])

print(df.iloc[0])
print(df.iloc[3])

print(df.iloc[0:2])
print(df.iloc[2:4,0:2])

drop1=df[df["ID"]!=3]
print(drop1)

drop2=df.drop("P2")
print(df)


inser1=df.iloc[0:1,0:1]=[111]
print(df)

list1=df["Name"].tolist()
print(list1)
print(type(list1))