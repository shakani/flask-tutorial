from flask import Flask  # noqa: D104

from config import Config

app = Flask(
    __name__,
)  # Passing __name__ to Flask almost always configures Flask in the correct way
app.config.from_object(Config)

from app import routes  # noqa: E402, F401

"""
`routes` imported at bottom instead of at top
--> workaround to avoid circular imports (common problem in Flask apps)
`routes` module needs to import the `app` variable (not module) defined here
putting import at bottom avoids this issue
"""
