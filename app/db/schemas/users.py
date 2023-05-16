from pydantic import BaseModel, constr
from datetime import date


class UsersBase(BaseModel):
    first_name: constr(to_lower=True)  # type: ignore
    last_name: constr(to_lower=True)  # type: ignore

    class Config:
        orm_mode = True


class UsersCreate(UsersBase):
    pass


class Users(UsersBase):
    id: int
    creation_date: date
