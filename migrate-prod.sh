#!/usr/bin/env bash

export FLASK_CONFIG=production # may not need this...
/bin/python2.7 /opt/zillow_scraper/manage.py db upgrade
/bin/python2.7 /opt/zillow_scraper/manage.py db migrate
echo "DONE!"
