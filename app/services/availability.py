from datetime import datetime
from app.database.database import Base
from app.models.salle import Salle
from app.models.reservation import Reservation

def update_room_availability(Base):
    db = Base()
    try:
        now = datetime.now()

        rooms = db.query(Salle).all()
        for room in rooms:
            active_reservation = db.query(Reservation).filter(
                Reservation.room_id == room.id,
                Reservation.start_time <= now,
                Reservation.end_time >= now
            ).first()

            room.is_available = active_reservation is None

        db.commit()
        print(f"[{now}] Room availability updated.")
    finally:
        db.close()