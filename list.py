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

# Assign a list of ten metal ores to a variable
metal_ores = ["hematite", "magnetite", "galena", "sphalerite", "pyrite", "chalcopyrite", "bornite", "malachite", "cassiterite", "wolframite"]

# Print the fourth element of the list
print("The fourth element of the list is:", metal_ores[3])

# Print the sixth through tenth element of the list
print("The sixth through tenth elements of the list are:", metal_ores[5:])

# Change the value of the seventh element to "My Precious"
metal_ores[6] = "My Precious"
print("The updated list is:", metal_ores)

# Append "uraninite" to the end of the list
metal_ores.append("uraninite")
print("After appending 'uraninite', the list is:", metal_ores)

# Clear the list
metal_ores.clear()
print("After clearing the list, the list is:", metal_ores)

# Create a copy of the original list
metal_ores = ["hematite", "magnetite", "galena", "sphalerite", "pyrite", "chalcopyrite", "bornite", "malachite", "cassiterite", "wolframite"]
metal_ores_copy = metal_ores.copy()
print("The copied list is:", metal_ores_copy)

# Count the number of occurrences of "pyrite" in the list
pyrite_count = metal_ores.count("pyrite")
print("The number of occurrences of 'pyrite' is:", pyrite_count)

# Extend the list with another list of metal ores
more_metal_ores = ["hemimorphite", "limonite"]
metal_ores.extend(more_metal_ores)
print("After extending the list with more metal ores, the list is:", metal_ores)

# Get the index of "malachite" in the list
malachite_index = metal_ores.index("malachite")
print("The index of 'malachite' is:", malachite_index)

# Insert "cinnabar" at index 3
metal_ores.insert(3, "cinnabar")
print("After inserting 'cinnabar', the list is:", metal_ores)

# Remove the last element of the list
last_element = metal_ores.pop()
print("The last element removed was:", last_element)
print("After removing the last element, the list is:", metal_ores)

# Remove the first occurrence of "hematite" from the list
metal_ores.remove("hematite")
print("After removing 'hematite', the list is:", metal_ores)

# Reverse the list
metal_ores.reverse()
print("After reversing the list, the list is:", metal_ores)

# Sort the list in alphabetical order
metal_ores.sort()
print("After sorting the list, the list is:", metal_ores)

# Create a tuple of three elements
my_tuple = ("Silver", 3, True)
print("The tuple is:", my_tuple)

# Create a set of four elements
my_set = {"Silver", "Bronze", "Steel", "MaryJane"}
print("The set is:", my_set)

# Create a dictionary with two key-value pairs
my_dict = {"name": "Scrups", "age": 7}
print("The dictionary is:", my_dict)


