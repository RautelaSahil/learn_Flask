#here we will have all the routes/Urls for our application
from app import app,db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
#Decorators to define route for index page.
#both the above routes will point to this function.
def index():
    #mock user data
    user = {'username': 'Miguel'}
    posts = [
        {'author': {'username': 'John'} , 'body': 'Beautiful day in Portland!' },
        {'author': {'username': 'Susan'} , 'body': 'The Avengers movie was so cool!' }
    ]
    
    return render_template('index.html',title = "Home",posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login():
    #current_user is provided by flask login to check if user is authenticated
    if current_user.is_authenticated:
        # If user is already logged in, redirect to index
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Query the user by username
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        # Check if user exists and password is correct
        if user is None or not user.check_password(form.password.data):
            # Invalid login attempt
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # Log the user in
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        # Security check for next_page
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html',title='Sign In', form =form)


@app.route('/logout')
def logout():
    logout_user()
    # Redirect to index page after logout
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)