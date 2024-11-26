from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/login')
def login():
    return render_template('index.html', title='Greeting Page', name='aaaaaa')
    # return 'qeqeqwe' # render_template('login.html', title="Login Page")
