from typing import Optional, List
from domain.curso import Curso
from domain.repositories.curso_repositories import  CursoRepository
from infraestructure.tortoise.models import CursoModel


class CursoRepositoryTortoise(CursoRepository):

    def criar(self, model: CursoModel) -> Curso:

        return Curso(
            id = model.id,
            nome = model.nome,
            descricao = model.descricao,
            carga_horaria=model.carga_horaria,
            professor = model.professor,
            ativo = model.ativo,
            data_criacao = model.data_criacao,
        )


    async def salvar(self, curso: Curso) -> Curso:
        model = await CursoModel.create(
            id = str(curso.id),
            nome = curso.nome,
            descricao = curso.descricao,
            carga_horaria = curso.carga_horaria,
            professor = curso.professor,
            ativo =curso.ativo,
        )

        return self.criar(model)
   
    async def buscar_por_id(self, curso_id: str) -> Optional[Curso]:
        curso_model = await CursoModel.get_or_none(id = curso_id)
        return self.criar(curso_model) if curso_model else None
    
    async def buscar_por_nome(self, nome: str ) -> Optional[Curso]:

        curso_model = await CursoModel.get_or_none(nome = nome )
        return self.criar(curso_model) if curso_model else None

    async def listar(self) -> List[Curso]:
        models = await CursoModel.all()
        return [self.criar(m) for m in models]

    async def atualizar(self, curso: Curso) -> Curso:
        await CursoModel.filter(id = str(curso.id)).update(
            nome = curso.nome,
            descricao = curso.descricao,
            carga_horaria = curso.carga_horaria,
            professor = curso.professor,
            ativo = curso.ativo,
        )

        model = await CursoModel.get(id = str(curso.id))
        return self.criar(model)

    async def deletar(self, curso_id: str) -> None:
        await CursoModel.filter(id = curso_id).delete()