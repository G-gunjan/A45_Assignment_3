# Flask and Django Docker Application

This project demonstrates a containerized web application setup using both Flask and Django frameworks. The application consists of two separate services that run simultaneously:

Flask Application: A simple web app that handles user input (name and age) and displays personalized greetings.
Django Application: A task management system that allows users to create, view, and delete items through a web interface.

##  Prerequisites

Ensure the following are installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)
- [Jenkins](https://www.jenkins.io/)

## Project Structure

```
A3_45_ASSIGNMENT_3/
│
├── django_app/                           
│   ├── django_app/                    
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── product/                           
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── db.sqlite3
│   ├── manage.py
│   ├── Dockerfile                         
│   └── requirements.txt                   
│
├── flask_app/                             
│   ├── static/
│   ├── templates/
│   ├── env/                               
│   ├── app.py
│   ├── Dockerfile                         
│   └── requirements.txt                  
│
├── docker-compose.yml                     
├── Jenkinsfile                            
└── requirements.txt                       

```

## Quick Start

**Clone the Repository**

```bash
git clone https://github.com/G-gunjan/A45_Assignment_3.git
cd A45_Assignment3
```
```
docker-compose up --build
```
**Access the Applications**
*Flask App: http://localhost:5000

*Django App: http://localhost:8000

*Django Admin: http://localhost:8000/admins
**Create a Django Superuser**
```
docker-compose run django_app python manage.py createsuperuser
```
**Links**
* GitHub Repo: https://github.com/G-gunjan/A45_Assignment_3.git

* Docker Hub - Django App: https://hub.docker.com/repository/docker/gunjanpandya/django_app/general

*Docker Hub - Flask App: https://hub.docker.com/repository/docker/gunjanpandya/flask_app/general

**Features**
 **Flask Application**
*Homepage with a greeting

*Form to collect user name and age

*Personalized greeting on submission

*CSRF protection and form validation


**Django Application**
*Homepage lists all items

*Add new items via form

*Delete items

*Admin interface to manage products

*SQLite for data persistence
**Docker Configuration**
The project uses Docker Compose to manage two containers:

**Flask Container**
*Python 3.10

*Flask + WTForms

*Development server on port 5000

Django Container
*Python 3.10

*Django + SQLite

*Development server on port 8000

**Environment Variables**
*Flask App
*FLASK_ENV: development
*FLASK_DEBUG: 1
*SECRET_KEY: Custom secret key for security
*PYTHONUNBUFFERED: 1
*Django App
*DEBUG: 1
*PYTHONUNBUFFERED: 1
**Development**
To make changes to the application:

*The code is mounted as volumes, so changes will reflect immediately
*Both applications have debug mode enabled for development
*Auto-reload is enabled for both services
**Production Deployment**
**For production deployment:**

*Change debug settings to False
*Use proper secret keys
*Configure proper database settings for Django
*Use production-grade servers instead of development servers
*Docker Hub Images
**The Docker images are available at:**

*Flask App: https://hub.docker.com/repository/docker/gunjanpandya/flask_app/general
*Django App: https://hub.docker.com/repository/docker/gunjanpandya/django_app/general

