# (1) Create a CSV file for address book,CSV file should have column for name,address,mobile,email.

import csv


data = [
    ["Name", "Address", "Mobile No.", "Email"],
    ["Alex ford ", "Delhi, India", "9876543210", "alex.ford@gmail.com"],
    ["Peter Parker", "San franscisco, USA", "0123456789", "peter.parker@gmail.com"],
    ["Tony Stark", "New york, USA", "9999999999", "tony.stark@gmail.com"]
]


with open("data1.csv","w",newline="") as file1 :
    data1_writer=csv.writer(file1)

    for x in data:
        data1_writer.writerow(x)


with open("data1.csv","r",newline="") as file1:

    data1_reader=csv.reader(file1)

    for x in data1_reader:
        print(x)
