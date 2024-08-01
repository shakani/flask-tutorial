from flask import Flask

app = Flask(__name__) # Passing __name__ to Flask almost always configures Flask in the correct way

from app import routes