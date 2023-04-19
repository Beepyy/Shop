FROM python:3.8

WORKDIR /app
VOLUME .:usr/src/app
COPY . .

EXPOSE 8080:8080
CMD ["python manage.py makemigrations","python manage.py migrate","python manage.py runserver"]