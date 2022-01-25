print("Rock Paper Scissor Game")
print("Enter choice\n  1.Rock\n 2.Paper\n 3.Scissor")



print("Player 1")
choice1=int(input("Enter the choice"))
if(choice1==1):
    print("Your choice is rock")
elif(choice1==2):
    print("Your choice is paper")
elif(choice1==3):
    print("Your choice is scissor")
        
print("Player 2")
choice2=int(input("Enter the choice"))
if(choice2==1):
    print("Your choice is rock")
elif(choice2==2):
    print("Your choice is paper")
elif(choice2==3):
    print("Your choice is scissor")
    
if (choice1==choice2):
    print("Tie")
elif (choice1==1 and choice2==2) or (choice1==2  and choice2==3) or (choice1==3 and choice2==1) :
    print("Player 2 wins")
elif (choice1==2 and choice2==1) or (choice1==3 and choice2==2) or (choice1==1 and choice2==3) :
    print("Player 1 wins")


for i in range(1):
    print("Would you like to play again")
    ans=input() 
    if ans=='no':
        break
print("Thanks for playing" )