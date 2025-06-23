#insertion of data in database1


import sqlite3

conn = sqlite3.connect("database1.db")

#insertion of data in Products Table
conn.execute('''
       
 INSERT INTO Products(name,category,price) VALUES
( 'Laptop', 'Electronics', 70000),
( 'Keyboard', 'Electronics', 2000),
( 'Note Book', 'Stationery', 200),
( 'Pen', 'Stationery', 10);

''')

conn.commit()

#insertion of data in Users Table
conn.execute('''
       
INSERT INTO Users(name,email,signup_date) VALUES
( 'A', 'aaaa@gmail.com', '2024-01-01'),
( 'B', 'bbbb@gmail.com', '2024-02-02'),
( 'C', 'cccc@gmail.com', '2024-03-03'),
( 'D', 'dddd@gmail.com', '2024-04-04');

''')

conn.commit()

conn.close()