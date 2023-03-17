# Script: Ops 301 ops chal-03
# Author: Justin H
# Date of latest revision: 3/15/23
# Purpose: Conditionals
# Team: Geneva, Nick, && Sierra

#!/bin/bash

while true
do
    echo "Menu Options:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read -p "Enter your choice [1-4]: " choice

    if [ $choice == "1" ]
    then
        echo "Hello world!"
    elif [ $choice == "2" ]
    then
        ping 127.0.0.1
    elif [ $choice == "3" ]
    then
        ifconfig
    elif [ $choice == "4" ]
    then
        echo "Exiting..."
        exit 0
    else
        echo "Invalid choice. Please enter a number between 1 and 4."
    fi
done
