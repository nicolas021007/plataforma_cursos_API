# Plataforma de Cursos API
 
API backend para gerenciamento de cursos e matrícula de alunos, desenvolvida em **Python** com **FastAPI**, seguindo os princípios de **Domain-Driven Design (DDD)**. O sistema permite cadastrar cursos e alunos, além de verificar e gerenciar as matrículas dos alunos nos cursos.
 
## 🧱 Arquitetura
 
O projeto é organizado em camadas, separando responsabilidades de forma clara:
 
```
plataforma_cursos_API/
├── api/               # Camada de entrada da aplicação (rotas/endpoints)
├── domain/            # Entidades e regras de negócio
├── infraestructure/   # Configuração de banco de dados e integrações externas
├── repositories/       # Acesso e persistência de dados
├── schemas/            # Modelos de validação e serialização (Pydantic)
├── services/            # Lógica de aplicação e orquestração das regras de negócio
├── main.py              # Ponto de entrada da aplicação
└── db.sqlite3            # Banco de dados local (SQLite)
```
 
O fluxo de dependências segue: **schemas → domain → services → repositories → routers**, mantendo o domínio isolado de detalhes de infraestrutura.
 
## 🚀 Tecnologias
 
- **Python 3**
- **FastAPI** — framework web para construção da API
- **SQLite** — banco de dados relacional local
- **Uvicorn** — servidor ASGI para rodar a aplicação
## ⚙️ Instalação e execução
 
### Pré-requisitos
 
- Python 3.10+ instalado
- Git
### 1. Clone o repositório
 
```bash
git clone https://github.com/nicolas021007/plataforma_cursos_API.git
cd plataforma_cursos_API
```
 
### 2. Crie e ative o ambiente virtual
 
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
 
### 3. Instale as dependências
 
```bash
pip install -r requirements.txt
```
 
> Caso o projeto ainda não tenha um `requirements.txt`, gere um com:
> ```bash
> pip freeze > requirements.txt
> ```
 
### 4. Execute a aplicação
 
```bash
uvicorn main:app --reload
```
 
A API estará disponível em: `http://127.0.0.1:8000`
 
Documentação interativa (Swagger):
`http://127.0.0.1:8000/docs`
 
## 📦 Funcionalidades
 
- Cadastro e gerenciamento de cursos
- Cadastro de alunos
- Matrícula de alunos em cursos, com verificação de vínculo entre aluno e curso
- Estrutura em camadas seguindo DDD
- Persistência local com SQLite
> Este projeto não implementa autenticação de usuários.
 
## 🗂 Status do projeto
 
Em desenvolvimento ativo.
 
## 👤 Autor
 
**Nicolas Rosa Santos**
Estudante de Análise e Desenvolvimento de Sistemas (ADS) — Estácio