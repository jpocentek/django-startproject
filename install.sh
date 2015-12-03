#!/bin/bash
#
# Run `install.sh -d` to include development dependencies.

debug=0
projectname=""

while getopts "d?:f:" opt; do
    case $opt in
    d\?)
        debug=1;;
    f)
        projectname=$OPTARG;;
    esac
done

if [ -f replace_names.py ]; then
    mv startproject $projectname
    python replace_names.py $projectname
    rm replace_names.py
fi

python setup.py develop
pip install -r requirements.txt

if [ $debug -eq "1" ]
then
    pip install -r requirements_dev.txt
fi
