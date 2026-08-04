from pydantic import BaseModel,EmailStr, Field
from  datetime import date, datetime
from uuid import UUID
from typing import Optional


class Alunobase(BaseModel):

    nome : str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    data_nascimento: date
    telefone: Optional[str] = Field(None, max_length=20)

class AlunoCreate(Alunobase):
    senha: str = Field(..., min_length = 6 , max_length  =20)

class AlunoUpdate(BaseModel):

    nome: Optional[str] = Field(..., min_length = 3, max_length = 100)
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    ativo :Optional[bool] = None

class AlunoResponse(Alunobase):

    id: UUID
    ativo: bool
    data_cadastro: datetime

    class Config:
        from_attribute = True


