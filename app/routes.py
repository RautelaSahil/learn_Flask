#here we will have all the routes/Urls for our application
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
#Decorators to define route for index page.
#both the above routes will point to this function.
def index():
    #mock user data
    user = {'username': 'Miguel'}
    posts = [
        {'author': {'username': 'John'} , 'body': 'Beautiful day in Portland!' },
        {'author': {'username': 'Susan'} , 'body': 'The Avengers movie was so cool!' }
    ]
    
    return render_template('index.html',user=user,posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In', form =form)
    