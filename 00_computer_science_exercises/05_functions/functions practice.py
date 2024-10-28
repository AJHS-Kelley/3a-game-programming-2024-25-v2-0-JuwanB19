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
    language = input ("pick a language.\n just type the first letter of your language\n").lower()

    if language == "E":
        print(f"hello world"\n)
    elif language == "S"
        print(f"Hola Mundo"\n)
    elif language == "F"
        print(f"Bonjour le monde"\n)
    else
        print(f"Y you dumb")