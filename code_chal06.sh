#!/bin/bash

paths=("./home1" "./home2" "./home3" "./home4")

for path in "${paths[@]}"; do
  if [ ! -e "$path/file45.md" ]; then
    touch "$path/file45.md"
  else
    echo "$path/file45.md already exists"
  fi
done

# End