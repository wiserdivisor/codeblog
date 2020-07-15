# if not using __name__=="__main__"
# export FLASK_APP=flaskblog.py
# then ` flask run `
# log on "localhost:5000"

# importing flask class.
from flask import Flask, render_template, url_for

# make app variable.
# set it to an instance of flask class.
# double underscore means name of module.
# if run in python direct...
# __name__ == __main__.
# so flask knows where to look for...
# templates and static files.
# this is instanciated flask application.
app = Flask(__name__)

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
def hello():
    return render_template("home.html", posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)
