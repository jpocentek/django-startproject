#!/bin/bash
#
# Run `install.sh -d` to include development dependencies.

python setup.py develop

pip install -r requirements.txt

debug=0

while getopts "d?:" opt; do
    case $opt in
    d|\?)
        debug=1
    esac
done

if [ $debug -eq "1" ]
then
    pip install -r requirements_dev.txt
fi
