from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .database import retrieve_user, new_user, login_manager
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
@login_required
def index():
        return redirect(url_for('home'))
                
@auth.route('/login', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
                return redirect(url_for('home.homepage'))
        if request.method == 'POST':
                user = retrieve_user(request.form['username'])
                if not user or not user.check_password(request.form['password']):
                        return render_template('login.html', error="Invalid username/password.")
                login_user(user)
                return redirect(url_for('home.homepage'))
        else:
                return render_template('login.html')

@auth.route('/signup', methods=['POST'])
def signup():
        failed_signup = False
        username = request.form['username']
        password = request.form['password']
        user = None

        if(username != ''):
                user = retrieve_user(request.form['username'])
        else:
                failed_signup = True
                flash("Username field must not be empty", 'error_signup')

        if(password == ''):
                failed_signup = True
                flash("Password field cannot be empty.", 'error_signup')

        if user:
                flash("User with that name already exists.", 'error_signup')
                failed_signup = True
        if request.form['password'] != request.form['confirm-password']:
                flash("Passwords do not match.", 'error_signup')

        if not failed_signup:
                new_user(request.form['username'], request.form['email'], request.form['password'])
                flash("Successful signup.", 'success_msg')
        
        return redirect(url_for('auth.login'))

@login_manager.unauthorized_handler
def login_required_redirect():
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


