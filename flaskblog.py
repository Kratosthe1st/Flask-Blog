from flask import Flask, render_template,flash,redirect,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ddd13bc2073648c445cad7dabca3ea42'

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


if __name__ == '__main__':
    app.run(debug=True)
