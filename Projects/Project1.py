import random

num = random.randrange(-1, 2)
print(num)

gamedic = {
    -1:"stone",
    0:"paper",
    1:"scissors"
}

choice = input("Choose any one in \"Stone,Papper and Scissors\": ")

print("Your choice: ",choice)
print("Compuer choice: ",gamedic[num])

if(gamedic[num]==choice.lower()):
    print("Draw the match.")

elif (gamedic[num]=="stone" and choice.lower()=="paper"):
    print("You wins!")

elif (gamedic[num]=="stone" and choice.lower()=="scissors"):
    print("Computer wins!")

elif (gamedic[num]=="scissors" and choice.lower()=="paper"):
    print("Computer wins!")

elif (gamedic[num]=="scissors" and choice.lower()=="stone"):
    print("You wins!")

elif (gamedic[num]=="paper" and choice.lower()=="scissors"):
    print("You wins!")

elif (gamedic[num]=="paper" and choice.lower()=="stone"):
    print("Computer wins!")

else:
    print("Any thing is wrong.")