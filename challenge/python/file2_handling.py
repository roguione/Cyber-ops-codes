# Script: Ops 301 ops chal-10
# Author: Justin H
# Date of latest revision: 3/24/23
# Purpose: File Handling
# Team: Geneva, Nick, && Sierra

# First set the file path to /home/roguione/pfsense/myfile.txt and create the directory if it does not exist using the os.makedirs function
# Open the file in append mode using the with open(file_path, 'a') as f statement and write three lines to the file using the f.write function
# open the file in read mode using the with open(file_path, 'r') as f statement and read the first line using the f.readline function
# Print the first line to the screen using the print function.
# We delete the file using the os.remove function


import os

# Set the file path
file_path = '/home/roguione/pfsense/hey.txt'

# Create the directory if it does not exist
if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))

# Create the file if it does not exist
if not os.path.exists(file_path):
    open(file_path, 'w').close()

# Open the file in write mode
with open(file_path, 'w') as f:
    # Write "Hey You" to the file
    f.write('Hey You\n')

# Open the file in read mode
with open(file_path, 'r') as f:
    # Read the first line and print it to the screen
    first_line = f.readline()
    print(first_line)

# Delete the file
os.remove(file_path)
