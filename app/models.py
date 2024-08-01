from typing import Optional  # noqa: D100

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class User(db.Model):  # noqa: D101
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))  # noqa: FA100

    def __repr__(self) -> str:  # noqa: D105
        return f"<User {self.username}>"
