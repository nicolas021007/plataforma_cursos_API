from uuid import uuid4
from typing import List

from domain.matricula import  Matricula
from domain.repositories.matricula_repositories import MatriculaRepository
from domain.repositories.aluno_repositories import AlunoRepository
from domain.repositories.curso_repositories import CursoRepository
from schemas.matricula import MatriculaCreate, MatriculaUpdate


class MatriculaService:

    def __init__(
            self, 
            repository:MatriculaRepository,
            aluno_repository: AlunoRepository,
            curso_repository: CursoRepository,
    ):
        self.repository = repository
        self.aluno_repository = aluno_repository
        self.curso_repository = curso_repository

    async def registrar(self, dados: MatriculaCreate) -> Matricula:
        aluno = await self.aluno_repository.buscar_por_id(str(dados.aluno_id))

        if  not aluno:
            raise ValueError("Aluno não encontrado.")

        curso = await self.curso_repository.buscar_por_id(str(dados.curso_id))

        if not curso:
            raise ValueError("Curso não encotrado.")

        matricula_existente = await self.repository.buscar_por_aluno_e_curso(str(dados.aluno_id), str(dados.curso_id))

        if matricula_existente:
            raise ValueError("Aluno já está matriculado nesse curso.")

        matricula = Matricula(
            id = uuid4(),
            aluno_id = dados.aluno_id,
            curso_id = dados.curso_id,
        )

        return await self.repository.salvar(matricula)



    async def buscar_por_id(self, matricula_id: str) -> Matricula:

        matricula = await self.repository.buscar_por_id(matricula_id)

        if not matricula:
            raise ValueError("Matricula não encontrada.")

        return matricula


    async def listar(self) -> List[Matricula]:
        return await self.repository.listar()


    async def listar_por_aluno(self, aluno_id: str) -> List[Matricula]:
        return await self.repository.listar_por_aluno(aluno_id)


    async def listar_por_curso(self, curso_id : str) -> List[Matricula]:

        return await self.repository.listar_por_curso(curso_id)


    async def atualizar(self, matricula_id: str, dados: MatriculaUpdate) -> Matricula:

        matricula = await self.buscar_por_id(matricula_id)

        if dados.ativo is not None:
            if dados.ativo:
                matricula.reativar()

            else:
                matricula.cancelar()

        return await self.repository.atualizar(matricula)

    async def deletar(self, matricula_id: str) -> None:

        await self.buscar_por_id(matricula_id)
        await self.repository.deletar(matricula_id)

        