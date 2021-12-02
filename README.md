# PostgreSQL
sudo apt install postgresql postgresql-contrib

sudo -u postgres psql postgres

create user polls with password 'polls';

alter role polls set client_encoding to 'utf8';

alter role polls set default_transaction_isolation to 'read committed';

alter role polls set timezone to 'UTC';

create database polls_db owner polls;

\q

# Git
git clone https://github.com/AidysM/Polling-system.git

# Polling System
cd Polling_system/

pipenv install -r requirements.txt

pipenv shell

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

# Browser
http://127.0.0.1:8000

http://127.0.0.1:8000/admin/
