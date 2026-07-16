from datetime import date,datetime
from uuid import UUID
from typing import Optional


class Aluno:

    def __init__(
            self, 
            id: UUID,
            nome: str,
            email: str,
            senha_hash: str,
            data_nascimento: date,
            telefone: Optional[str] = None,
            ativo:bool = True,
            data_cadastro: Optional[datetime] = None
    ):
        
        self._validar_nome(nome)
        self._validar_idade(data_nascimento)

        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.ativo = ativo
        self.data_cadastro = data_cadastro


    def _validar_nome(self, nome:str) -> None:

            if len(nome.strip()) < 3: 
                raise ValueError(" O nome tem que ter no minímo 3 caracteres.")
            
    def _validar_idade(self, data_nascimento: date)-> None :

            idade = (date.today() - data_nascimento).days // 365

            if idade < 13:
                raise ValueError("O Aluno deve ter no minímo 13 anos.")  
        
    def atualizar_dados(self, nome: Optional[str] = None , telefone: Optional[str] = None)  -> None:

            if nome:

                self._validar_nome(nome)
                self.nome = nome
            
            if telefone:

                self.telefone = telefone
        
    def desativar(self) -> None:

            if not self.ativo:
                raise ValueError("Aluno já está desativado.")
            
            self.ativo = False


    def ativar(self) -> None:

            if self.ativo:
                raise ValueError("Aluno já está ativado.")
            
            self.ativo = True

    def __repr__(self) -> str:
     return f"<Aluno {self.nome} ({self.email})>"
            
