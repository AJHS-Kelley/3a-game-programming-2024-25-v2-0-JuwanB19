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
    if iscorrect == "yes":
        print(f"ok {playerName}, Lets play rock paper scissors!\n")
    else:
        playerName = input("please type your name and press enter.\n")
    return playerName
#Calling the function
playerName = playerName()

# THE RULES using MULTI-LINE STRINGS
def rules():
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
    #does another part of this program need to access this info
    #if yes must have a return
    #if no a return statement is not required

def playerChoice():
    playerChoice = input("please enter rock, paper, or scissors and press enter\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("please enter rock, paper, or scissors and press enter\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions please try again.\n")
            exit()
        print(f"you have chosen {playerChoice}.\n")
    else:
        print(f"you have chosen {playerChoice}.\n")
    return playerChoice

def cpuChoice():
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
    return cpuChoice
# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    
    # let cpu select choice at random 
    
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