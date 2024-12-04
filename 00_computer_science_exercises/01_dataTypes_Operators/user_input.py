# User Input practice, Ryan Kelley, v0.0

# input() is the built-in function to get information from the keyboard
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!

# INCORECT, CAUSES A CONCATENATION ERROR
# myNumber = input("Please type an INTEGER number and press enter.\n")
# print(myNumber + 5)

# CORRECT -- Use a wrapper
myNumber = int(input("Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will covert the data to an INTEGER if possible
newNumber = input("please type a value anbd press enter. \n")
print(int(newNumber)) # can convert STRING to INTEGER
print(float(newNumber)) # can convert STRING to FLOAT
print(str(newNumber)) # can convert INTEGER to STRING

# float() will convert the data to a FLOAT if possible
newNumber = input("please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot convert FLOAT to INTEGER
print(float(newNumber)) # can convert STRING to FLOAT
print(str(newNumber)) # can convert FLOAT to STRING

# str() will convert the data to a STRING if possible
newnumber = 5
print(newNumber + newNumber) # should print 10
print(str(newNumber = newNumber)) # should print 5

