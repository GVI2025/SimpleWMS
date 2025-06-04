from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.article import ArticleRead, ArticleCreate, ArticleUpdate
from app.services import article as article_service
from app.database.database import get_db

router = APIRouter(prefix="/articles", tags=["Articles"])

@router.get("/", response_model=List[ArticleRead])
def list_articles(
    skip: int = 0,
    limit: int = 100,
    sku: Optional[str] = Query(None, description="Filter by SKU"),
    db: Session = Depends(get_db)
):
    if sku:
        article = article_service.get_article_by_sku(db, sku)
        return [article] if article else []
    return article_service.list_articles(db, skip, limit)

@router.post("/", response_model=ArticleRead)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    existing = article_service.get_article_by_sku(db, article.sku)
    if existing:
        raise HTTPException(status_code=400, detail="Article with this SKU already exists.")
    return article_service.create_article(db, article)

@router.get("/{article_id}", response_model=ArticleRead)
def get_article(article_id: str, db: Session = Depends(get_db)):
    article = article_service.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.put("/{article_id}", response_model=ArticleRead)
def update_article(article_id: str, article: ArticleUpdate, db: Session = Depends(get_db)):
    updated = article_service.update_article(db, article_id, article)
    if not updated:
        raise HTTPException(status_code=404, detail="Article not found")
    return updated

@router.delete("/{article_id}", response_model=ArticleRead)
def delete_article(article_id: str, db: Session = Depends(get_db)):
    deleted = article_service.delete_article(db, article_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Article not found")
    return deleted
