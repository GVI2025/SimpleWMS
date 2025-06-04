from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TypeMission(str, Enum):
    DEPLACEMENT = "Déplacement"
    REAPPRO = "Réapprovisionnement"
    INVENTAIRE = "Inventaire"
    RECEPTION = "Réception"
    PREPARATION = "Préparation commande"

class EtatMission(str, Enum):
    A_FAIRE = "À faire"
    EN_COURS = "En cours"
    TERMINE = "Terminé"
    ECHOUE = "Échoué"

class MissionBase(BaseModel):
    type: TypeMission
    etat: EtatMission
    article_id: str
    source_id: Optional[str]
    destination_id: Optional[str]
    quantite: int
    agent_id: Optional[str]
    date_creation: datetime
    date_execution: Optional[datetime] = None

class MissionCreate(MissionBase):
    urgent : False
    pass

class MissionUpdate(MissionBase):
    urgent : False
    pass

class MissionRead(MissionBase):
    id: str
    urgent: False

    class Config:
        orm_mode = True
