from pydantic import BaseModel


class CursoCreate(BaseModel):
    id:int
    titulo:str
    preco:float
    tipo:int
    desconto_percentual:float=0.0


class AlterarPrecoInput(BaseModel):
    preco: float


class CursoOut(BaseModel):
    id:int
    titulo:str
    preco:float
    tipo:int
    desconto_percentual:float=0.0
    


