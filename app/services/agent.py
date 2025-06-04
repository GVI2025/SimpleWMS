from typing import Optional

from sqlalchemy.orm import Session
from app.models import Agent as AgentModel
from app.schemas.agent import AgentCreate, AgentUpdate

def get_agent(db: Session, agent_id: str):
    return db.query(AgentModel).filter(AgentModel.id == agent_id).first()

def get_agent_by_email(db: Session, email: str):
    return db.query(AgentModel).filter(AgentModel.email == email).first()

def list_agents(db: Session, skip: int = 0, limit: int = 100, actif: Optional[bool] = None):
    query = db.query(AgentModel)
    if actif is not None:
        query = query.filter(AgentModel.actif == actif)
    return query.offset(skip).limit(limit).all()

def create_agent(db: Session, agent: AgentCreate):
    db_agent = AgentModel(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def update_agent(db: Session, agent_id: str, agent_data: AgentUpdate):
    db_agent = get_agent(db, agent_id)
    if db_agent:
        for key, value in agent_data.dict().items():
            setattr(db_agent, key, value)
        db.commit()
        db.refresh(db_agent)
    return db_agent

def delete_agent(db: Session, agent_id: str):
    db_agent = get_agent(db, agent_id)
    if db_agent:
        db.delete(db_agent)
        db.commit()
    return db_agent
