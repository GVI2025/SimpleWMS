from pydantic import BaseModel
from datetime import date,time

class ReservationBase(BaseModel):
    salle_id: str
    date: date
    heure: time
    utilisateur: str

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: str

    class Config:
        orm_mode = True
