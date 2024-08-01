from flask import Flask

app = Flask(__name__) # Passing __name__ to Flask almost always configures Flask in the correct way

from app import routes
"""
`routes` imported at bottom instead of at top
--> workaround to avoid circular imports (common problem in Flask apps)
`routes` module needs to import the `app` variable (not module) defined here
putting import at bottom avoids this issue
"""