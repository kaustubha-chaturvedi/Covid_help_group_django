# tabler icons classes at /icons

## steps to connect to db

1. Setup mysql
1. Create Database named 'ichg'
1. makemigrations
1. migrate

## 3

custom user model created
fixed signup,signin,signout
created foundation for whole backend

## to reconfigure acording to project
drop database ichg;
create database ichg;
py ./manage.py makemigrations
py ./manage.py migrate