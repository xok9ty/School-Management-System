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
- **Responsive Forms**: User-friendly forms with validation.
- **Password Reset**: Secure password reset via email.

## Models

- **Teacher**: Stores teacher information (name, contact details, etc.)
- **Student**: Stores student information (name, class, contact details, etc.)
- **Subject**: Stores subject information with teacher assignment
- **Class**: Stores class information with student assignments

## Usage
1. Login with your credentials or register a new account.
2. Navigate through the dashboard to manage different entities.
3. Use the respective sections to add, edit, or delete:
  - Teachers
  - Students
  - Subjects
  - Classes

## Password Reset
If you forget your password:
  1. Click on "Forgot password" link
  2. Enter your email address
  3. Check your email for reset instructions
  4. Follow the link to set a new password

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
   venv/bin/activate  # On MacOS use `source venv\Scripts\activate`
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
