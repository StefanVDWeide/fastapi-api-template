from pydantic import BaseModel, constr, EmailStr, Field
from datetime import date
from app.db.schemas.posts import Posts


class UsersBase(BaseModel):
    first_name: constr(to_lower=True)  # type: ignore
    last_name: constr(to_lower=True)  # type: ignore
    email: EmailStr
    is_admin: bool

    class Config:
        orm_mode = True


class UsersCreate(UsersBase):
    password: str = Field(alias="password")


class Users(UsersBase):
    id: int
    creation_date: date
    posts: list[Posts] = []
