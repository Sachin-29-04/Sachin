
for x in range (1,10,2) :

     pass


for x in range (10,1,-2) :
      print(x)


n1=int(input("enter number"))
for x in range(1,11,1):
    if(x%2==0):
       continue
    print(n1,"*",x,"=",n1*x)


for x in range (1,5,1):
     for y in range(1,3,1) :
         print("ty")

     print(x)


for x in range (1,5,1):
      for y in range(1,3,1) :
          print(x,y)



for x in  range(2,5):
      for y in range (1,11,1) :
          print(x,"*",y,"=",x*y)


for x in range (0,10):
     for y in range( 1,x):
         print(y,end=" ")
     print()

i=1
while i <=5:
     print(i)
     i=i+1


while True :
     print()
     n=int(input("enter number and 0 to exit"))
     if n==0 :
          break
     print(n)

str="Python program"

print(str[0])
print(str[-2])

print(str[0:4])
print(str[-5:-1])
print(str[0::2])
print(str[-1::-1])

l=len(str)

for x in l :
  print(str)

print(ord("a"))
print(chr(97))

l=[10,20,"gg",40,[1,4,"h"]]
print(l)
print(type(l))

print(l[0])
print(l[4])
print(l[0:3])

ll=[10,60,40]
s=0
for x in ll:
    s+=x
    print(s)


m=0
for x in ll:
      if x>m :
         m=x

print(m)


for i in range(4,8):
    ll.append(i)

print(ll)


ll.insert(4,55)
print(ll)

ll.extend([20,30,69])
print(ll)

ll.pop()
print(ll)

ll.pop(0)
print(ll)


