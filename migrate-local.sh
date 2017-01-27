#!/usr/bin/env bash

export FLASK_CONFIG=default
python manage.py db upgrade
python manage.py db migrate
echo "DONE"
