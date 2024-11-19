#!/bin/bash

# Help message
function helpm {
	echo "Usage:  [-h]"
	echo
	echo "Just let the helper assist you :)"
}

# If help argument is passed
if [[ "$1" == "-h" ]]; then
    helpm
    exit 0
fi

# foo1 takes accent color parameter
echo "[default|purple|pink|red|orange|yellow|green|teal|grey|all]"
echo "Enter the accent color:  "
read foo1

# foo2 takes theme color parameter
echo "[standard|light|dark]"
echo "Enter the theme color: "
read foo2

# foo3 takes any tweaks
echo "[nord|dracula|gruvbox|everforest|catppuccin|all|black|rimless|normal|float]"
echo "Enter tweaks (leave empty if none desired): "
read foo3

# First, we delete any installed files for a clean directory
./install.sh -r

# Next, we install the theme again with the specified parameters
if [[ -z "$foo3" ]]; then
    ./install.sh -t "$foo1" -c "$foo2" -l 
else
    ./install.sh -t "$foo1" -c "$foo2" -l --tweaks $foo3
fi
