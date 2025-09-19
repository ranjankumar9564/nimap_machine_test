Nimap Machine Test - Django REST API

This project is a Django REST API for managing Clients and Projects with JWT authentication. PostgreSQL is used as the database.

How to Use

Clone the repository:
git clone https://github.com/ranjankumar9564/nimap_machine_test.git

Navigate to the project folder:
cd nimap_machine_test

Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

Install dependencies:
pip install -r requirements.txt

Configure PostgreSQL in settings.py

Run migrations:
python manage.py migrate

Start the server:
python manage.py runserver

API Endpoints

Get JWT Token: POST /api/token/

Create Client: POST /api/clients/

List Clients: GET /api/clients/

Retrieve/Update/Delete Client: GET/PUT/DELETE /api/clients/{id}/

Create Project for Client: POST /api/clients/{client_id}/projects/

List Projects for User: GET /api/projects/

Include JWT token in headers: Authorization: Bearer <token>

GitHub Repository

https://github.com/ranjankumar9564/nimap_machine_test