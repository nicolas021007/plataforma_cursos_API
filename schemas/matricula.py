from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional



class MastriculaBase(BaseModel):
    aluno_id : UUID
    curso_id: UUID



class MatriculaCreate(MastriculaBase):
    pass


class MatriculaUpdate(BaseModel):
    ativo: Optional[bool] = None


class MatriculaResponse(MastriculaBase):
    id: UUID
    ativo: bool
    data_matricula: datetime

    class Config:
        from_attributes = True