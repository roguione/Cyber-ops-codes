#!/bin/bash
# Justin - Sierra, Geneva, Nick A
# 03/14/23

#Varibles
source_path="/var/log/syslog"
dest_path=$(pwd)

#Set Filename to today's date
filename=$(date +"%Y-%m-%d")

#Copy
cp "$source_path" "$dest_path/$filename"



