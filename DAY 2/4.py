
# (4) Create a billing program using list

l=[]
while(True) :
      print(''' 
          1.Create bill
          2.Display item and Price 
          3.Display Total
          4.Exit
      ''')
      n = int(input("enter your choice : "))

      if(n==1):
          item=input("enter item : ")

          price=int(input("enter price : "))
          l.append([item,price])


      elif(n==2):
          for x in l :
              print("Item : ",x[0]," Price : ",x[1])

      elif(n==3):
          total=0
          for x in l:
              total+=x[1]

          print("Total amount : ",total)


      elif(n==4):
          break;
      else :
          print("invaild choice")

