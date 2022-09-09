#!/bin/bash

cd /home/ubuntu
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
