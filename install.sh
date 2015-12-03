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

if [ -f the_maker.py ]; then
    mv doubledjango $projectname
    python the_maker.py $projectname
    rm the_maker.py
fi

python setup.py develop
pip install -r requirements.txt

if [ $debug -eq "1" ]
then
    pip install -r requirements_dev.txt
fi
