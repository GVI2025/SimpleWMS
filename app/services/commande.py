from sqlalchemy.orm import Session
from app.models import Commande as CommandeModel, LigneCommande as LigneModel, Article as ArticleModel
from app.schemas.commande import CommandeCreate, CommandeUpdate

def get_commande(db: Session, commande_id: str):
    return db.query(CommandeModel).filter(CommandeModel.id == commande_id).first()

def get_commande_by_reference(db: Session, reference: str):
    return db.query(CommandeModel).filter(CommandeModel.reference == reference).first()

def list_commandes(db: Session, skip: int = 0, limit: int = 100, designation: str = None):
    query = db.query(CommandeModel)
    
    if designation:
        # Join with ligne_commande and article to filter by article designation
        query = query.join(
            LigneModel, 
            CommandeModel.id == LigneModel.commande_id
        ).join(
            ArticleModel, 
            LigneModel.article_id == ArticleModel.id
        ).filter(
            ArticleModel.designation.ilike(f"%{designation}%")
        ).distinct()
    
    return query.offset(skip).limit(limit).all()

def create_commande(db: Session, commande: CommandeCreate):
    db_commande = CommandeModel(
        reference=commande.reference,
        etat=commande.etat
    )
    db.add(db_commande)
    db.flush()  # pour récupérer l'id

    for ligne in commande.lignes:
        db_ligne = LigneModel(
            commande_id=db_commande.id,
            article_id=ligne.article_id,
            quantite=ligne.quantite
        )
        db.add(db_ligne)

    db.commit()
    db.refresh(db_commande)
    return db_commande

def update_commande(db: Session, commande_id: str, commande_data: CommandeUpdate):
    db_commande = get_commande(db, commande_id)
    if db_commande:
        for key, value in commande_data.dict().items():
            setattr(db_commande, key, value)
        db.commit()
        db.refresh(db_commande)
    return db_commande

def delete_commande(db: Session, commande_id: str):
    db_commande = get_commande(db, commande_id)
    if db_commande:
        db.delete(db_commande)
        db.commit()
    return db_commande
