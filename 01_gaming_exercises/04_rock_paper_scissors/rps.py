# Rock, Paper, Scissors by Juwan Brunson v0.1

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
playerName = input("Please type your name and press enter.\n")
print(f"hello{playerName}!\n")
iscorrect = input("IS that correct? Type yes or no then press enter.\n").lower()

# .lower() can turn All input into lowercase.
# .lower() can turn All input into UPPERCASE.

if iscorrect == "yes":
    print(f"ok {playerName}, Lets play rock paper scissors!\n")
else:
    playerName = input("please type your name and press enter.\n")

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
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input("please enter rock, paper, or scissors and press enter\n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
            print("You are not following directions please try again.\n")
            exit()
        print(f"you have chosen {playerChoice}.\n")
    else:
        print(f"you have chosen {playerChoice}.\n")



    # let cpu select choice at random 
    # compare player choice to cpu choice
    # print the result to the screen
    # award point to winner and output result    
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to determine CPU choice. \nPlease restart.\n")
        exit()
    