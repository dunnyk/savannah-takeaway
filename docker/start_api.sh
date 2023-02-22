#!/bin/bash

export $(grep -v '^#' .env.docker | xargs)


echo $CURRENT_UID
# pipenv shell
echo "<<<<<<<<<< Export LANG to the Env>>>>>>>>>>"
echo ' '
echo ' '

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"
echo ' '
echo ' '
sleep 15
# Run database migrations
python manage.py migrate

echo ' '
echo ' '
sleep 5
echo "<<<<<<< Database Setup and Migrations Complete >>>>>>>>>>"
echo " "
echo ' '
echo "<<<<<<< Collecting static files >>>>>>>>>>"
echo ' '
yes | python manage.py collectstatic --noinput


echo ' '
echo ' '
sleep 5
echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
echo ' '
echo ' '

# Start the API with gunicorn
gunicorn --bind 0.0.0.0:8000 savannahTest.wsgi --reload --access-logfile '-' --workers 2