from sqlalchemy import Column, Enum, ForeignKey, Integer, DateTime, String, Boolean
from sqlalchemy.orm import relationship
from uuid import uuid4
import enum
from datetime import datetime

from app.database.database import Base

class TypeMission(enum.Enum):
    DEPLACEMENT = "Déplacement"
    REAPPRO = "Réapprovisionnement"
    INVENTAIRE = "Inventaire"
    RECEPTION = "Réception"
    PREPARATION = "Préparation commande"

class EtatMission(enum.Enum):
    A_FAIRE = "À faire"
    EN_COURS = "En cours"
    TERMINE = "Terminé"
    ECHOUE = "Échoué"

class Mission(Base):
    __tablename__ = "missions"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    type = Column(Enum(TypeMission), nullable=False)
    etat = Column(Enum(EtatMission), nullable=False, default=EtatMission.A_FAIRE)
    article_id = Column(String, ForeignKey("articles.id"), nullable=False)
    source_id = Column(String, ForeignKey("emplacements.id"), nullable=True)
    destination_id = Column(String, ForeignKey("emplacements.id"), nullable=True)
    quantite = Column(Integer, nullable=False)
    agent_id = Column(String, ForeignKey("agents.id"), nullable=True)
    date_creation = Column(DateTime, default=datetime.utcnow)
    date_execution = Column(DateTime, nullable=True)
    urgent = Column(Boolean, default=False, nullable=True)

    article = relationship("Article")
    source = relationship("Emplacement", foreign_keys=[source_id])
    destination = relationship("Emplacement", foreign_keys=[destination_id])
    agent = relationship("Agent")
