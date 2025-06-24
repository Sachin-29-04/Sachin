#Dataframe

import pandas as pd

data_set=[[1,"Alex",21],[2,"Ben",20],[3,"Chris",19],[4,"Dwayne",18]]

df=pd.DataFrame(data_set,columns=["ID","Name","Age"])
print(df)

df=pd.DataFrame(data_set,columns=["ID","Name","Age"],index=["P1","P2","P3","P4"])
print(df)


data_set1={
    "ID":[101,102,103,104],
    "Name":["A","B","C","D"],
    "Age":[21,20,19,18]
}

df1=pd.DataFrame(data_set1)
print(df1)
df1=pd.DataFrame(data_set1,index=[11,22,33,44])
print(df1)


data_set2=[[1,"Apple",50],[2,"Banana",40],[3,"Cherry",30]]

df2=pd.DataFrame(data_set2,columns=["Q","Fruit","Price"],index=["R1","R2","R3"])
print(df2)


data_set3=[(1,"Laptop",70000),(2,"Keyboard",2000),(3,"Mouse",1000)]

df3=pd.DataFrame(data_set3,columns=["No.","Device","Price"],index=["R1","R2","R3"])
print(df3)


data_set4=[{"Name":"S","Branch":"IT"},
          {"Name":"A","Branch":"AI"},
          {"Name":"B","Branch":"DS"},
          {"Name":"C","Branch":"CS"}
            
            ]

df4=pd.DataFrame(data_set4)
print(df4)
