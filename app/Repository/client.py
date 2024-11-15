from sqlalchemy import select, delete
from app.Database import new_session, Client
from app.Schema.client import SClientAdd, SClient, SClientFilter


class ClientRepository:
    @classmethod
    async def add_client(cls, client: SClientAdd) -> int:
        async with new_session() as session:
            data = client.model_dump()
            new_client = Client(name=data['name'], phone=data['phone'], description=data['description'])
            session.add(new_client)
            await session.flush()
            await session.commit()
            return new_client.id

    @classmethod
    async def get_clients(cls, filter_client: SClientFilter) -> list[SClient]:
        async with new_session() as session:
            query = select(Client)

            if filter_client.phone:
                query = query.filter_by(phone=filter_client.phone)

            if filter_client.name:
                query = query.filter_by(name=filter_client.name)

            result = await session.execute(query)

            clients = result.scalars().all()

            return [SClient.model_validate(client) for client in clients]

    @classmethod
    async def delete_client(cls, id_: int) -> bool:
        async with new_session() as session:
            client = await session.get(Client, id_)
            if not client:
                return False

            await session.delete(client)
            await session.commit()
            return True
