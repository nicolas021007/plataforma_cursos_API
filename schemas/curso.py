from pydantic import BaseModel, Field
from datetime import date, datetime
from uuid import UUID
from typing import Optional

class CursoBase(BaseModel):
    nome : str = Field(...,min_length= 3, max_length = 150)
    descricao : str = Field(..., min_length = 10, max_length = 1000)
    carga_horaria: int = Field(..., gt = 0, description= "Carga horária em horas")
    professor : Optional[str] = None
   



class CursoCreate(CursoBase):
    pass

class CursoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length =3 , max_length= 150)
    descricao : Optional[str] = Field(None, min_length = 10, max_length = 1000)
    carga_horaria: int = Field(None, gt = 0)
    professor: Optional[str] = None
    ativo: Optional[bool] =None

    
class CursoResponse(CursoBase):
    id: UUID
    ativo: bool
    data_criacao : datetime


    class Config:
        from_attributes = True
