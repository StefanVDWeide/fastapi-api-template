import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .sessions import Base


class Users(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    first_name = sa.Column(sa.Text, nullable=False)
    last_name = sa.Column(sa.Text, nullable=False)
    creation_date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)  # type: ignore

    posts = relationship("Posts", back_populates="users")


class Posts(Base):
    __tablename__ = "posts"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    user_id = sa.Column(
        sa.Integer, ForeignKey("users.id"), nullable=False, index=True
    )
    date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)  # type: ignore
    
    employee = relationship("Users", back_populates="posts") # type: ignore
