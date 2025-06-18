from pydantic import BaseModel

class SalleBase(BaseModel):
    nom: str
    capacite: int
    localisation: str

class SalleCreate(SalleBase):
    pass

class SalleUpdate(SalleBase):
    pass

class SalleRead(SalleBase):
    id: str

    class Config:
        orm_mode = True