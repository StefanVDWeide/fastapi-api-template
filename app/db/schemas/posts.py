from pydantic import BaseModel
from datetime import date


class PostsBase(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True


class PostsCreate(PostsBase):
    user_id: int


class Posts(PostsBase):
    id: int
    creation_date: date
    user_id: int
