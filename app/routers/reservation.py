from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.reservation import ReservationRead, ReservationCreate, ReservationUpdate
from app.services import reservation as reservation_service
from app.database.database import get_db

router = APIRouter(prefix="/reservations", tags=["Réservations"])

# @router.get('/', response_model=List[ReservationRead])
# def list_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return reservation_service.list_reservations(db, skip, limit)