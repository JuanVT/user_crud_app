# CRUD App

This application allows users to create, read, update and delete their profile information.

It has been built with Django.

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
### Set up .env
I've used python decouple in this project in order to hide all secrets and keys. For you to be able to run this project you need to create a .env and use the following format:  

```
SECRET_KEY = MySecretKey
DEBUG = BooleanValue
SOCIAL_AUTH_GITHUB_KEY = MyGithubKey
SOCIAL_AUTH_GITHUB_SECRET = MySocialAuthGithubKey
```
For simplicity, I'll provide the real github key and secret for you to be able to value the exercise, but the real aim of using python decouple is to hide these and to not push sensible data in the repository:  

* SOCIAL_AUTH_GITHUB_KEY = b397842d8a80244e2690
* SOCIAL_AUTH_GITHUB_SECRET = fb54db87341eaec8aa5efde5eb033cea2259a48a   

Click [here](https://pypi.org/project/python-decouple/) for more info about python-decouple.

### Run the application
```
python manage.py runserver
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
