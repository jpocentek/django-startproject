#!/bin/bash
#
# Run ``run.sh -d`` to start development server.

HOST="0.0.0.0"
PORT="9999"
PROJECT_NAME="doubledjango"

# echo "Starting Celery workers"
# python ./scripts/manage.py celery worker -E -B -l info -f \
#     ./logs/celery.log &>/dev/null &
#
# echo "Starting Celery management application"
# python ./scripts/manage.py celerycam &>/dev/null &

debug=0

while getopts "d?:" opt; do
    case $opt in
    d|\?)
        debug=1
    esac
done

if [ $debug -eq "1" ]
then
    echo "Starting development server on $HOST:$PORT. Please wait..."
    python ./scripts/manage.py runserver $HOST:$PORT
else
    echo "Starting uwsgi process"
    uwsgi --ini ./$PROJECT_NAME/uwsgi.ini &>/dev/null &
fi
