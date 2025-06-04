from sqlalchemy.orm import Session
from app.models import Mission as MissionModel
from app.schemas.mission import MissionCreate, MissionUpdate

def get_mission(db: Session, mission_id: str):
    return db.query(MissionModel).filter(MissionModel.id == mission_id).first()

def list_missions(db: Session, skip: int = 0, limit: int = 100):
    # Cette ligne de code récupère toutes les missions dont le statut n'est pas "terminé" ou "échoué",
    return db.query(MissionModel).filter(MissionModel.etat.notin_(["TERMINE", "ECHOUE"])).offset(skip).limit(limit).all()

def create_mission(db: Session, mission: MissionCreate):
    db_mission = MissionModel(**mission.dict())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission

def update_mission(db: Session, mission_id: str, mission_data: MissionUpdate):
    db_mission = get_mission(db, mission_id)
    if db_mission:
        for key, value in mission_data.dict().items():
            setattr(db_mission, key, value)
        db.commit()
        db.refresh(db_mission)
    return db_mission

def delete_mission(db: Session, mission_id: str):
    db_mission = get_mission(db, mission_id)
    if db_mission:
        db.delete(db_mission)
        db.commit()
    return db_mission
