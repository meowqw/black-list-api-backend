from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
from Seeder.user import create_default_user
from app.Router.client import client_router
from app.Router.user import user_router
from Database import create_tables, delete_tables
from Service.auth import get_current_active_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    await create_default_user()
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    user_router
)

app.include_router(
    client_router,
    dependencies=[Depends(get_current_active_user)]
)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
