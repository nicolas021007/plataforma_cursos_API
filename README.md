# Plataforma de Cursos API
 
API REST para gerenciamento de uma plataforma de cursos, desenvolvida em **FastAPI** seguindo os princípios de **Domain-Driven Design (DDD)**. Permite o cadastro de alunos, cursos e o controle de matrículas entre eles.
 
## 📋 Sobre o projeto
 
Este projeto foi desenvolvido como parte dos estudos em Análise e Desenvolvimento de Sistemas (ADS), com foco em aplicar uma arquitetura em camadas bem definida, separando regras de negócio, acesso a dados e exposição via API.
 
## 🚀 Tecnologias
 
- **[Python 3.12](https://www.python.org/)**
- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web para construção da API
- **[Tortoise ORM](https://tortoise.github.io/)** — ORM assíncrono para Python
- **[SQLite](https://www.sqlite.org/)** — banco de dados
- **[Pydantic](https://docs.pydantic.dev/)** — validação de dados e schemas
- **[Passlib](https://passlib.readthedocs.io/)** (bcrypt) — hash de senhas
- **[Uvicorn](https://www.uvicorn.org/)** — servidor ASGI
## 🏗️ Arquitetura
 
O projeto segue os princípios de **DDD (Domain-Driven Design)**, organizado nas seguintes camadas:
 
```
plataforma_cursos_API/
├── main.py                          # Ponto de entrada da aplicação
├── api/
│   └── routers/                     # Rotas HTTP (camada de apresentação)
│       ├── alunos.py
│       ├── cursos.py
│       └── matriculas.py
├── services/                        # Regras de aplicação e orquestração
│   ├── aluno_service.py
│   ├── curso_service.py
│   └── matricula_service.py
├── domain/                          # Entidades e regras de negócio puras
│   ├── aluno.py
│   ├── curso.py
│   ├── matricula.py
│   └── repositories/                # Contratos (interfaces abstratas)
│       ├── aluno_repositories.py
│       ├── curso_repositories.py
│       └── matricula_repositories.py
├── repositories/
│   └── tortoise/                    # Implementação concreta dos repositórios
│       ├── aluno_repo.py
│       ├── curso_repo.py
│       └── matricula_repo.py
├── schemas/                         # Schemas Pydantic (validação de entrada/saída)
│   ├── aluno.py
│   ├── curso.py
│   └── matricula.py
└── infraestructure/
    └── tortoise/
        ├── config.py                # Configuração de conexão com o banco
        └── models.py                # Models do Tortoise ORM
```
 
### Fluxo de uma requisição
 
```
Router → Service → Repository (interface) → Repository (Tortoise) → Model → Banco de dados
```
 
- **Router**: recebe a requisição HTTP, valida o schema de entrada e delega para a service.
- **Service**: contém as regras de aplicação (validações de negócio, orquestração entre repositórios).
- **Domain**: entidades puras, sem dependência de framework, com suas próprias regras de validação.
- **Repository**: abstrai o acesso a dados; a interface fica no domínio, a implementação usa Tortoise ORM.
- **Schemas**: definem o formato de entrada (`Create`/`Update`) e saída (`Response`) de cada recurso.
## 📦 Recursos da API
 
### Alunos (`/alunos`)
 
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/alunos/` | Cadastra um novo aluno |
| `GET` | `/alunos/` | Lista todos os alunos |
| `GET` | `/alunos/{id}` | Busca um aluno por ID |
| `PUT` | `/alunos/{id}` | Atualiza dados de um aluno |
| `DELETE` | `/alunos/{id}` | Remove um aluno |
 
**Regras de negócio:**
- E-mail deve ser único
- Nome deve ter no mínimo 3 caracteres
- Aluno deve ter no mínimo 18 anos
- Senha é armazenada com hash (bcrypt), nunca em texto puro
### Cursos (`/cursos`)
 
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/cursos/` | Cadastra um novo curso |
| `GET` | `/cursos/` | Lista todos os cursos |
| `GET` | `/cursos/{id}` | Busca um curso por ID |
| `PUT` | `/cursos/{id}` | Atualiza dados de um curso |
| `DELETE` | `/cursos/{id}` | Remove um curso |
 
**Regras de negócio:**
- Nome do curso deve ser único
- Nome deve ter no mínimo 3 caracteres
- Descrição deve ter no mínimo 10 caracteres
- Carga horária deve ser maior que zero
### Matrículas (`/matriculas`)
 
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/matriculas/` | Matricula um aluno em um curso |
| `GET` | `/matriculas/` | Lista todas as matrículas |
| `GET` | `/matriculas/aluno/{aluno_id}` | Lista os cursos de um aluno |
| `GET` | `/matriculas/curso/{curso_id}` | Retorna o curso com a lista de alunos matriculados |
| `GET` | `/matriculas/{id}` | Busca uma matrícula por ID |
| `PUT` | `/matriculas/{id}` | Ativa ou cancela uma matrícula |
| `DELETE` | `/matriculas/{id}` | Remove uma matrícula |
 
**Regras de negócio:**
- Aluno e curso precisam existir para criar a matrícula
- Um aluno não pode se matricular duas vezes no mesmo curso
- Respostas incluem o nome do aluno e do curso, não apenas os IDs
## ⚙️ Como executar o projeto
 
### Pré-requisitos
 
- Python 3.12+
- pip
### Passo a passo
 
1. Clone o repositório:
```bash
git clone https://github.com/nicolas021007/plataforma_cursos_API.git
cd plataforma_cursos_API
```
 
2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
 
3. Instale as dependências:
```bash
pip install fastapi uvicorn tortoise-orm aiosqlite "passlib[bcrypt]" pydantic[email]
```
 
4. Execute a aplicação:
```bash
uvicorn main:app --reload
```
 
5. Acesse a documentação interativa (Swagger):
```
http://127.0.0.1:8000/docs
```
 
O banco de dados SQLite (`db.sqlite3`) é criado automaticamente na primeira execução.
 
## 📄 Licença
 
Este projeto foi desenvolvido para fins de estudo no curso de Análise e Desenvolvimento de Sistemas.
 