#!/bin/bash

set -e

source /env/bin/activate

python3 project/manage.py migrate


python3 /app/project/manage.py collectstatic --noinput


PORT=${PORT:-1000}

if [ "$1" = "gunicorn" ]; then

    exec gunicorn project.wsgi:application -b 0.0.0.0:$PORT

else
    exec python3 project/manage.py runserver 0.0.0.0:$PORT


fi

