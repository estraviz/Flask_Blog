from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
