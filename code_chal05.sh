




#!/bin/bash

# Display a list of running processes
ps -eo pid,cmd

# Loop to prompt the user for a PID and kill the corresponding process
while true; do
    # Prompt the user for a PID
    read -p "Enter the PID of the process to kill (or 'q' to quit): " pid

    # Exit the loop if the user enters 'q'
    if [ "$pid" = "q" ]; then
        break
    fi

    # Attempt to kill the process with the specified PID
    if kill "$pid"; then
        echo "Killed process with PID $pid"
    else
        echo "No process found with PID $pid"
    fi
done
