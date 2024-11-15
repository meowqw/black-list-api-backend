from app.Database import new_session, User
from app.Service.auth import pwd_context
from sqlalchemy import select


async def create_default_user():
    async with new_session() as session:
        existing_user = await session.execute(select(User).filter_by(username="admin@gmail.com"))
        if not existing_user.scalar_one_or_none():
            hashed_password = pwd_context.hash("123456")
            user = User(name="Admin", username="admin@gmail.com", password=hashed_password)
            session.add(user)
            await session.commit()
            print("Пользователь по умолчанию создан.")
        else:
            print("Пользователь по умолчанию уже существует.")
