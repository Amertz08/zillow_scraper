#!/usr/bin/env bash

export FLASK_CONFIG=default
export PY_BASE_PATH=/Users/adammertz/.virtualenvs/zillow
${PY_BASE_PATH}/bin/python manage.py db upgrade
${PY_BASE_PATH}/bin/python manage.py db migrate
echo "DONE"
