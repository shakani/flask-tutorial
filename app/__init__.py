from flask import Flask  # noqa: D104
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(
    __name__,
)  # Passing __name__ to Flask almost always configures Flask in the correct way
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes  # noqa: E402, F401

"""
`routes` imported at bottom instead of at top
--> workaround to avoid circular imports (common problem in Flask apps)
`routes` module needs to import the `app` variable (not module) defined here
putting import at bottom avoids this issue
"""
