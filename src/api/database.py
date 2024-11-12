from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import AsyncGenerator


DATABASE_URL = "mysql+aiomysql://root:Ti040506@127.0.0.1:3306/moto_rental_db"


engine = create_async_engine(DATABASE_URL, echo=True)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        yield db


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)