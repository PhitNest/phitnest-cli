#!/bin/bash

cd $(dirname $0)

pyinstaller --onefile --icon=icon.ico --name=phitnest src/phitnest.py

# Check the exit status of the pyinstaller command
if [ $? -ne 0 ]; then
    echo "==============================="
    echo " F A I L E D   T O   B U I L D "
    echo "==============================="
    exit 1
fi

echo "====================================="
echo " S U C C E S S F U L L Y   B U I L T "
echo "====================================="