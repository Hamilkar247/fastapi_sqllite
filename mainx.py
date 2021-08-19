from fastapi import FastAPI, Depends
from pydantic import BaseModel

import fastapi_db_sqlite
from api_web import place_api, sesja_api
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer, DateTime, create_engine
from typing import Optional, List
from sqlalchemy.orm import declarative_base, sessionmaker, Session



app = FastAPI()
#app.include_router(place_api.router)
#app.include_router(sesja_api.router)

#SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///.db.sqlite3:'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
Base = declarative_base()


# Depedency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DBSesja(Base):
    __tablename__ = "sesje"

    id = Column(Integer, primary_key=True, index=True)
    nazwa_sesji = Column(String)
    start_sesji = Column(String)
    koniec_sesji = Column(String)
    czy_aktywna = Column(String)
    dlugosc_trwania_sesji_w_s = Column(String)


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


class DBUzytkownik(Base):
    __tablename__ = "uzytkownicy"

    id = Column(Integer, primary_key=True, index=True)
    nazwa = Column(String(50))
    email = Column(String(100))
    dane_osobowe = Column(String, nullable=True)
    stanowisko = Column(String)
    opis = Column(String, nullable=True)
    uprawnienia = Column(String, nullable=True)


class DBPaczkaDanych(Base):
    __tablename__ = "paczki_danych"

    id = Column(Integer, primary_key=True, index=True)
    czas_paczki = Column(DateTime)
    kod_status = Column(String(50))
    numer_seryjny = Column(String(20))


class DBWartoscPomiarowSensora(Base):
    __tablename__ = "wartosci_pomiarow_sensora"

    id = Column(Integer, primary_key=True, index=True)
    wartosc = Column(Integer)
    litery_porzadkowe = Column(String[10])


Base.metadata.create_all(bind=engine)


class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class Config:
        orm_mode = True


def get_place(db: Session, place_id: int):
    return db.query(DBPlace).where(DBPlace.id == place_id).first()


def get_places(db: Session):
    return db.query(DBPlace).all()


def create_place_db(db: Session, place: Place):
    db_place = DBPlace(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)

    return db_place


@app.get('/')
async def root():
    return {'message': 'Hello World!'}
