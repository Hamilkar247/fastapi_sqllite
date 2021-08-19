from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mainx import get_db
from pydantic_models.sesja_pydantic import Sesja, create_sesja_db

#router = APIRouter(
#    prefix="/zbior_sesji",
#    tags=["zbior_sesji"],
#    responses={404: {"description": "Not"}}
#)
#
#
#@router.post('/zbior_sesji', response_model=Sesja)
#def create_sesja(sesja: Sesja, db: Session = Depends(get_db)):
#    db_sesja = create_sesja_db(db, sesja)
#    return db_sesja


#@router.get('/zbior_sesji', response_model=List[Sesja])
#def get_zbior_sesji(db: Session = Depends(get_db())):
#    return get_zbior_sesji(db)
#
#
#@router.get('/zbior_sesji/id={sesja_id}')
#def get_sesja_id(sesja_id: int, db: Session = Depends(get_db)):
#    return get_sesja_id(db, sesja_id)

