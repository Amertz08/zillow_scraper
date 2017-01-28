# Zillow Scraper
Scraper that grabs listing data off of Zillow

## To work on in virtual env

```bash
# assuming you are using virtualenvwrapper
$ mkvirtualenv zillow
(zillow)$ pip install -r requirements.txt
(zillow)$ mysql -u root -p
mysql> CREATE DATABASE zillow_scraper;
mysql> CREATE USER 'zillow'@'localhost' IDENTIFIED BY '<PASSWORD_FROM_CONFIG>';
mysql> GRANT ALL PRIVILENGES ON zillow_scraper.* TO 'zillow'@'localhost';
mysql> exit
(zillow)$ python manage.py creatdb
(zillow)$ python manage.py db init
# CHANGE PY_BASE_PATH in migrate-local.sh before running this command
(zillow)$ bash migrate-local.sh
(zillow)$ python manage.py runserver
# open browser to http://localhost:5000

# If you want to run the scraper against a particular city run the following
(zillow)$ scrapy crawl zillow -a city=CITY_NAME -a state=STATE_ABBREVIATION
```

## Testing
:laughing: