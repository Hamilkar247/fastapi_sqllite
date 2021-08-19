from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer, create_engine
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from db_sqlite_fastapi.place_sqlite import Base, SessionLocal


def setup_sqlalchemy():
    #SqlAlchemy Setup
    SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///.db.sqlite3:'
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()


# Depedency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DBPlace(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String, nullable=True)
    coffee = Column(Boolean)
    wifi = Column(Boolean)
    food = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)

