from fastapi import APIRouter, Depends, HTTPException, status 
from typing import List

from services.matricula_service import MatriculaService
from repositories.tortoise.matricula_repo import MatriculaRepositoryTortoise
from repositories.tortoise.aluno_repo import AlunoRepositoryTortoise
from repositories.tortoise.curso_repo import CursoRepositoryTortoise
from schemas.matricula import MatriculaCreate, MatriculaUpdate, MatriculaResponse,CursoComAlunos

router = APIRouter()


def get_matricula_service() -> MatriculaService:
    repository = MatriculaRepositoryTortoise()
    aluno_repository = AlunoRepositoryTortoise()
    curso_repository = CursoRepositoryTortoise()

    return MatriculaService(repository,aluno_repository, curso_repository)


@router.post(
    "/",
    response_model= MatriculaResponse,
    status_code= status.HTTP_201_CREATED,

)

async def criar_matricula(
    dados: MatriculaCreate,
    service: MatriculaService = Depends(get_matricula_service),
):
    try: 
        matricula = await service.registrar(dados)
        return matricula
    except ValueError as erro:
        mensagem = str(erro)

        if "não encontrado" in mensagem:

            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= mensagem)
        
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail= mensagem)



@router.get("/", response_model= List[MatriculaResponse])

async def listar_matriculas(service: MatriculaService = Depends(get_matricula_service),):

    return await service.listar()




@router.get("/aluno/{aluno_id}", response_model= List[MatriculaResponse])

async def listar_matriculas_por_aluno(
    aluno_id: str,
    service : MatriculaService = Depends(get_matricula_service)):


    return await service.listar_por_aluno(aluno_id)




@router.get("/curso/{curso_id}", response_model = CursoComAlunos)
async def curso_com_alunos(
    curso_id: str,
    service: MatriculaService = Depends(get_matricula_service)
):

    try:
        return await service.curso_com_alunos(curso_id)
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(erro))


@router.get("/{matricula_id}", response_model= MatriculaResponse)
async def buscar_matricula(
    matricula_id: str,
    service: MatriculaService = Depends( get_matricula_service)
):

    try :
        return await service.buscar_por_id(matricula_id)
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail  = str(erro))


@router.put("/{matricula_id}", response_model = MatriculaResponse)
async def atualizar_matricula(
    matricula_id: str,
    dados: MatriculaUpdate,
    service: MatriculaService = Depends(get_matricula_service)
):

    try: 
        return await service.atualizar(matricula_id, dados)
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(erro))


@router.delete("/{matricula_id}", status_code = status.HTTP_204_NO_CONTENT)

async def deletar_matricula(
    matricula_id: str,
    service: MatriculaService = Depends(get_matricula_service)
):

    try:
        return await service.deletar(matricula_id)
    except ValueError as erro:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(erro))
