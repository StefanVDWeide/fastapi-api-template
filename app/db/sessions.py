from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
)

from os import getenv
from typing import Any, AsyncGenerator
from asyncio import current_task


SQLALCHEMY_DATABASE_URL = getenv("DATABASE_URL", "sqlite+aiosqlite:///sql_app.db")

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


async def create_async_session() -> async_scoped_session[AsyncSession]:
    async_session = async_scoped_session(
        async_sessionmaker(
            autocommit=False,
            autoflush=False,
            class_=AsyncSession,
            bind=async_engine,
            expire_on_commit=False,
        ),
        scopefunc=current_task,
    )

    return async_session


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    Session = await create_async_session()
    async with Session() as session:
        try:
            yield session
        finally:
            await session.close()


Base: Any = declarative_base()
