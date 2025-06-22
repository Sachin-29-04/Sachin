#ROCK, PAPER AND SCISSORS (random choice)

set1={"r","p","s"}
list2=["p","s","r"]

list1=list(set1)

i=int(input("enter 0 ,1 or 2 : "))
player1=list1[i]
j=int(input("enter 0 ,1 or 2 : "))
player2=list2[j]


print("Player 1 chose : ", player1)
print("Player 2 chose : ", player2)

if(player1==player2):
    print("It's a tie ")
elif(player1=="r" )  :
    if(player2=="p"):
        print("Player 2 Wins")
    else :
        print("Player 1 wins")
elif (player1 == "p" ):
    if (player2 == "s"):
        print("Player 2 Wins")
    else:
        print("Player 1 wins")
elif (player1 == "s" ):
    if (player2 == "r"):
        print("Player 2 Wins")
    else:
        print("Player 1 wins")
else:
    print("invalid choice")