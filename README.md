# 🏫School Management System

A Django-based web application for managing teachers, students, subjects, and classes in a school environment.

## Requirements

* Python
* HTML
* CSS
* Django
* Bootstrap

## Features

- **User Authentication**: Login, registration, and password reset functionality.
- **Dashboard**: Overview with counts of teachers, students, subjects, and classes.
- **CRUD Operations**:
  - Teachers management
  - Students management
  - Subjects management
  - Classes management

## Installation

1. Install the required libraries:
   ```
   pip install django
   ```
   
2. Clone the repository:
   ```
   git clone https://github.com/xok9ty/dj_project.git
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   # Windows use `venv\Scripts\activate`
   # MacOS use `source venv\Scripts\activate`
   ```

4. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the applicatoin at http://127.0.0.1:8000/
