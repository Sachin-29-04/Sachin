# (3) factorial
n=int(input("enter number "))

fact=1

for x in range (n,0,-1) :
    
    fact*=x

print(f"Factorial of {n} is",fact)