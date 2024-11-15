from sqlalchemy import select

from app.Schema.user import *
from app.Database import new_session, User

class UserRepository:
    @classmethod
    async def get_users(cls) -> list[SUser]:
        async with new_session() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()
            users = [SUser(**user_model.__dict__) for user_model in user_models]
            return users

    @classmethod
    async def get_user_by_username(cls, username: str) -> SUser | None:
        async with new_session() as session:
            query = select(User).filter_by(username=username)
            result = await session.execute(query)
            user_models = result.scalars().all()
            users = [SUser(**user_model.__dict__) for user_model in user_models]
            if users:
                return users[0]
            return None