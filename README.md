# Django Todo App

Welcome to the Django Todo App! This application allows users to manage their tasks with basic CRUD (Create, Read, Update, Delete) operations. It's built using Django, a high-level web framework for Python.

## Features

- **Create** new todo items
- **Read** and view existing todo items
- **Update** todo items
- **Delete** todo items

## Prerequisites

Make sure you have the following installed:

- Python 3.6+
- pip (Python package installer)
- Django 3.0+ (included in requirements)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vaishnavi2206/Django-Todo-App.git
   cd django-todo-app

2. **Create a virtual environment **
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4. **Run database migrations:**
  ```bash
  python manage.py migrate

5.  **Run the application:**

  ```bash
  python manage.py runserver
