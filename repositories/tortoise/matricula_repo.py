from typing import Optional, List
from domain.matricula import Matricula
from domain.repositories.matricula_repositories import MatriculaRepository
from infraestructure.tortoise.models import MatriculaModel

class MatriculaRepositoryTortoise(MatriculaRepository):

    def criar(self, model:MatriculaModel) -> Matricula:
        return Matricula(
            id = model.id,
            aluno_id = model.aluno_id,
            curso_id = model.curso_id,
            ativo = model.ativo,
            data_matricula= model.data_matricula,
        )

    async def salvar(self, matricula: Matricula) -> Matricula:

        model = await MatriculaModel.create(
            id = str(matricula.id),
            aluno_id = str(matricula.aluno_id),
            curso_id = str(matricula.curso_id),
            ativo = matricula.ativo,
        )
        return self.criar(model)

    async def buscar_por_id(self, matricula_id = str) -> Optional[Matricula]:
        matricula_model = await MatriculaModel.get_or_none(id = matricula_id)

        return self.criar(matricula_model) if matricula_model else None

    async def buscar_por_aluno_e_curso(self, aluno_id, curso_id) -> Optional[Matricula]:
        matricula_model = await MatriculaModel.get_or_none(aluno_id = aluno_id, curso_id = curso_id)

        return self.criar(matricula_model) if matricula_model else None
    

    async def listar(self) -> List[Matricula]:
        models = await MatriculaModel.all()
        return [self.criar(m) for m in models]


    async def listar_por_aluno(self, aluno_id : str) ->List[Matricula]:
        models = await MatriculaModel.filter(aluno_id = aluno_id)

        return [self.criar(m) for m in models]

    async def listar_por_curso(self, curso_id: str) -> List[Matricula]:
        models = await MatriculaModel.filter(curso_id = curso_id)

        return [self.criar(m) for m in models]


    async def atualizar(self, matricula : Matricula) -> Matricula:

        await MatriculaModel.filter(id = str(matricula.id)).update(
            ativo = matricula.ativo,
        )
        model = await MatriculaModel.get(id = str(matricula.id))
        return self.criar(model)


    async def deletar(self, matricula_id: str) -> None:

        await MatriculaModel.filter(id = matricula_id).delete()

       