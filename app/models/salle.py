from sqlalchemy import Column, String, Integer
from uuid import uuid4

from app.database.database import Base

class Salle(Base):
    __tablename__ = "salle"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    nom = Column(String, unique=True, nullable=False)
    capacité = Column(Integer, nullable=False)
    localisation = Column(String, nullable=False)
