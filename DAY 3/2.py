# (2) Write a function for basic math operations

def operation(num1,num2) :
      sum =num1 + num2
      print("Addition of num 1 an num2 is = ",sum)

      sub = num1 - num2
      print("Subtraction of num 1 an num2 is = ", sub)

      mul = num1 * num2
      print("Multiplication of num 1 an num2 is = ", mul)

      div = num1 / num2
      print("Division of num 1 an num2 is = ", div)



num1=int(input("enter num1 "))
num2=int(input("enter num2 "))
operation(num1,num2)