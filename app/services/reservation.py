from sqlalchemy.orm import Session
from app.models import Reservation as ReservationModel

def create_reservation(db: Session, reservation: ReservationModel):
    db_reservation = ReservationModel(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservation(db: Session, reservation_id: str):
    return db.query(ReservationModel).filter(ReservationModel.id == reservation_id).first()
