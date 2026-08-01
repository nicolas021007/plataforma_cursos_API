from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from infraestructure.tortoise.config import TORTOISE_ORM
from api.routers.alunos import router as aluno_router
from api.routers.cursos import router as curso_router
from api.routers.matriculas import router as matricula_router


app = FastAPI(

    title = "Plataforma de Cursos",
    description ="API REST para gerenciamento de cursos, alunos e matriculas",
    version = "1.0.0",
)

app.include_router(aluno_router, prefix = "/alunos", tags =["Alunos"])
app.include_router(curso_router, prefix="/cursos", tags = ["Cursos"])
app.include_router( matricula_router, prefix = "/matriculas", tags = ["Matriculas"])


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = True,
)


@app.get("/")
async def root():
    return {"mensagem": "API Plataforma de Cursos no ar!"}