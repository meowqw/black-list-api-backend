from http.client import HTTPException

from fastapi import APIRouter, Depends, Body
from starlette import status

from app.Schema.user import *
from app.Service.auth import authenticate_user, create_access_token, get_current_active_user

user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Пользователь"]
)

@user_router.post("/token")
async def login_for_access_token(form_data: LoginData = Body(...)) -> Token:
    auth = await authenticate_user(form_data.username, form_data.password)
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(data={"sub": form_data.username})
    return token

@user_router.get("/me", response_model=SUser)
async def read_users_me(current_user: SUser = Depends(get_current_active_user)):
    return current_user
