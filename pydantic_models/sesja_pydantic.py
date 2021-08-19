from pydantic import BaseModel
from sqlalchemy.orm import Session

from mainx import DBSesja


class Sesja(BaseModel):
    nazwa_sesji: str
    start_sesji: str
    koniec_sesji: str
    dlugosc_trwania_sesji_w_s: str
    czy_aktywna: str

    class Config:
        orm_mode = True


def get_sesja(db: Session, sesja_id: int):
    return db.query(DBSesja).where(DBSesja.id == sesja_id).first()


def get_zbior_sesji(db: Session):
    return db.query(DBSesja).all()


def create_sesja_db(db: Session, sesja: Sesja):
    db_sesja = DBSesja(**sesja.dict())
    db.add(db_sesja)
    db.commit()
    db.refresh(db_sesja)

    return db_sesja