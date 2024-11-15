from typing import Dict

from fastapi import APIRouter, Depends, Body

from app.Repository.client import ClientRepository
from app.Schema.client import SClient, SClientAdd, SClientFilter

from app.Service.auth import get_current_active_user

client_router = APIRouter(
    prefix="/api/v1/clients",
    tags=["Список клиентов"],
    dependencies=[Depends(get_current_active_user)]
)


@client_router.post("")
async def add_client(client: SClientAdd = Body(...)) -> dict[str, bool]:
    new_client_id = await ClientRepository.add_client(client)
    return {"result": new_client_id is not None}


@client_router.get("")
async def get_clients(filter_client: SClientFilter = Depends()) -> list[SClient]:
    clients = await ClientRepository.get_clients(filter_client)
    return clients


@client_router.delete("/{id}")
async def delete_client(id: int) -> dict[str, bool]:
    result = await ClientRepository.delete_client(id)
    return {'result': result}
