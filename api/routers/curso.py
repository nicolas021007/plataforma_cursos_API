from fastapi import APIRouter, HTTPException
from schemas.curso import CursoCreate, CursoOut, AlterarPrecoInput
from services.plataforma_services import (
    criar_curso,
    listar_cursos,
    buscar_curso,
    atualizar_preco
)

router = APIRouter(prefix="/curso", tags=["curso"])



@router.post("/", response_model=CursoOut)
def post_curso(data:CursoCreate):
    return criar_curso(data)

@router.get("/", response_model=list[CursoOut])
def get_cursos():
    return listar_cursos()

@router.get("/{id}", response_model=CursoOut)
def buscar_curso(id:int):
    curso = buscar_curso(id)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return  curso

@router.put("/{id}/preco", response_model = CursoOut)
def put_curso(id:int, data:AlterarPrecoInput):
    curso = atualizar_preco(id, data.preco)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return {"codigo": curso.id,
            "titulo": curso.titulo,
            "preço_final": curso.preco_final()
            }



@router.get("/{id}/preco_final")

def get_preco_final(id: int):   

    curso= buscar_curso(id)
    if not curso:
        raise HTTPException(status_code = 404, detail = "curso não encontrado")
    return {"codigo": curso.id,
            "titulo": curso.titulo}