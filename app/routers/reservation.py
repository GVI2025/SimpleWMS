from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.reservation import ReservationRead, ReservationCreate, ReservationUpdate
from app.services import reservation as reservation_service
from app.database.database import get_db

router = APIRouter(prefix="/reservations", tags=["Réservations"])

@router.get('/', response_model=List[ReservationRead])
def list_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return reservation_service.get_reservation(db, skip, limit)

@router.post('/', response_model=ReservationRead)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return reservation_service.create_reservation(db, reservation)

@router.get('/{reservation_id}', response_model=ReservationRead)
def get_reservation(reservation_id: str, db: Session = Depends(get_db)):
    reservation = reservation_service.get_reservation_by_id(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.put('/{reservation_id}', response_model=ReservationRead)
def update_reservation(reservation_id: str, reservation: ReservationUpdate, db: Session = Depends(get_db)):
    updated = reservation_service.update_reservation(db, reservation_id, reservation)
    if not updated:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated  