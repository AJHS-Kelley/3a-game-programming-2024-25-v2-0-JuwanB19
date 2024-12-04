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
def playerName()->str: #function signiature -- name of function (arugment)
    """gets name of player and returns it """
    #the line above is a docstring gives breif example about what a function does
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
def rules()->None:
    """this function peints rules of rps"""
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

def playerChoice()->str:
    """allows player to chose rock paper scissors"""
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

def cpuChoice()->str:
    """allows cpu to chose rock paper scissors"""
    cpuChoice = random.randint(0,2) # randomly setect 0,1 or 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "scissors"
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to determine cpu choice.\nPlease restart.\n")
        exit()
    return cpuChoice

def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    # compare player choice to cpu choice
    print(f"playerChoice {playerChoice}")
    print(f"cpuChoice {cpuChoice}")
    if playerChoice == "rock" and cpuChoice == "paper":
        #cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point.\n")
        #cpuScore += 1
    elif playerChoice == "rock" and cpuChoice == "scissors":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        #playerScore += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("cpu wins a point.\n")
        #cpuScore += 1
    elif playerChoice == "scissors" and cpuChoice == "paper":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        #playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        #playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("cpu wins a point.\n")
        #cpuScore += 1
    else:
        print("unable to determine restart.\n")
        exit()   

def score(winner: str) -> int:
    """This function uses the winner to update the score for CPU, Num. DRAWS, and player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1
    else: # This is a DRAW.
        score = 0
    return score

def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """This function determines if a player has won the game or not by scoring 5 points."""
    if playerScore >= 5:
        print("Congratulations! You are the winner.\n")
        return True
    elif cpuScore >= 5:
        print("Sadly, you have been defeated by the CPU.\n")
        return True
    else: # No winner yet.
        return False

def playGame(playerScore: int, cpuScore: int) -> None:
    """This function will use all other functions to play Rock, Paper, Scissors. """
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player Wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"Player Score: {playerScore}\n")
        print(f"CPU Score: {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)