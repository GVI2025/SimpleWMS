from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.mission import MissionRead, MissionCreate, MissionUpdate
from app.services import mission as mission_service
from app.database.database import get_db

router = APIRouter(prefix="/missions", tags=["Missions"])

@router.get("/", response_model=List[MissionRead])
def list_missions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return mission_service.list_missions(db, skip, limit)

@router.post("/", response_model=MissionRead)
def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    return mission_service.create_mission(db, mission)

@router.get("/{mission_id}", response_model=MissionRead)
def get_mission(mission_id: str, db: Session = Depends(get_db)):
    mission = mission_service.get_mission(db, mission_id)
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.put("/{mission_id}", response_model=MissionRead)
def update_mission(mission_id: str, mission: MissionUpdate, db: Session = Depends(get_db)):
    updated = mission_service.update_mission(db, mission_id, mission)
    if not updated:
        raise HTTPException(status_code=404, detail="Mission not found")
    return updated

@router.delete("/{mission_id}", response_model=MissionRead)
def delete_mission(mission_id: str, db: Session = Depends(get_db)):
    deleted = mission_service.delete_mission(db, mission_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mission not found")
    return deleted

# TODO: Fix mission