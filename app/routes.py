"""Routes handle the different URLs that the application supports.

Handlers for the app routes are written as Python functions called *view functions*
View functions are mapped to one or more route URLs so Flask knows what logic to
execute when a client requests a given URL
"""

from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


# Home page route
@app.route("/")
@app.route("/index")
def index() -> str:
    """Return index page."""
    user = {"username": "Miguel"}

    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!",
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!",
        },
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}",
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)


"""
Decorator pattern: use decorators to register functions as callbacks for certain events
Here, @app.route decorator creates an association between the URL given as an argument
 and the function
When web browser requests a URL ('/' or '/index'), Flask will invoke this function and
 pass its return value back to the browser as a response
"""
