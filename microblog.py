import sqlalchemy as sa
import sqlalchemy.orm as so

from app import app, db
from app.models import Post, User


@app.shell_context_processor
def make_shell_context() -> dict:
    return {
        "sa": sa,
        "so": so,
        "db": db,
        "User": User,
        "Post": Post,
    }
