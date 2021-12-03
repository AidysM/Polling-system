# Local
## PostgreSQL
sudo apt install postgresql postgresql-contrib

sudo -u postgres psql postgres

create user polls with password 'polls';

alter role polls set client_encoding to 'utf8';

alter role polls set default_transaction_isolation to 'read committed';

alter role polls set timezone to 'UTC';

create database polls_db owner polls;

\q

## Git
git clone https://github.com/AidysM/Polling-system.git

## Polling System
cd Polling_system/

pipenv install -r requirements.txt

pipenv shell

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

## Browser
http://127.0.0.1:8000

http://127.0.0.1:8000/admin/


# Docker
## Docker-ce
sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

sudo apt update

apt-cache policy docker-ce

sudo apt install docker-ce

sudo systemctl status docker

sudo usermod -aG docker ${USER}

su - ${USER}

id -nG

sudo usermod -aG docker username

## Git
git clone https://github.com/AidysM/Polling-system.git

## Polling System
cd Polling_system/

docker-compose up -d --build

docker-compose exec db psql --username=polls --dbname=polls_dev

\l

\q

docker volume inspect polling_system_postgres_data

chmod +x app/entrypoint.sh

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate --noinput

docker-compose exec web python manage.py createsuperuser

docker-compose logs -f

## Browser
http://127.0.0.1:8000

http://127.0.0.1:8000/admin/
