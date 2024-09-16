# awarding extra lives Juwan Brunson v0.0


lives = 3 

#Allow user to input score AS AN INTEGER

# If score is 10000 or less
    #lose a life
#if score is > 10000  but less than 100001
    #give 1 extra life
# if score is > 100000
    #give 2 extra lives 

# output the score and number of lives to the screen

playerScore = int(input("Please enter your score\n"))
playerName = "Juwan"

if playerScore <= 10000:
    print(f"wsp {playerName}! you scored {playerScore} points and you lost a life\n")
    print(lives - 1)
elif playerScore  < 100001:
    print(f"wsp {playerName}! you scored {playerScore} points and you get 1 extra life")
    print(lives + 1)
else:
    print(f"wsp {playerName}! you scored {playerScore} points and you get 2 extra lives\n")
    print(lives + 2)

    