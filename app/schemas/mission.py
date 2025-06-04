from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TypeMission(str, Enum):
    DEPLACEMENT = "DEPLACEMENT"
    REAPPRO = "REAPPRO"
    INVENTAIRE = "INVENTAIRE"
    RECEPTION = "RECEPTION"
    PREPARATION = "PREPARATION"

class EtatMission(str, Enum):
    A_FAIRE = "A_FAIRE"
    EN_COURS = "EN_COURS"
    TERMINE = "TERMINE"
    ECHOUE = "ECHOUE"

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
    urgent: Optional[bool] = False

class MissionCreate(MissionBase):
    pass

class MissionUpdate(MissionBase):
    pass

class MissionRead(MissionBase):
    id: str

    class Config:
        orm_mode = True
