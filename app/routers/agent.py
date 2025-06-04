from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.agent import AgentRead, AgentCreate, AgentUpdate
from app.services import agent as agent_service
from app.database.database import get_db

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.get("/", response_model=List[AgentRead])
def list_agents(
    skip: int = 0,
    limit: int = 100,
    actif: Optional[bool] = Query(None, description="Lister seulement les agents actifs"),
    db: Session = Depends(get_db)
):
    return agent_service.list_agents(db, skip=skip, limit=limit, actif=actif)


@router.post("/", response_model=AgentRead)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    existing = agent_service.get_agent_by_email(db, agent.email)
    if existing:
        raise HTTPException(status_code=400, detail="Agent with this email already exists.")
    return agent_service.create_agent(db, agent)

@router.get("/{agent_id}", response_model=AgentRead)
def get_agent(agent_id: str, db: Session = Depends(get_db)):
    agent = agent_service.get_agent(db, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.put("/{agent_id}", response_model=AgentRead)
def update_agent(agent_id: str, agent: AgentUpdate, db: Session = Depends(get_db)):
    updated = agent_service.update_agent(db, agent_id, agent)
    if not updated:
        raise HTTPException(status_code=404, detail="Agent not found")
    return updated

@router.delete("/{agent_id}", response_model=AgentRead)
def delete_agent(agent_id: str, db: Session = Depends(get_db)):
    deleted = agent_service.delete_agent(db, agent_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Agent not found")
    return deleted
