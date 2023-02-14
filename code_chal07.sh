#!/bin/bash

# Main

# Display CPU information using lshw
echo "CPU: "
sudo lshw -short | grep -i processor | awk '{print }'
echo ""

# Display current CPU performance
echo "CPU: "
mpstat | awk '/all/{print "CPU usage: " 100-$NF"%"}'
echo ""

# Display RAM information using lshw
echo "RAM : "
sudo lshw -short | grep -i memory | awk '{print }'
echo ""

# Display current RAM performance
echo "RAM Performance:"
free -m | awk 'NR==2{printf "Used Memory: %sMB/%sMB (%.2f%%)\n", $3, $2, $3*100/$2 }'
echo ""

# End
