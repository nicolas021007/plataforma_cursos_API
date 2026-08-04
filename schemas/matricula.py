from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional, List



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
    aluno_nome: str
    curso_nome: str


    class Config:
        from_attributes = True

class AlunoMatriculado(BaseModel):
    id: UUID
    nome: str
    matricula_ativa: bool


class CursoComAlunos(BaseModel):
    id: UUID
    nome: str
    descricao: str
    carga_horaria: int
    professor: Optional[str] = None
    ativo: bool
    data_criacao: datetime
    alunos: List[AlunoMatriculado]
