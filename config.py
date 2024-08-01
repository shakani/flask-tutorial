import os  # noqa: D100

basedir = os.path.abspath(os.path.dirname(__file__))  # noqa: PTH100, PTH120


class Config:  # noqa: D101
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")  # noqa: PTH118
