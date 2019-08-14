from flask import render_template, flash, redirect, url_for, flash
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Brian Musyoki',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 10th 2019'
    },

    {
        'author': 'Nancy Mumina',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 21st 2019'
    },

    {
        'author': 'Thomas Mumina',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'August 21st 2019'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', data=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='ABout Bruh!')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data } !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@andela.com' and form.password.data == 'admin':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful please check username and password', 'danger')
    return render_template('login.html', title='LogIn', form=form)