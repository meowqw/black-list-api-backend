import sys
sys.path.append("..")

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///black-list.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
   pass

from .client import Client
from .user import User

async def create_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)