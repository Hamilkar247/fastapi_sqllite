from fastapi import APIRouter, Depends

from typing import Optional, List
from sqlalchemy.orm import Session

from mainx import get_db

router = APIRouter(
    prefix="/places",
    tags=["places"],
    responses={404: {"description": "Not"}}
)


@router.post('/places', response_model=Place)
def create_places_view(place: Place, db: Session = Depends(get_db)):
    db_place = create_place_db(db, place)
    return db_place


@router.get('/places', response_model=List[Place])
def get_places_view(db: Session = Depends(get_db)):
    return get_places(db)


@router.get('/place/{place_id}')
def get_place_view(place_id: int, db: Session = Depends(get_db)):
    return get_place(db, place_id)
