from requests import Session
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from config import settings

DATABASE_URL ="postgresql://"+settings.POSTGRES_USER+":"+settings.POSTGRES_PASSWORD+"@"+settings.POSTGRES_IP+":"+settings.POSTGRES_PORT+"/"+settings.POSTGRES_DB



engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = _declarative.declarative_base()