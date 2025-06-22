# (1) Write a python program that takes in a student name, class.
# It should also take in five subject marks of the students and find the total marks and percentage
# Display a result in such a way that their name, class and percentage are printed

name=input("Enter student name : ")

sclass=int(input("enter class : "))

print("marks are out of 100 in one subject")

sub1=int(input("enter marks of sub 1 : "))

sub2=int(input("enter marks of sub 2 : "))

sub3=int(input("enter marks of sub 3 : "))

sub4=int(input("enter marks of sub 4 : "))

sub5=int(input("enter marks of sub 5 : "))

totalmarks=sub1+sub2+sub3+sub4+sub5

percentage=(totalmarks/500)*100



print("Name  : ",name)

print("Class : ",sclass)

print("Total marks : ",totalmarks)

print("Percentage : ",percentage)
