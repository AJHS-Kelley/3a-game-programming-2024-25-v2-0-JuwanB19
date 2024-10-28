#function practcie Juwan B v0.0

import random

language = input
def helloWorldMulti(): #funvtion signature
    """this function will output hello world! in a language the user choose. """ #docstring \
    #print a list of languages to the screen, atleast three but no more than 5
    print("""
          welcome pick a lanaguge
          [E]nglish
          [S]panish
          [F]rench
          """)
    #allow the user to select(input) a choice for language
    #print "hello world" to screen inm that language
    language = input ("pick a language.\n just type the first letter of your language\n").upper()

    if language == "E":
        print(f"hello world\n")
    elif language == "S":
        print(f"Hola Mundo\n")
    elif language == "F":
        print(f"Bonjour le monde\n")
    else:
        print(f"Y you dumb")

#helloWorldMulti() #function call

#function to determine even/odd
arugment1 = random.randint(-1000, 1000)

def isEven(arugment1: int)-> bool: #requires one argument return a boolean value
    """Will return either true or false"""
    if arugment1 % 2 == 0:
        return True
    else: 
        return False

#print(isEven(arugment1))

# function with multiple arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("you can ride\n")
        return True
    else:
        print("you can't ride\n")
        return False
    
canRideRollerCoaster(11,5) #arguments must be passed in the same order as the function signature indicates