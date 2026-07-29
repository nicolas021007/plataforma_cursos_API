from datetime import datetime
from uuid import UUID
from typing import Optional


class Curso:

    def __init__(
       self,
       id: UUID,
       nome: str,
       descricao: str,
       carga_horaria: int, 
       professor: Optional[str] = None,
       ativo : bool =True,
       data_criacao : Optional[datetime] = None,
    ):
       
        self._validar_nome(nome)
        self._validar_descricao(descricao)
        self._validar_carga_horaria(carga_horaria)

        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria
        self.professor = professor
        self.ativo = ativo
        self.data_criacao = data_criacao or datetime.now()



    def _validar_nome(self, nome : str) -> None:
        if len(nome.strip()) < 3:
            raise ValueError("O nome do curso deve ter no mínimo 3 caracteres.")
        
    def _validar_descricao(self, descricao:str) -> None:
        if len(descricao.strip()) >= 1000: 
            raise ValueError("Você usou todas as caracteres que podia usar.")
        

    def _validar_carga_horaria(self, carga_horaria: int) -> None :
        if carga_horaria <= 0 :
            raise ValueError("A carga horária deve ser maior que zero.")
        

    def atualizar_dados(
            self,
            nome : Optional[str] = None,
            descricao : Optional[str] =  None,
            carga_horaria : Optional[int] = None,
            professor : Optional[str] = None,

    ) -> None:
        if nome:
            self._validar_nome(nome)
            self.nome = nome

        if descricao:
            self._validar_descricao(descricao)
            self.descricao = descricao

        if carga_horaria:
            self._validar_carga_horaria(carga_horaria)
            self.carga_horaria = carga_horaria

        if professor:
            self.professor = professor

        
    def desativar(self) -> None:
        if not self.ativo:
            raise ValueError("Curso já está desativado.")
        self.ativo = False

    
    def ativar(self) -> None:
        if self.ativo:
            raise ValueError("Curso já está ativado.")
        self.ativo  = True

    def __repr__(self) -> str:

        return f"<Curso {self.nome} ({self.carga_horaria}h)> "

        
