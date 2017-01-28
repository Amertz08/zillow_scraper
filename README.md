# Zillow Scraper
Scraper that grabs listing data off of Zillow

## To work on in virtual env

Create the virtual environment and install requirements.

```bash
# assuming you are using virtualenvwrapper
$ mkvirtualenv zillow
(zillow)$ pip install -r requirements.txt
(zillow)$ mysql -u root -p
```

Run the following MySQL commands

```sql
CREATE DATABASE zillow_dev;
CREATE USER 'zillow'@'localhost' IDENTIFIED BY '<PASSWORD_FROM_CONFIG>';
GRANT ALL PRIVILENGES ON zillow_dev.* TO 'zillow'@'localhost';
```

Then run the following bash commands to finalize the database setup

```bash
(zillow)$ python manage.py creatdb
(zillow)$ python manage.py db init
# CHANGE PY_BASE_PATH in migrate-local.sh before running this command
(zillow)$ bash migrate-local.sh
(zillow)$ python manage.py runserver
# open browser to http://localhost:5000
```

To run the scraper against a specific city run the following command. Both arguments are required.

```bash
(zillow)$ scrapy crawl zillow -a city=CITY_NAME -a state=STATE_ABBREVIATION
```

## Testing

The following command will run the full test suite.

```bash
(zillow)$ python manage.py test
```

In order for this to work properly you must follow the following mysql commands to create the proper db.
```sql
CREATE DATABASE zillow_test;
GRANT ALL PRIVILEGES ON zillow_test.* TO 'zillow'@'localhost';
```
