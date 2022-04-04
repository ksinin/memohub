#!/bin/bash
cd /src

echo ">>> Apply database migrations"
python manage.py migrate

echo ">>> Starting server"
gunicorn -c /src/gunicorn.conf.py memohub.wsgi:application
