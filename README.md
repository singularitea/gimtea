# gimtea - map branch

install PostgreSQL

	$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

login to PostgreSQL client

	$ sudo -u postgres psql

   	 postgresql=# CREATE DATABASE liveedu;

   	 postgresql=#  CREATE USER root WITH PASSWORD 'Thisisit2002';

  	  postgresql=#  ALTER ROLE root SET client_encoding TO 'utf8';

 	   postgresql=#  ALTER ROLE root SET default_transaction_isolation TO 'read committed';

   	 postgresql=#  ALTER ROLE root SET timezone TO 'UTC';

  	  postgresql=# \q



create virtual environment and activate

	$ virtualenv venv

	$ source venv/bin/activate



install Django and psycopg2

	$ pip install django psycopg2


Create project

	$ django-admin startproject gimtea


Create app

	$ python manage.py startapp instruments


Edit models.py to create tables


add app to settings file


migrate DB

python manage.py makemigrations

python manage.py migrate



Make database migrations

	$ python manage.py makemigrations

	$ python manage.py migrate



Create database admin

	$ python manage.py createsuperuser

ben

ben80085


Test server

	$ python manage.py runserver


127.0.0.1:8000/admin
