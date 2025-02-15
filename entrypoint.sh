#!/bin/bash

set -e

source /env/bin/activate

if [$1 == 'gunicorn']; then

    exec gunicorn project.project.wsgi:application -b 0.0.0.0:8000

else
    exec python3 project/manage.py runserver 0.0.0.0:8000 

fi