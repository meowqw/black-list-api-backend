from typing import Optional

from pydantic import BaseModel, ConfigDict


class SClientAdd(BaseModel):
    name: str
    phone: str
    description: str


class SClient(SClientAdd):
    id: int
    name: str
    phone: str
    description: str

    class Config:
        orm_mode = True
        from_attributes = True


class SClientItemId(BaseModel):
    id: int


class SClientFilter(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
