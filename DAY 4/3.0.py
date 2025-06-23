#Creation of database1
import sqlite3

conn=sqlite3.connect("database1.db")


#creation of Products Table
conn.execute('''
         CREATE TABLE Products (
         product_id INTEGER PRIMARY KEY AUTOINCREMENT,
         name VARCHAR(100),
         category VARCHAR(50),
         price INTEGER
)
      ''')

#creation of Users Table
conn.execute('''
    CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    email VARCHAR(100),
    signup_date DATE
)
''')
conn.close()
