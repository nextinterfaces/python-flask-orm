from flask import Flask
import os
from flask import request, jsonify
from flask import render_template

print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
print(f"FLASK_APP: {os.getenv('FLASK_APP')}")

app = Flask(__name__)
print(f"__name__: {__name__}")

@app.route('/')
def index():
    return "Hello, Flask!"

@app.route('/api/test')
def test1():
    return {'user': "asass"}

@app.route('/user/<username>')
def user(username):
    return f'Hello, {username}!'

@app.route('/greet', methods=['POST'])
def greet():
    data = request.json  # Parse JSON body
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'})  # JSON response

@app.route('/hello/<name>')
def hello(name):
    return render_template('index.html', title='Greeting Page', name=name)

@app.errorhandler(404)
def not_found(error):
    return "Page not found!", 404


from auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
