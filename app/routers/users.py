from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.db import sessions
from app.db.models import Users
from app.db.schemas import users as user_schemas
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from typing import Sequence, Annotated
from app.deps import get_current_user


router = APIRouter(prefix="/users", tags=["users"])

auth_user_dependency = Annotated[Users, Depends(get_current_user)]


@router.get("/get/users")
async def get_users(
    current_user: auth_user_dependency,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> Sequence[user_schemas.Users]:
    q = select(Users)
    result = await db.execute(q)
    users = result.scalars().all()

    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/get/user/{id}")
async def get_user(
    current_user: auth_user_dependency,
    id: int,
    db: AsyncSession = Depends(sessions.get_async_session),
) -> user_schemas.Users | dict:
    # Construct the query, in this case a scaler since we expect a single value
    # and don't need a tuple
    q = await db.scalars(select(Users).filter(Users.id == id))
    user = q.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# TODO: Implement functionality to delete user, only accessible for admins
@router.delete("/delete/user/{id}")
async def delete_user(current_user: auth_user_dependency, id: int) -> str:
    return "ok"
