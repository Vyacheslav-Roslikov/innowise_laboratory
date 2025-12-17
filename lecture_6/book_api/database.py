from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import Annotated, AsyncGenerator
from fastapi import Depends

DATABASE_URL = "sqlite+aiosqlite:///./books.db"

engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})
new_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Model(MappedAsDataclass, DeclarativeBase):
    """
    The base class for all database models.
    """

    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Asynchronous session generator for social dependency.
    """
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]
