from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database.database import Base

class Implantation(Base):
    __tablename__ = "implantations"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    article_id = Column(String, ForeignKey("articles.id"), nullable=False)
    emplacement_id = Column(String, ForeignKey("emplacements.id"), nullable=False)
    quantite = Column(Integer, nullable=False)
    seuil_minimum = Column(Integer, nullable=False)
    commentaires = Column(Text, nullable=True)  # ✅ Ajout ici

    article = relationship("Article")
    emplacement = relationship("Emplacement")
