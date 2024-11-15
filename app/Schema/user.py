from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginData(BaseModel):
    username: str
    password: str


class SUser(BaseModel):
    username: str
    name: str
    password: str

    class Config:
        orm_mode = True
        from_attributes = True