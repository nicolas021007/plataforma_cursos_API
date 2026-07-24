from abc import ABC, abstractmethod
from typing import Optional, List
from domain.curso import Curso

class CursoRepository(ABC):

    @abstractmethod

    async def salvar(self, curso: Curso) -> Curso:
        ...

    @abstractmethod

    async def buscar_por_id(self, curso_id :  str) -> Optional[Curso]:
        ...

    @abstractmethod

    async def buscar_por_nome(self, curso_nome : str ) -> Optional[Curso]:
        ...


    @abstractmethod

    async def listar(self) -> List[Curso]:
        ...

    @abstractmethod

    async def atualizar(self, curso: Curso) -> Curso :
        ...

    @abstractmethod

    async def deletar(self, curso_id: str) -> None:
        ...