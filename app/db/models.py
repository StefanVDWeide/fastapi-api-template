import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .sessions import Base


class Users(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    first_name = sa.Column(sa.Text, nullable=False)
    last_name = sa.Column(sa.Text, nullable=False)
    email = sa.Column(sa.Text, nullable=False, unique=True)
    hashed_password = sa.Column(sa.Text, nullable=False)
    creation_date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)  # type: ignore
    is_admin = sa.Column(sa.Boolean, nullable=False, default=False)

    posts = relationship(
        "Posts", back_populates="user", lazy="selectin", cascade="all, delete"
    )


class Posts(Base):
    __tablename__ = "posts"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.Text, nullable=False)
    content = sa.Column(sa.Text, nullable=False)
    user_id = sa.Column(sa.Integer, ForeignKey("users.id"), nullable=False, index=True)
    creation_date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)  # type: ignore

    user = relationship("Users", back_populates="posts", lazy="selectin")  # type: ignore
