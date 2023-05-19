from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str


class TokenData(BaseModel):
    username: str | None = None


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: float | None = None
