from typing import Optional, List
from domain.aluno import Aluno
from domain.repositories.aluno_repositories import AlunoRepository
from infraestructure.tortoise.models import AlunoModel


class AlunoRepositoryTortoise(AlunoRepository):

    def criar(self, model: AlunoModel) -> Aluno:
        return Aluno (
            id = model.id,
            nome = model.nome,
            email = model.email,
            senha_hash = model.senha_hash,
            data_nascimento = model.data_nascimento,
            telefone = model.telefone,
            ativo = model.ativo, 
            data_cadastro = model.data_cadastro,
            
        )

    async def salvar(self, aluno: Aluno) -> Aluno:
        model = await AlunoModel.create(
            id = str(aluno.id),
            nome = aluno.nome,
            email = aluno.email,
            senha_hash = aluno.senha_hash,
            data_nascimento = aluno.data_nascimento,
            telefone = aluno.telefone,
            ativo = aluno.ativo,
            
        )
        return self.criar(model)
    
    async def buscar_por_id(self, aluno_id: str) -> Optional[Aluno]:

        aluno_model = await AlunoModel.get_or_none(id= aluno_id)
        return self.criar(aluno_model) if aluno_model else None
    

    async def buscar_por_email(self,email : str) -> Optional[Aluno]:

        aluno_model = await AlunoModel.get_or_none(email = email)

        return self.criar(aluno_model) if aluno_model else None

    async def listar(self) -> List[Aluno]:
        models = await AlunoModel.all()
        return [self.criar(m) for m in models]
    
    async def atualizar(self, aluno: Aluno) -> Aluno:

        await AlunoModel.filter(id = str (aluno.id)).update(
            nome = aluno.nome,
            telefone = aluno.telefone,
            ativo = aluno.ativo

        )
        model = await AlunoModel.get(id = str(aluno.id))
        return self.criar(model)
    
    async def deletar(self, aluno_id : str ) -> None:
        await AlunoModel.filter(id = aluno_id).delete()