# Script: Ops 301 ops chal-08
# Author: Justin H
# Date of latest revision: 3/22/23
# Purpose: Python Conditonals
# Team: Geneva, Nick, && Sierra


# This is a Python script that prompts the user to enter four numbers a, b, c, and d
# Then performs some logical operations on them using if-else statements.

a = "2 dogs"   # Assign "2 dogs" to the variable a
b = "1 cat"   # Assign "1 cat" to the variable b
c = "5 humans" # Assign "5 humans" to the variable c
d = "3 apes"   # Assign "3 apes" to the variable d

# Check if b is greater than a
if b > a:
    print("b is greater than a")

# Check if a and b are equal   
elif a == b:
    print("A and B are equal")

# If neither of the above conditions are true, then a is greater than b    
else:
    print("A is greater than B")

# Check if c is less than or equal to d
if c <= d:
    print("C is lesser than /equal to D")
    
 # If c is not less than or equal to d, then it must be greater than d   
else:
    print("C is greater than / equal to D")
    
# Check if d is not equal to c
if d != c:
    print("C is not equal to D")

# This explains how Human are not equal to Ape
print("This explains how Human are not equal to Ape")