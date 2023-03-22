# Script: Ops 301 ops chal-08
# Author: Justin H
# Date of latest revision: 3/22/23
# Purpose: Lists & Variables
# Team: Geneva, Nick, && Sierra


#!/usr/bin/env python3

# we start by creating a list of ten string elements, each representing a different metal ore.
# Print the fourth element of the list using its index (which is 3, since Python uses zero-based indexing)
# We print the sixth through tenth element of the list using slicing notation.
# Slice notation [5:10] means "start at the sixth element (index 5) and go up to, but not including, the tenth element (index 10-1=9)"
# We change the value of the seventh element (which has index 6) to "onion" using assignment, and then print the updated list to confirm that the change has been made.

# Assign a list of ores to a variable
metal_ores = ["gold", "silver", "copper", "iron", "zinc", "lead", "tin", "nickel", "aluminum", "mercury"]

# Print the fourth element of the list
print(metal_ores[3])

# Print the sixth through tenth element of the list
print(metal_ores[5:10])

# Change the value of the seventh element to "My Precious"
metal_ores[6] = "my precious"

# Print the updated list
print(metal_ores)


