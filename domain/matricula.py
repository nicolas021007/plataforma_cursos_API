from datetime import datetime
from uuid import UUID
from typing import  Optional


class Matricula:
    def __init__(
            self,
            id: UUID,
            aluno_id: UUID,
            curso_id: UUID,
            ativo: bool = True,
            data_matricula: Optional[datetime] = None,
    ):

        self.id = id
        self.aluno_id =aluno_id
        self.curso_id = curso_id
        self.ativo = ativo
        self.data_matricula = data_matricula or datetime.now()

    #-------regras de negócio -----------------


    def cancelar(self) -> None:

        if not self.ativo:
            raise ValueError("Matrícula já está cancelada.")

        self.ativo = False

    def reativar(self) -> None:

        if self.ativo:
            raise ValueError("Matrícula já está ativa.")

        self.ativo = True

    def __repr__(self) -> str:
        
        return f"<Matrícula aluno ={self.aluno_id} curso={self.curso_id} ativo={self.ativo}"

        