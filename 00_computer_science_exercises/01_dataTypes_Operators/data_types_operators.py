# Data Types and operators, Juwan Brunson, v0.0

# fundamental Data Types
# String- str - sequence of letters, numbers, spaces, or other characters
#string in python are in ' ' or " "

# Boolean- bool- True or False values.

# Float- float- any number value with a decimal, +/- and 0

# Intergers - int- any number +/- and 0

# Data Types are stored in VARIABLES
# A variable is basiclly a bucket with a name to put data into.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED IN IT 
# VARIABLES CAN NOT START WITH A NUMBER
# camelCaseVariableNames
# snake_case_variable_names

# DECLEARING VARIABLE AND ASSIGNING VALUES

highScore = 1000 # int data type 

carSpeed = 9.575 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data type

player = "Juwan Brunson" #string data type
enemyType = "fire" # string data type

# ASSIGN NEW VALUES
playerName = "John Cena"
carSpeed = 7.90

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0




# Printing Data types
newInt = 5
newFloat = 7.6
newString = "Quandale Dingle"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

# printing Variables to Console / Screen
print(playerName)
print(isPurple)
print(highScore)
print(carSpeed)

#printing variables and expressions to console / screen
print(highScore + 500)
print(4*12)
print(highScore)

# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {playerName}. Your high score is {highScore}.\n")

# Comparison Operators

# IS-EQUAL-TO == Are the two vaules equal to each other?
# Returns True or False based on evaluation
x = 12.0
#print(x == 5)

#NOT-EQUAL-TO != Are the two values NOT equal? 
# Returns True or False based on evaluation
print(x != 12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
print(5 > 3) #Greater Than
print(12 >= 2) #Greater Than or Equal To

# LESS THAN / lESS-THAN-OR-EQUAL TO
print(5 < 3) #Less Than
print(12 <= 2) #Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 17
height = 65.4
eyeColor = "Brown"
#In order to ride the Teacups, you must be at least 18 years old and at least 60" tall
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "Brown")
#ALWAYS CHECK FOR THE LEAST-LIKELY TO BE False CONDITION FIRST!!!!!
#print(defeatedBoss == True and level > 5 and hasBlueKey == True)

# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 or height >= 60)
print(age >= 18 or height >= 60 and eyeColor == "Brown")
#print(defeatedBoss == False or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT

a = 5
print(a == 5)
print(not (not (a == 5)))

# COMBINING LOGICAL OPERATORS
#print(a == 5 and hasKey == True or isCloud == True)
#TRUE and 

# IDENTITY OPERATORS 
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

#MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato") in fruits