from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9e976f13bef0ef86a3414c2bffa8711'

posts = [
    {
        'author': 'Javier Estraviz',
        'title': 'Hello World!',
        'content': 'This is the content corresponding to my first post',
        'date_posted': 'February 14, 2019'
    },
    {
        'author': 'Javier Estraviz',
        'title': 'Second Post',
        'content': 'This is the content corresponding to my 2nd post',
        'date_posted': 'February 15, 2019'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
