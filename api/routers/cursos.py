from  fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from services.curso_service import CursoService
from repositories.tortoise.curso_repo import CursoRepositoryTortoise
from schemas.curso import CursoCreate, CursoUpdate, CursoResponse


router = APIRouter()


def get_curso_service() -> CursoService :
    repository = CursoRepositoryTortoise()
    return CursoService(repository)


@router.post(
    "/",
    response_model = CursoResponse,
    status_code= status.HTTP_201_CREATED,

)

async def criar_curso(
    dados: CursoCreate,
    service: CursoService = Depends(get_curso_service),
):

    try:
        curso = await service.registrar(dados)
        return curso
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str( erro))


@router.get("/", response_model= List[CursoResponse])

async def listar_cursos(
    service: CursoService = Depends(get_curso_service),
):
    return await service.listar()



@router.get("/{curso_id}", response_model = CursoResponse)

async def buscar_curso(
    curso_id: str,
    service: CursoService = Depends(get_curso_service),
):

    try:
        return await service.buscar_por_id(curso_id)
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(erro))


@router.put("/{curso_id}", response_model = CursoResponse)

async def  atualizar_curso(
    curso_id : str,
    dados: CursoUpdate,
    service: CursoService = Depends(get_curso_service),

):

    try:
        return await service.atualizar(curso_id, dados)

    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail= str(erro))


@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)

async def deletar_curso(
    curso_id : str,
    service: CursoService = Depends(get_curso_service)
):

    try:
        await service.deletar(curso_id)
    except ValueError as erro:
        raise HTTPException(status_code  = status.HTTP_404_NOT_FOUND, detail = str(erro))
