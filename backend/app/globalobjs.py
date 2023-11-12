from fastapi import FastAPI
from .core.config import settings
from gino.ext.starlette import Gino
from sqlalchemy import MetaData

__all__ = ['app', 'db']

app = FastAPI(title=settings.PROJECT_NAME)
db: MetaData = Gino(
        app,
        dsn=settings.DATABASE_URI,
        pool_min_size=3,
        pool_max_size=20,
        retry_limit=10,
        retry_interval=10,
        ssl=None,
    )
