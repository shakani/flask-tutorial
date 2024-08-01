"""Routes handle the different URLs that the application supports.

Handlers for the app routes are written as Python functions called *view functions*
View functions are mapped to one or more route URLs so Flask knows what logic to
execute when a client requests a given URL
"""

import sqlalchemy as sa
from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user

from app import app, db
from app.forms import LoginForm
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('idnex'))
    return render_template("login.html", title="Sign In", form=form)


"""
Decorator pattern: use decorators to register functions as callbacks for certain events
Here, @app.route decorator creates an association between the URL given as an argument
 and the function
When web browser requests a URL ('/' or '/index'), Flask will invoke this function and
 pass its return value back to the browser as a response
"""
