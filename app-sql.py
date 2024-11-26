from flask import Flask, request, g, render_template, redirect, url_for
import sqlite3
from jinja2 import DictLoader

# Configuration
DATABASE = 'users.db'

# Create Flask app
app = Flask(__name__)

# Add HTML templates to Jinja2 loader
app.jinja_loader = DictLoader({
    'index.html': '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>User List</title>
    </head>
    <body>
        <h1>User List</h1>
        <a href="/add">Add User</a>
        <ul>
            {% for user in users %}
                <li>{{ user[1] }} (Age: {{ user[2] }}) - <a href="/delete/{{ user[0] }}">Delete</a></li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''',
    'add.html': '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add User</title>
    </head>
    <body>
        <h1>Add User</h1>
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="number" name="age"><br>
            <input type="submit" value="Add User">
        </form>
    </body>
    </html>
    '''
})

# Function to get database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close database connection
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Execute SQL script for schema creation (called on app startup)
@app.before_request
def initialize_database():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    db.commit()

# Route to list users
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('index.html', users=users)

# Route to add a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

# Route to delete a user
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    return redirect(url_for('index'))

# Teardown - close database after each request
@app.teardown_appcontext
def teardown_db(exception):
    close_connection(exception)

if __name__ == '__main__':
    # Run Flask application
    app.run(debug=True)
