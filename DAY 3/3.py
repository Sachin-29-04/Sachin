# (3)To check a number is palindrome or not


def palindrome(num) :
         ans=0
         rev=num
         while(rev!=0) :
              rem=rev%10
              ans=ans*10+rem
              rev=rev//10

         if(ans==num):
             print("number is palindrome")
         else :
             print("not a palindrome")



palindrome(12321)
palindrome(12345)
palindrome(4567654)


