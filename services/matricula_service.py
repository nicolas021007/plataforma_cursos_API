from uuid import uuid4
from typing import List

from domain.matricula import  Matricula
from domain.repositories.matricula_repositories import MatriculaRepository
from domain.repositories.aluno_repositories import AlunoRepository
from domain.repositories.curso_repositories import CursoRepository
from schemas.matricula import MatriculaCreate, MatriculaUpdate,MatriculaResponse, CursoComAlunos


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

    async def _montar_resposta(self,matricula: Matricula) -> dict:
        aluno = await self.aluno_repository.buscar_por_id(str(matricula.aluno_id))
        curso = await self.curso_repository.buscar_por_id(str(matricula.curso_id))

        return {
            "id" : matricula.id,
            "aluno_id": matricula.aluno_id,
            "curso_id": matricula.curso_id,
            "aluno_nome":aluno.nome if aluno else "Aluno não encontrado",
            "curso_nome": curso.nome if curso else "Curso não encontrado",
            "ativo": matricula.ativo,
            "data_matricula": matricula.data_matricula
        }

    async def registrar(self, dados: MatriculaCreate) -> dict:
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

        matricula_salva = await self.repository.salvar(matricula)
        return await self._montar_resposta(matricula_salva)



    async def buscar_por_id(self, matricula_id: str) -> Matricula:

        matricula = await self.repository.buscar_por_id(matricula_id)

        if not matricula:
            raise ValueError("Matricula não encontrada.")

        return await self._montar_resposta(matricula)


    async def listar(self) -> List[dict]:
        matriculas = await self.repository.listar()
        return [await self._montar_resposta(m) for m in matriculas]


    async def listar_por_aluno(self, aluno_id: str) -> List[dict]:
        matriculas = await self.repository.listar_por_aluno(aluno_id)
        return [await self._montar_resposta(m) for m in matriculas]


    async def listar_por_curso(self, curso_id : str) -> List[dict]:

        matriculas = await self.repository.listar_por_curso(curso_id)
        return [await self._montar_resposta(m) for m in matriculas]


    async def curso_com_alunos(self, curso_id : str) -> dict:

        curso = await self.curso_repository.buscar_por_id(curso_id)


        if not curso:
            raise ValueError("Curso não encontrado.")

        matriculas = await self.repository.listar_por_curso(curso_id)

        alunos = []

        for matricula in matriculas:

            aluno = await self.aluno_repository.buscar_por_id(str(matricula.aluno_id))

            if aluno:
                alunos.append({
                    "id": aluno.id,
                    "nome": aluno.nome,
                    "matricula_ativa": matricula.ativo
                })

        return {
            "id": curso.id,
            "nome": curso.nome,
            "descricao": curso.descricao,
            "carga_horaria": curso.carga_horaria,
            "professor": curso.professor,
            "ativo": curso.ativo,
            "data_criacao": curso.data_criacao,
            "alunos": alunos
        }


    async def atualizar(self, matricula_id: str, dados: MatriculaUpdate) -> dict:

        matricula = await self.repository.buscar_por_id(matricula_id)

        if not matricula:
            raise ValueError("Matricula não encontrada.")

        if dados.ativo is not None:
            if dados.ativo:
                matricula.reativar()

            else:
                matricula.cancelar()

                
        matricula_atualizada = await self.repository.atualizar(matricula)

        return await self._montar_resposta(matricula_atualizada)

    async def deletar(self, matricula_id: str) -> None:

        await self.buscar_por_id(matricula_id)
        await self.repository.deletar(matricula_id)

        