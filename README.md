## Safe-Space-Group-Project-Backend

This is the backend for a blog application built with Flask, SQLAlchemy, and Alembic for database migrations. It includes user authentication, blog creation, and tagging features.

## 📁 Project Structure

.
├── README.md
└── server
├── Pipfile # Python dependencies
├── Pipfile.lock
├── alembic/ # Alembic migrations (legacy or alternative to 'migrations/')
├── alembic.ini # Alembic configuration
├── app.db # SQLite database file
├── app.py # Flask app entry point
├── config.py # Configuration settings
├── migrations/ # Alembic-generated migration scripts
├── models.py # SQLAlchemy models for User, Blog, and Tag
└── seed.py # Script for populating the database with sample data



## Setup Instructions

1. Clone the Repository
git clone git@github.com:Jjumaaa/Safe-Space-Group-Project-Backend.git
cd Safe-Space-Group-Project-Backend/server

2. Create and Activate Virtual Environment

pipenv install
pipenv shell

3. Run Database Migrations

flask db upgrade
If you haven’t initialized migrations yet:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

4. Seed the Database

python seed.py
 ## Running the App

flask run
By default, the app runs on:
http://127.0.0.1:5000/

## Features
User registration with secure password hashing

Blog creation and assignment to users

Blog tagging using many-to-many relationships

Alembic-based database migrations

Seed script with realistic fake data (via Faker)

 ## Technologies Used
Python 3.8+

Flask

SQLAlchemy

Flask-Migrate (Alembic)

Flask-Bcrypt

Faker

## Authors
Primrose 
Cristina
