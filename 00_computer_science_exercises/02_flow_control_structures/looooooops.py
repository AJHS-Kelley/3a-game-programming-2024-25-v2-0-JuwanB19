# Loops, Juwan Brunson, v0.0
import random # import the random module for us to use
# generally put all your import statements at the top

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# While <-- Used when you don't know how many loops you'll need

#for loop is like go fish, you search each card for what the player asked
# while loop is like musical chairs, you move around until the music stops

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a for loop

#for loop example -- Iterating a List
fruits = [ "grape", "apple", "banana", "lemon"]
for eachFruit in fruits:
    print(eachFruit)

# continue KeyWord -- Skips the current iteration and then finishes the loop
fruits = ["grape", "apple", "banana", "lemon"]
for eachFruit in fruits: 
    print(eachFruit)

 # continue KeyWord -- Skips the current iteration and then finishes the loop
fruits = ["grape", "apple", "banana", "lemon"]
for eachFruit in fruits: 
    if eachFruit == "banana":
        continue
    print(eachFruit)

# break keyword -- immediately exit the loop 
fruits = ["grape", "apple", "banana" "lemon"]
for eachFruit in fruits:
    if eachFruit == "banana":
        break
    print(eachFruit)
# # for loops using range (). range (x) is EXCLUSIVE, it starts at 0 and ends at x - 1 
# for i in range(10): # range is 0 - 9
#    print(i)
# # might not always want yo start at zero
# for i in range(10, 100): #
#    print(i)
    
# # sometimes You're not done writing the loops
# for x in range (10)
#    pass # tells phython this loop isn't finished, don't freak out
    
# while loops -- Musical Chairs
playerScore = 0
counter = 0 
while playerScore == 100:
# run as long as this is true
    print(f"starting: {playerScore}") 
