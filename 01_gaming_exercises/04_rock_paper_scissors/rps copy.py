# Rock, Paper, Scissors by Juwan Brunson v0.1

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCTRES -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("how many loops do you want?\nenter an integer an integer, no commas, and press enter\n"))
# req is th euniversal abbreviation in computer programming for REQUEST reqs= requests
rpsTimeStart = time.time() #returns seconds since jan 01 1970 @ 12am
while loopCount < loopsReq:

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
        
    # let player choice at random
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
        numDraws += 1
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
        numDraws += 1
    elif playerChoice == "paper" and cpuChoice == "rock":
        #player wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("you win a point.\n")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        #draw
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("its a draw.\n")
        numDraws += 1
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # cpu wins
        print(f"the cpu chose {cpuChoice} and you chose {playerChoice}.\n")
        print("cpu wins a point.\n")
        cpuScore += 1
    else:
        print("unable to determine restart.\n")
        exit()
    loopCount += 1

    
    
    print(f"your final score: {playerScore}\ncpu final score: {cpuScore}\n {numDraws}\n")
if playerScore > cpuScore:
        print(f"congratsyou won")
elif cpuScore > playerScore:
        print(f"the cpu won, you suck")
else:
        print("unable to determine winner.\n restart.\n")
        exit()

rpsTimeStart = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"number of loops: {loopCount}\n")
print(f"Execution time {rpsTime:.2F} seconds\n"):.2F formats 
