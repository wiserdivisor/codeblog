# if not using __name__=="__main__"
# export FLASK_APP=flaskblog.py
# then ` flask run `
# log on "localhost:5000"

# importing flask class.
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

# make app variable.
# set it to an instance of flask class.
# double underscore means name of module.
# if run in python direct...
# __name__ == __main__.
# so flask knows where to look for...
# templates and static files.
# this is instanciated flask application.
app = Flask(__name__)
app.config['SECRET_KEY'] = '81e84b26ff8f1015428db0cc672fc862'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    image_file = db.Column(db.String(20), nullable=False, default = "default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{ self.username }','{ self.email }','{ self.image_file }')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{ self.title }','{ self.date_posted }')"



posts = [
    {
        'author' : "Vignesh Reddy",
        'title' : "Blog Post One",
        'content' : "First Post Content",
        'date_posted' : "July 10, 2020"
    },
    {
        'author' : "abc xyz",
        'title' : "Blog Post Two",
        'content' : "Second Post Content",
        'date_posted' : "July 10, 2020"
    },
]

# making a route.
# route is for going to diff pages.
# like ABOUT and CONTACT pages.
# do that with app.route decorators.
# decorators are for adding additional...
# functionality to existing functions.
@app.route("/") #homepage
@app.route("/home")
# function for this route
def home():
    return render_template("home.html", posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="admin@blog.com" and form.password.data=="somepass":
            flash("Login Successful!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful.", 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
