from pydantic import BaseModel, Field
from datetime import date, datetime
from uuid import UUID
from typing import Optional

class CursoBase(BaseModel):
    nome : str = Field(...,min_length= 3, max_length = 150)
    descricao : str = Field(..., min_length = 10, max_length = 1000)
    carga_horario: str = Field(..., gt = 0, description= "Carga horária em horas")
    professor : Optional[str] = None
    ativo : Optional[bool] = None



class CursoResponse(CursoBase):
    id: UUID
    ativo: bool
    data_criacao : datetime


    class Config:
        from_attributes = True
