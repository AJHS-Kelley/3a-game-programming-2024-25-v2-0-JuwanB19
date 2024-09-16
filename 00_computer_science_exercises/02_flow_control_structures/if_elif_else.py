# Flow Control Structures, Juwan Brunson, v0.0
# Making Computer Programs Make Decisions

temperature = 57.5
color = "Green"
height = 10
likesPineappleOnPizza = False

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")
if height < 10:
    print("You're Short Bro. \n")
if likesPineappleOnPizza == False:
    print("Welcome to the club\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza: 
    print("yummy")

# What if we want something different to happen?
if color == "Green":
    print("Your shirt is the correct uniform color,\n")
else:
    print("Your shirt is not the correct uniform color.\n")

if height >= 7:
    print("Do you play basketball?\n")
else:
    print("You're shorts bud.\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride.

# when writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=
if height >= 3:
    print("you're tall enough to ride the hulk ride!\n")
elif height >= 6: 
    print("You're too tall bud\n")
else: # "oh, no, something's up. Height wrong do not ride."
    print("NOPE, height not right. Do not ride.\n")


# when writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3:
    print("you're not tall enough to ride the hulk ride!\n")
elif height < 6: 
    print("You're good big bro\n")
else: # "oh, no, something's up. Height wrong do not ride."
    print("NOPE, height not right. Do not ride.\n")

if temperature >= 100:
    print("its too hot outside\n")
elif temperature >=50:
    print("recess is allowed!\n")
elif temperature > 0:
    print("Recess is in the gym!\n")
else: # no temp
    print("wait not temperture detected\n")
