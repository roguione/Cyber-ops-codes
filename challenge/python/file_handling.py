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
file_path = '/home/roguione/pfsense/myfile.txt'

# Create pfsense directory if it does not exist
if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))

# Open the file in append mode
with open(file_path, 'a') as f:
    # Write three lines to the file
    f.write('Get Off My Script.\n')
    f.write('eat an apple.\n')
    f.write('Lick a Lollipop.\n')

# Open the file in read mode
with open(file_path, 'r') as f:
    # Read the first line and print it to the screen
    first_line = f.readline()
    print(first_line)

# Delete the file
os.remove(file_path)
