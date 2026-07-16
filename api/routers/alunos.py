from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from services.aluno_service import AlunoService
from repositories.tortoise.aluno_repo import AlunoRepositoryTortoise
from schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse

router = APIRouter()

def get_aluno_service() -> AlunoService:

    repository = AlunoRepositoryTortoise()
    return AlunoService(repository)


@router.post(
    "/", 
    response_model = AlunoResponse,
    status_code = status.HTTP_201_CREATED
    )

async def criar_aluno(dados: AlunoCreate, service: AlunoService = Depends(get_aluno_service)):

    try:
        aluno = await service.registrar(dados)
        return aluno
    except ValueError as erro:
        raise HTTPException(status_code =status.HTTP_400_BAD_REQUEST, detail = str(erro))
    

@router.get("/", response_model =List[AlunoResponse])

async def listar_alunos(service: AlunoService = Depends(get_aluno_service)):

    return await service.listar()

@router.get("/{aluno_id}", response_model =AlunoResponse)

async def buscar_aluno(
    aluno_id: str, 
    service: AlunoService = Depends(get_aluno_service),
    ):
     try:
         return await service.buscar_por_id(aluno_id)
     
     except ValueError as erro:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(erro))
     
@router.put("/{aluno_id}", response_model = AlunoResponse)

async def atualizar_aluno(
    aluno_id : str,
    dados: AlunoUpdate,
    service : AlunoService = Depends(get_aluno_service)
):

    try:
        return await service.atualizar(aluno_id,dados)

    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail =str(erro))
    
@router.delete("/{aluno_id}", status_code = status.HTTP_204_NO_CONTENT)

async def deletar_aluno(
    aluno_id: str, 
    service: AlunoService = Depends(get_aluno_service),
):
    
    try:
        await service.deletar(aluno_id)

    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(erro))