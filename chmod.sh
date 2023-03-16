# Script: Ops 301 ops chal-03
# Author: Justin H
# Date of latest revision: 3/15/23
# Purpose: File Permissions
# Team: Geneva, Nick, && Sierra

#  Script first checks if the hello.txt file exists in the /home/roguione/hello directory 
#  Using the -f option of the test command. 
#  If it doesn't exist, it creates the file with the content "Hello, world!".

#!/bin/bash

# Set the directory path
directory="/home/roguione/hello"

# Prompt the user for the permissions number
read -p "Enter permissions number: " permissions

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Error: Directory not found."
  exit 1
fi

# Navigate to the directory
cd "$directory" || exit 1

# Change permissions of all files inside the directory
chmod -R "$permissions" *

# Print the directory contents and permissions
echo "Directory contents and permissions:"
ls -l