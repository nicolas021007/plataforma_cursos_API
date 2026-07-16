from uuid import uuid4
from typing import List, Optional
from passlib.context import CryptContext
from domain.aluno import Aluno
from domain.repositories.aluno_repositories import AlunoRepository
from schemas.aluno import AlunoCreate, AlunoUpdate

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated ="auto")

class AlunoService:

    def __init__(self, repository: AlunoRepository):
        self.repository = repository

    async def registrar(self, dados : AlunoCreate) -> Aluno:
        aluno_existente = await self.repository.buscar_por_email(dados.email)

        if aluno_existente:
            raise ValueError("Aluno com este email já existe.")
        
        senha_hash = pwd_context.hash(dados.senha)

        aluno = Aluno(
            id = uuid4(),
            nome = dados.nome,
            email = dados.email,
            senha_hash = senha_hash, 
            data_nascimento = dados.data_nascimento,
            telefone =dados.telefone,
        )

        return await self.repository.salvar(aluno)
    
    async def buscar_por_id(self, aluno_id: str) -> Aluno:

        aluno = await self.repository.obter_por_id(aluno_id)

        if not aluno:
            raise ValueError("Aluno não encontrado.")

        return aluno

    async def listar(self) -> List[Aluno]:
        return await self.repository.listar()

    
    async def atualizar(self, aluno_id: str, dados: AlunoUpdate) -> Aluno:

        aluno = await self.repository.obter_por_id(aluno_id)


        aluno.atualizar_dados(
            nome = dados.nome,
            telefone = dados.telefone
        )
        if dados.ativo is not None:
            if dados.ativo:
                aluno.ativar()
            else:
                aluno.desativar()

        return await self.repository.atualizar(aluno)
    
    async def deletar(self, aluno_id: str) -> None:

        await self.buscar_por_id(aluno_id)
        await self.repository.deletar(aluno_id)

    
    async def autenticar(self, email: str, senha: str) -> Optional[Aluno]:

        aluno =  await self.repository.obter_por_email(email)

        if not aluno:
            return None
        
        if not pwd_context.verify(senha,aluno.senha_hash):
            return None
        
        return aluno
