print("globalobjs(1)")
import sys
sys.path.append('..')
from backend.app.globalobjs import app, db
from .core.config import settings

__all__ = ['app', 'db', 'settings']
