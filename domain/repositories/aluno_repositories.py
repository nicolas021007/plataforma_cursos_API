from abc import ABC, abstractmethod
from typing import Optional, List
from domain.aluno import Aluno


class AlunoRepository(ABC):

    @abstractmethod
    async def criar(self, aluno: Aluno) -> Aluno:
        pass

    @abstractmethod
    async def buscar_por_id(self, id:str) -> Optional[Aluno]:
        pass

    @abstractmethod
    async def buscar_por_email(self, email:str) -> Optional[Aluno]:
        pass

    @abstractmethod
    async def listar(self)-> List[Aluno]:
        pass

    @abstractmethod
    async def atualizar(self, aluno: Aluno) -> Aluno:
        pass
    

    @abstractmethod
    async def deletar(self, id: str) -> None:
        pass