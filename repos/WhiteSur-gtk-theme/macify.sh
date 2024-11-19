#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <Dark/Light> <color>"
  exit 1
fi

# Assign the arguments to variables
foo1=$1
foo2=$2

# Run the command with the provided parameters
./install.sh -l -o normal -c "$foo1" -t "$foo2"
