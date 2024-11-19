#!/bin/bash

# Check if the script is being run with sudo
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root. Please use sudo."
  exit 1
fi

# Run the commands
./install.sh
./tweaks.sh -F
./install.sh -o normal -c Dark -t all
