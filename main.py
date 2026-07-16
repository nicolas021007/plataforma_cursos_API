from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from infraestructure.tortoise.config import TORTOISE_ORM
from api.routers.alunos import router as aluno_router


app = FastAPI(

    title = "Plataforma de Cursos",
    description ="API REST para gerenciamento de cursos, alunos e matriculas",
    version = "1.0.0",
)

app.include_router(aluno_router, prefix = "/alunos", tags =["Alunos"])
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas = True,
    add_exception_handlers = True,
)


@app.get("/")
async def root():
    return {"mensagem": "API Plataforma de Cursos no ar!"}