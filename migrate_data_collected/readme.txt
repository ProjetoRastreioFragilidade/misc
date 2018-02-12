For create database and migrate data collected make:

mysql> CREATE DATABASE ppsus CHARACTER SET UTF8;
mysql> CREATE USER ppsus@localhost IDENTIFIED BY 'rede243';
mysql> GRANT ALL PRIVILEGES ON ppsus.* TO ppsus@localhost;
mysql> FLUSH PRIVILEGES;

$ python migrate_data.py
$ cd ../backend
$ python manage.py makemigrations ppsus_app
$ python manage.py migrate
$ python manage.py createsuperuser