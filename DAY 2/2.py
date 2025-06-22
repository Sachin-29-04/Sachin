# (2) In your last program where you find thr total marks and percentage of a students
#find grade of student using conditional statements

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

if percentage>=60:
    print("grade A")
elif percentage>=50 :
    print("grade B")
elif percentage>=40 :
    print("grade C")
elif percentage>=33 :
    print("grade D")
else :
    print("Fail")



