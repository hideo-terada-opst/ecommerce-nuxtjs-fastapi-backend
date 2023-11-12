import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from gino.ext.starlette import Gino
sys.path.append('..')
from backend.users.api.controller import router as user_router
from sqlalchemy import MetaData

__all__ = ['app', 'db']

from .globalobjs import app, db
print(f"%% app={app}")
print(f"%% db={db}")

# app = FastAPI(title=settings.PROJECT_NAME)
# db: MetaData = Gino(
#         app,
#         dsn=settings.DATABASE_URI,
#         pool_min_size=3,
#         pool_max_size=20,
#         retry_limit=10,
#         retry_interval=10,
#         ssl=None,
#     )

@app.on_event("startup")
async def startup():
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    print("SHUTDOWN")


app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user_router, prefix='/users')