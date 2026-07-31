from abc import ABC,abstractmethod
from typing import Optional, List
from domain.matricula import Matricula



class MatriculaRepository(ABC):

    @abstractmethod
    async def salvar(self, matricula: Matricula) -> Matricula:
        ...

    @abstractmethod
    async def buscar_por_id(self, matricula_id: str) -> Optional[Matricula]:
        ...

    @abstractmethod
    async def buscar_por_aluno_e_curso(self, aluno_id: str,curso_id: str) -> Optional[Matricula]:
        ...

    @abstractmethod
    async def listar(self) -> List[Matricula]:
        ...

    @abstractmethod
    async def listar_por_aluno(self,aluno_id:str) ->Optional[Matricula]:
        ...

    @abstractmethod 
    async def listar_por_curso(self, curso_id: str) -> Optional[Matricula]:
        ...

    @abstractmethod
    async def atualizar(self, matricula: Matricula) -> Matricula:
        ...

    @abstractmethod
    async def deletar(self, matricula_id: str) -> None:
        ...