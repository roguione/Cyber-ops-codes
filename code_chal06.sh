#!/bin/bash
# Script: Ops 201 Class 04 Ops Challenge Solution
# Author: Justin H
# Date of latest revision: 2/13/23
# Purpose: Conditionals

# Team: Geneva && Sierra

# Main

paths=("./home1" "./home2" "./home3" "./home4")

for path in "${paths[@]}"; do
  if [ ! -e "$path/file45.md" ]; then
    touch "$path/file45.md"
  else
    echo "$path/file45.md already exists"
  fi
done

# End