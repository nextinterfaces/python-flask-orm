# Flask Example Project

This project is a Python-based web application leveraging Flask, SQLAlchemy, and related technologies to manage and interact with data.

## Features

- Database integration using SQLAlchemy ORM.
- Flask framework for routing and server management.
- Modular project structure for easy extensibility.

---

## Project Structure

```plaintext
.venv/                 # Virtual environment directory
auth/                  # Sample module
static/                # Static assets (CSS, JS, images)
templates/             # HTML templates for the front-end

app-main.py            # Main entry point for the Flask application
app-orm.py             # Handles ORM logic with SQLAlchemy
app-sql.py             # Direct SQL-based queries and database interactions
models.py              # Database models defined with SQLAlchemy
requirements.txt       # List of dependencies
```

---

## Installation

Follow these steps to set up and run the project locally:


Solution 2: Install virtualenv via pipx

If you specifically want to use virtualenv, you can use pipx, which is Homebrew’s recommended way to manage Python applications.

Install pipx if this is brew managed python:

    brew install pipx

Ensure pipx is configured:

    pipx ensurepath

Install virtualenv using pipx:

    pipx install virtualenv

Create a virtual environment using virtualenv:

    virtualenv .venv

Activate the virtual environment:

    source .venv/bin/activate

    # or deactivate when done
    deactivate

Proceed to install packages (e.g., Flask):

    pip install -r requirements.txt
    pip list

Or install manually:

    pip install flask # etc
    pip freeze > requirements.txt
    pip list

Run the Main example:

    # Main example, navigate to http://127.0.0.1:5000
    export FLASK_APP=app.py FLASK_ENV=development && python3 app-main.py

Run the ORM example:

    # ORM example, GET http://127.0.0.1:5000/users
    # curl --location 'http://127.0.0.1:5000/users' --header 'Content-Type: application/json' --data-raw '{"username": "john_doe", "email": "john@example.com" }

    export FLASK_APP=app.py FLASK_ENV=development && python3 app-orm.py

Run the plain SQL example:

    # SQL example
    export FLASK_APP=app.py FLASK_ENV=development && python3 app-sql.py


Run `flask run` directly:

    # alternative, assuming there is existing app.py
    export FLASK_APP=app.py FLASK_ENV=development && flask run


Deployment

Deploy Flask apps using servers like Gunicorn or cloud platforms (AWS, GCP, etc.):

    gunicorn -w 4 app:app