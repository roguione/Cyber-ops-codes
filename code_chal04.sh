#!/bin/bash

# Script: Ops 201 Class 04 Ops Challenge Solution
# Author: Justin H
# Date of latest revision: 2/9/23
# Purpose: Print a string to the terminal

# Team: Geneva && Sierra

# Main

mkdir home1 home2 home3 home4

path_array=("./home1/" "./home2/" ",/home3/" ",/home/")

touch ${path_array[0]}file1.sh 
touch ${path_array[1]}file2.sh
touch ${path_array[2]}file2.sh
touch ${path_array[3]}file3.sh

# End