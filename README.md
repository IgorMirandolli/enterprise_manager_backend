# Enterprise Manager Backend

Backend do projeto Enterprise Manager, construido com FastAPI e MySQL.

## Como rodar localmente

Entre na pasta do backend:

```powershell
cd enterprise_manager_backend
```

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

Crie o arquivo de ambiente:

```powershell
copy .env.example .env
```

Edite o valor de `DATABASE_URL` no arquivo `.env` com a senha correta do seu MySQL.

Inicie a API:

```powershell
uvicorn app.main:app --reload
```

Depois acesse:

```text
http://127.0.0.1:8000/docs
```

## Estrutura

```text
app/
  api/            Rotas HTTP da API
  core/           Configuracoes centrais
  db/             Conexao com banco e base do SQLAlchemy
  models/         Models ORM
  repositories/   Acesso a dados
  schemas/        Schemas Pydantic
  services/       Regras de negocio
tests/            Testes automatizados
migrations/       Migrations do Alembic
```

