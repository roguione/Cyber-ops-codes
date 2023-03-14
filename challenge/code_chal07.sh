# !/bin/bash
# Justin H
# 14Feb23
# Main
# Display CPU information using lshw

echo "CPU: "
sudo lshw -short | grep -i processor | awk '{print }'
echo ""

# Display current CPU performance
echo "CPU: "
mpstat | awk '/all/{print "CPU usage: " }'
echo ""

# Display RAM information using lshw
echo "RAM : "
sudo lshw -short | grep -i memory | awk '{print }'
echo ""

# Display adapter
echo "display adapter"
lspci | grep -i vga | awk '{print }'
echo ""

# Network Adapter
echo "Network"
sudo lshw -short | grep -i network | awk '{print }'
echo ""