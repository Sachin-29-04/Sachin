#Updation of data in database1


import sqlite3

conn=sqlite3.connect("database1.db")


# entry ( 'Note Book', 'Stationery', 200) is Updated  (name ->'Note Book' to 'Book') and (price->200 to 400)
data=conn.execute("SELECT * FROM Products")

for x in data:
    print(x)

conn.execute("UPDATE Products set name='Book',price=400 where product_id=3")
conn.commit()

print("")

data = conn.execute("Select * FROM Products")
for x in data:
    print(x)

print("")



# entry ( 'B', 'bbbb@gmail.com', '2024-02-02'), is Updated  (name ->'B' to 'E') and (email->'bbbb@gmail.com' to 'eeee@gmail.com')


data1=conn.execute("SELECT * FROM Users")

for y in data1:
    print(y)

print("")

conn.execute("UPDATE Users set name='E',email='eeee@gmail.com' where user_id=2")
conn.commit()


data1= conn.execute("Select * FROM Users")
for y in data1:
    print(y)

conn.close()