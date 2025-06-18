from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import date, time

from app.database.database import Base

class Reservation(Base): 
    __tablename__ = "reservation"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    salle_id = Column(String, ForeignKey("salle.id"), nullable=False)
    date = Column(date, nullable=False)
    heure = Column(time, nullable=False)
    utilisateur = Column(String, nullable=False)

    salle = relationship("Salle", foreign_keys=[salle_id])