#deletion of data in database1



import sqlite3

conn=sqlite3.connect("database1.db")

# entry  ( 'Keyboard', 'Electronics', 2000) is deleted where product_id =2

data = conn.execute("Select * FROM Products")
for x in data:
    print(x)

print("")
pid=input("Enter Product id to delete product : ")


conn.execute("DELETE FROM Products where product_id ="+pid)
conn.commit()


data = conn.execute("Select * FROM Products")
for x in data:
    print(x)

print("")



# enter ('C', 'cccc@gmail.com', '2024-03-03') is deleted where user_id=2

data1=conn.execute("Select * FROM Users")
for y in data1 :
     print(y)

print("")
uid=input("enter User id to delete information : ")

conn.execute("DELETE FROM Users where user_id ="+uid)
conn.commit()

data1=conn.execute("Select * FROM Users")
for y in data1 :
     print(y)


conn.close()