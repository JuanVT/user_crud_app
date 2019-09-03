# CRUD App

This application allows users to create, read, update and delete their profile information.

It has been built with Django and SQLite3 database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

To get this project up and running, please download or clone the repository and follow the following steps:

* Setup a virtualenv (for development tasks)

```
pip install virtualenv
virtualenv .venv 
. .venv/bin/activate
```

* Install Requirements:

See requirements.txt to get all requirements installed and run the following command (make sure your virtualenv is activated)

```
pip install -r requirements.txt
```

### Run migrations for the SQL DB models
```
python manage.py migrate
```
### Run the application
```
python manage.py runserver
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
