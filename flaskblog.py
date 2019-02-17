from flask import Flask, render_template, url_for, flash, redirect
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
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # simulating successful access; temporary password condition
        if form.email.data == 'admin@blog.com' and \
           form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password',
                  'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
