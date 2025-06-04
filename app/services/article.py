from typing import Optional

from sqlalchemy.orm import Session
from app.models import Article as ArticleModel
from app.schemas.article import ArticleCreate, ArticleUpdate

def get_article(db: Session, article_id: str):
    return db.query(ArticleModel).filter(ArticleModel.id == article_id).first()

def get_article_by_sku(db: Session, sku: str):
    return db.query(ArticleModel).filter(ArticleModel.sku == sku).first()

def list_articles(db: Session, skip: int = 0, limit: int = 100, sku: Optional[str] = None):
    query = db.query(ArticleModel)
    if sku:
        query = query.filter(ArticleModel.sku == sku)
    return query.offset(skip).limit(limit).all()

def create_article(db: Session, article: ArticleCreate):
    db_article = ArticleModel(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article_id: str, article_data: ArticleUpdate):
    db_article = get_article(db, article_id)
    if db_article:
        for key, value in article_data.dict().items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: str):
    db_article = get_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article
