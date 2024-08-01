import os  # noqa: D100


class Config:  # noqa: D101
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
