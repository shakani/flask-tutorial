"""Routes handle the different URLs that the application supports.

Handlers for the app routes are written as Python functions called *view functions*
View functions are mapped to one or more route URLs so Flask knows what logic to
execute when a client requests a given URL
"""

from app import app

user = {"username": "Miguel"}


# Home page route
@app.route("/")
@app.route("/index")
def index() -> str:
    """Return index page."""
    return f"""
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello {user["username"]}! </h1>
    </body>
</html>
"""


"""
Decorator pattern: use decorators to register functions as callbacks for certain events
Here, @app.route decorator creates an association between the URL given as an argument
 and the function
When web browser requests a URL ('/' or '/index'), Flask will invoke this function and
 pass its return value back to the browser as a response
"""
