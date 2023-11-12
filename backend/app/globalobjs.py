from fastapi import FastAPI
from .core.config import settings
from gino_starlette import Gino
# from gino.ext.starlette import Gino
from sqlalchemy import MetaData

__all__ = ['app', 'db']

global app, db, app_db_singleton

class AppDbSingleton(object):
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(AppDbSingleton, cls).__new__(cls)

            global app, db
            app = FastAPI(title=settings.PROJECT_NAME)
            print("%%%%%%%% init Gino")
            db = Gino(
                    app,
                    dsn=settings.DATABASE_URI,
                    pool_min_size=3,
                    pool_max_size=20,
                    retry_limit=10,
                    retry_interval=10,
                    ssl=None,
                )
        print(f"instance={cls._instance}")
        return cls._instance

app_db_singleton = AppDbSingleton()
