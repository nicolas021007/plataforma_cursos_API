from uuid import uuid4
from typing import List
from domain.curso import Curso
from domain.repositories.curso_repositories import CursoRepository
from schemas.curso import CursoCreate,CursoUpdate


class CursoService:

    def __init__(self, repository: CursoRepository):
        self.repository = repository

    async  def  registrar(self, dados: CursoCreate) -> Curso:
        curso_existente = await self.repository.buscar_por_nome(dados.nome)

        if curso_existente:
            raise ValueError("Já existe um curso cadastrado com esse nome.")


        curso = Curso(
            id = uuid4(),
            nome = dados.nome,
            descricao= dados.descricao,
            carga_horaria=dados.carga_horaria,
            professor= dados.professor,

        )

        return await self.repository.salvar(curso)


    async def buscar_por_id(self, curso_id: str) -> Curso:

        curso = await self.repository.buscar_por_id(curso_id)

        if not curso :
            raise ValueError("Curso não encontrado.")

        return curso

    async def listar(self) -> List[Curso]:
        return await self.repository.listar()

    async def atualizar(self, curso_id : str, dados: CursoUpdate) -> Curso:

        curso = await self.buscar_por_id(curso_id)

        curso.atualizar_dados(
            nome = dados.nome,
            descricao=dados.descricao,
            carga_horaria= dados.carga_horaria,
            professor= dados.professor,
        )


        if dados.ativo is not None:
            if dados.ativo:
                curso.ativar()

            else:
                curso.desativar()


        return await self.repository.atualizar(curso)

    async def deletar(self, curso_id: str) -> None:
        await self.buscar_por_id(curso_id)
        await self.repository.deletar(curso_id)