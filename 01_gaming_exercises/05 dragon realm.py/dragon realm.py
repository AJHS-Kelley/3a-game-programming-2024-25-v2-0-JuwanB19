# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# You have made some progress but need to finish! 

import random
import time
import datetime
location = input
thingy = input

#saving data to a file
#step 1 create the file name to use
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# Just use "dragonRealmLog.txt"
#example: dragonrealm1132am.txt

#step 2 create / open the file to save the data
saveData = open(logFileName, "a") 
#file modes
#x creates file if file exist exit with error message
#w creates file if file exist erase and rewrite file contents
#a creates file if file exist append data to the file

saveData.write("GAME STARTED" +" " +str(datetime.datetime.now())+"\n")

def displayIntro():

    print('You have a map. In front of you,')
    print('you see the forest and the desert. ')
    print('you hope to find treasure and a cave is a great place to look')
    print('but you have to be able to fight enemys')
    print()

def lookingAtMap():
    print('you look down at the map while trying to decide where to go')
    print('pick the forest or the desert f or d')

def chooseArea():
    """choose whether the cave is in the forest or desert"""
    location = input() # You're missing the () for input.  This code also does not print anything to the screen to tell the player what to choose.    
    if location == "[f]orest":
        print('on the way to the forest you see some caves')
    elif location == "[d]esert":
        print('on the way to the desert you see some caves')
    else:
        print("smh")
    return location
        
def pickup():

    print('you need something to carry with you for your adhd')
    print('you either get a blastgun or pipebomb')
    print()

def adhdCure():

    if thingy == "[b]lastgun":
        print('you burnt you hand')
    elif thingy == "[p]ipebomb":
        print('you blew your arm off')
    else:
        print("you suffer from adhd")
    return adhdCure

def caveChoice():
    """ takes the location choosen and while otw to it you see caves"""
def walkToArea():
    print(f'while going to the {location}\n you see 2 caves')
    print('cave 1 is big cave 2 is small pick one')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    lookingAtMap()
    areaChosen = chooseArea()
    walkToArea()
    adhdCure()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

#close the file
saveData.write("END OF GAME LOG\n\n")
saveData.close()