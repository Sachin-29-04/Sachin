#ROCK, PAPER AND SCISSORS

player1=input("r for rock ,p for paper or s for scissors : ")
player2=input("r for rock ,p for paper or s for scissors : ")


print("Player 1 chose : ", player1)
print("Player 2 chose : ", player2)

if(player1==player2):
    print("It's a tie ")
elif(player1=="r")  :
    if(player2=="p"):
        print("Player 2 Wins")
    else :
        print("Player 1 wins")
elif (player1 == "p"):
    if (player2 == "s"):
        print("Player 2 Wins")
    else:
        print("Player 1 wins")
elif (player1 == "s"):
    if (player2 == "r"):
        print("Player 2 Wins")
    else:
        print("Player 1 wins")
else:
    print("invalid choice")