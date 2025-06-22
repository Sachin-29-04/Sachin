# (2) Input 2 strings concatinate them and store in another variable.
#  then perform generally used string methods on it

str1=input("enter the 1 string : ")
str2=input("enter the 2 string : ")

str3 = str1 +" " + str2

print(str1)
print(str2)
print(str3)

print(len(str1))
print(len(str2))
print(len(str3))

print(str3.lower())

print(str3.upper())

print(str3.capitalize())

print(str3.endswith("world"))

print(str3.find("o"))

print(str3.count("l"))

print(str3.title())

print(str3.swapcase())

print(str3.join("----"))

print(str3.isnumeric())
print(str1.isnumeric())

print(str3.isalpha())
print(str2.isalpha())

print(str3.index("l"))

