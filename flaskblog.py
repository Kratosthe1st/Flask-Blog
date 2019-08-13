from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
