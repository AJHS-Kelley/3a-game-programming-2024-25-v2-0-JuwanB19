# Rock, Paper, Scissors by Juwan Brunson v3.0

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName = "Test player"
playerChoice = None

# DATA STRUCTRES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
def playerName(): #function signiature -- name of function (arugment)
    playerName = input("Please type your name and press enter.\n")
    print(f"hello{playerName}!\n")
    iscorrect = input("IS that correct? Type yes or no then press enter.\n").lower()

    # .lower() can turn All input into lowercase.
    # .lower() can turn All input into UPPERCASE.

    if iscorrect == "yes":
        print(f"ok {playerName}, Lets play rock paper scissors!\n")
    else:
        playerName = input("please type your name and press enter.\n")

#Calling the function
playerName()

# THE RULES using MULTI-LINE STRINGS
print(f"""
welcome, {playerName} to the rock, paper, scissors robot! 
It's Time To play rock, paper, scissors!

you will play against the cpu. the first player to score 5 points wins.end
you will select from ROCK, PAPER, or SCISSORS.
the cpu will select from ROCK, PAPER, or SCISSORS at random.

1) Rock beats scissors
2) scissors beats paper
3) paper beats rock
""")

# MUlTI_ LINES STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quote is just ignored.
If you need to write large comments, it's easier to use multii- line strings than 
putting a # in front of 15 diffenet lines.
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input("please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("please enter rock, paper, or scissors and press enter\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions please try again.\n")
            exit()
        print(f"you have chosen {playerChoice}.\n")
    else:
        print(f"you have chosen {playerChoice}.\n")

    # let cpu select choice at random 
    cpuChoice = random.randint(0,2) # randomly setect 0,1 or 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = " scissors"
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to determine cpu choice.\nPlease restart.\n")
        exit()
    # print(f"cpu choice: {cpuchoice}")
        
    # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        #cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point.\n")
        cpuScore += 1
    elif playerChoice == "rock" and cpuChoice == "scissors":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        playerScore += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("cpu wins a point.\n")
        cpuScore += 1
    elif playerChoice == "scissors" and cpuChoice == "paper":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("cpu wins a point.\n")
        cpuScore += 1
    else:
        print("unable to determine restart.\n")
        exit()   


    print(f"your final score: {playerScore}\ncpu final score: {cpuScore}\n")
    if playerScore > cpuScore:
        print(f"congrats {playerName} you won")
    elif cpuScore > playerScore:
        print(f"the cpu won, you suck")
    else:
        print("unable to determine winner.\n restart.\n")
        exit()