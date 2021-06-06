# Blog
A simple blog Application APIs. Users can create blog posts by creating an account or anonymously. Comments  can be anonymous also.

## Getting Started

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes. See deployment for notes
on how to deploy the project on a live system

## Prerequisites
* Python version 3.6 or 3.7 or 3.8
* Django 3.0.6 
* Optional - > Pycharm or robust IDE

## Installation
# Option 1 - Using Docker (Preferably)
1. Clone this repository
2. Download [Docker desktop](https://www.docker.com/products/docker-desktop) for windows and mac, for 
[linux](https://docs.docker.com/engine/install/)

3. create a .env file in the root project and ask for environment variables keys

4. Run ```docker-compose up --build ``` to get your application running

5. Open a new terminal and Run ```  docker-compose run --rm web manage.py migrate ``` to check for container name


6. Run ```docker-compose run --rm web manage.py createsuperuser``` to create superuser

# Option 2 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

1. clone this repository.

2. create a virtual environment with python 3.6 or 3.7 or 3.8 for the project
    * Click [here](https://docs.python.org/3/library/venv.html) to learn how to 
    create virtual environment for python project

3. Run the following command to install the packages in the requirements.

```bash
pip install -r requirements.txt
``` 
 or in case you are not using virtual environment and have multiple python versions installed.
```bash
pip3 install -r requirements.txt
```

* Once the requirements are installed, cd into the project directory where 'manage.py' resides.
* Set environment variables for Secret Key - Ask For Secret Key

* There is a sample ```.env``` file in the root called ```.env-example```.
You may use this to configure the project for your local development.

* Once settings configuration is completed, make and create migrations for database.

* Run the following commands

Make migrations
```bash
python manage.py makemigrations

```

Migrate with this command
```bash
python manage.py migrate

```

Start the server

If 'My Port' is not included, server starts at 8000

```bash
python manage.py runserver 'My Port'

```
## Error Handling
The API may return these error types when requests fail:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### Endpoints
##### GET  '/account'
    This endpoint fetches all the accounts in the database and displays them as json.

##### GET  '/post'
    This endpoint fetches all the posts in the database and displays them as json.

##### GET  '/comment'
    This endpoint fetches all the comments in the database and displays them as json.

##### GET  '/news'
    This endpoint fetches latest news based on these categories (technology, business') from a third-party API and displays them as json.

##### GET  '/account/<int:account_id>'
    This endpoint will get the account that corresponds to the account ID that is passed into the url based on the json that is passed into the body of the request.

##### GET  '/post/<int:post_id>'
    This endpoint will get the post that corresponds to the post ID that is passed into the url based on the json that is passed into the body of the request.

##### GET  '/comment/<int:comment_id>'
    This endpoint will get the comment that corresponds to the comment ID that is passed into the url based on the json that is passed into the body of the request.

##### POST '/account'
    This endpoint will create a new account in the database based on the json that is in the body of the request.

##### POST '/post'
    This endpoint will create a new post in the database based on the json that is in the body of the request.

##### POST '/comment'
    This endpoint will create a new comment in the database based on the json that is in the body of the request.

##### PATCH  '/account/<int:account_id>'
    This endpoint will modify the account that corresponds to the account ID that is passed into the url based on the json that is passed into the body of the request.

##### PATCH  '/post/<int:post_id>'
    This endpoint will modify the post that corresponds to the post ID that is passed into the url based on the json that is passed into the body of the request.

##### PATCH  '/comment/<int:comment_id>'
    This endpoint will modify the comment that corresponds to the comment ID that is passed into the url based on the json that is passed into the body of the request.

###### PUT  '/account/<int:account_id>'
    This endpoint will modify the account that corresponds to the account ID that is passed into the url based on the json that is passed into the body of the request.

##### PUT  '/post/<int:post_id>'
    This endpoint will modify the post that corresponds to the post ID that is passed into the url based on the json that is passed into the body of the request.

##### PUT  '/comment/<int:comment_id>'
    This endpoint will modify the comment that corresponds to the comment ID that is passed into the url based on the json that is passed into the body of the request.

##### DELETE  '/account/<int:account_id>'
    This endpoint will modify the account that corresponds to the account ID that is passed into the url based on the json that is passed into the body of the request.

##### DELETE  '/post/<int:post_id>'
    This endpoint will modify the post that corresponds to the post ID that is passed into the url based on the json that is passed into the body of the request.

##### DELETE  '/comment/<int:comment_id>'
    This endpoint will modify the comment that corresponds to the comment ID that is passed into the url based on the json that is passed into the body of the request.


## Testing
To run tests open a terminal and run ```python manage.py test``` or you can use the Pycharm Django Test Runner

## Production
Check out [deploying django to heroku](https://devcenter.heroku.com/articles/django-app-configuration) 


* Create 'Procfile' file in the root repository and add the following
```bash
release: python manage.py migrate

web: gunicorn ussdc2c.wsgi --log-file -
```

