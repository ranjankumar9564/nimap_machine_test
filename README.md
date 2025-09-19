Nimap Machine Test - Django REST API

This project is a Django-based REST API for managing Users, Clients, and Projects. It allows registering clients, assigning projects to users, and fetching relevant information. PostgreSQL is used as the database.

Features

User authentication with JWT token

Register, view, update, and delete clients

Create projects and assign them to registered users

Retrieve all projects assigned to the logged-in user

All API endpoints are secured and require authentication

Tech Stack

Python 3.x

Django 5.x

Django REST Framework

PostgreSQL

JWT Authentication

Setup Instructions
1. Clone the Repository

git clone https://github.com/ranjankumar9564/nimap_machine_test.git

cd nimap_machine_test

2. Create Virtual Environment and Install Dependencies

python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt

3. Configure Database

Create a PostgreSQL database

Update settings.py with your database credentials:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'your_db_name',
'USER': 'your_db_user',
'PASSWORD': 'your_db_password',
'HOST': 'localhost',
'PORT': '5432',
}
}

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Create Superuser

python manage.py createsuperuser

6. Run the Server

python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/

API Endpoints

Obtain JWT Token: POST /api/token/

Refresh JWT Token: POST /api/token/refresh/

Clients:

List all: GET /api/clients/

Create: POST /api/clients/

Retrieve/Update/Delete: GET/PUT/DELETE /api/clients/<id>/

Projects:

Create for a client: POST /api/clients/<client_id>/projects/

List assigned projects: GET /api/projects/

Notes

Make sure to use registered users when assigning projects

JWT token is required to access all endpoints

Follow the correct JSON structure when sending requests