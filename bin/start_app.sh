#!/bin/bash
cd /src

echo ">>> Make migrations"
python manage.py makemigrations

echo ">>> Apply database migrations"
python manage.py migrate

echo ">>> Starting server"
gunicorn -c /src/gunicorn.conf.py memohub.wsgi:application
