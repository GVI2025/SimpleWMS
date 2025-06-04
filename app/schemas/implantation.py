from typing import Optional
from pydantic import BaseModel

class ImplantationBase(BaseModel):
    article_id: str
    emplacement_id: str
    quantite: int
    seuil_minimum: int
    commentaires: Optional[str] = None  # ✅ ici


class ImplantationCreate(ImplantationBase):
    pass

class ImplantationUpdate(ImplantationBase):
    pass

class ImplantationRead(ImplantationBase):
    id: str

    class Config:
        orm_mode = True
