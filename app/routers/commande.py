from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.commande import CommandeRead, CommandeCreate, CommandeUpdate
from app.services import commande as commande_service
from app.database.database import get_db

router = APIRouter(prefix="/commandes", tags=["Commandes"])

@router.post("/", response_model=CommandeRead)
def create_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    existing = commande_service.get_commande_by_reference(db, commande.reference)
    if existing:
        raise HTTPException(status_code=400, detail="Commande with this reference already exists.")
    return commande_service.create_commande(db, commande)

@router.get("/{commande_id}", response_model=CommandeRead)
def get_commande(commande_id: str, db: Session = Depends(get_db)):
    commande = commande_service.get_commande(db, commande_id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande not found")
    return commande

@router.put("/{commande_id}", response_model=CommandeRead)
def update_commande(commande_id: str, commande: CommandeUpdate, db: Session = Depends(get_db)):
    updated = commande_service.update_commande(db, commande_id, commande)
    if not updated:
        raise HTTPException(status_code=404, detail="Commande not found")
    return updated

@router.delete("/{commande_id}", response_model=CommandeRead)
def delete_commande(commande_id: str, db: Session = Depends(get_db)):
    deleted = commande_service.delete_commande(db, commande_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Commande not found")
    return deleted

@router.get("/", response_model=List[CommandeRead])
def read_commandes(
    skip: int = 0, 
    limit: int = 100, 
    designation: str = None, 
    db: Session = Depends(get_db)
):
    """
    Retrieve all commandes.
    
    Optional filtering by article designation using the 'designation' query parameter.
    Example: GET /commandes?designation=perceuse
    """
    commandes = commande_service.list_commandes(
        db, 
        skip=skip, 
        limit=limit, 
        designation=designation
    )
    return commandes
