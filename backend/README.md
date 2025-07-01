# Brain Agriculture API

API REST para gerenciamento de produtores rurais desenvolvida com FastAPI e PostgreSQL.

## 🚀 Tecnologias

- **Python 3.11**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **Docker** - Containerização
- **Pytest** - Testes unitários

## 📋 Funcionalidades

- ✅ Cadastro, edição e exclusão de produtores rurais
- ✅ Validação de CPF/CNPJ
- ✅ Gerenciamento de fazendas por produtor
- ✅ Controle de culturas por safra
- ✅ Validação de áreas (agricultável + vegetação ≤ total)
- ✅ Dashboard com estatísticas
- ✅ Logs para observabilidade
- ✅ Testes unitários

## 🛠️ Instalação

### Pré-requisitos

- Python 3.11+
- Docker e Docker Compose
- PostgreSQL (se não usar Docker)

### Com Docker (Recomendado)

1. Clone o repositório
2. Navegue para a pasta do backend:
```bash
cd backend
```

3. Execute com Docker Compose:
```bash
docker-compose up --build
```

A API estará disponível em: http://localhost:8000

### Sem Docker

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
```bash
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/brain_agriculture"
```

3. Execute a aplicação:
```bash
python main.py
```

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testes

Execute os testes unitários:

```bash
pytest tests/
```

## 📊 Endpoints Principais

### Produtores
- `POST /api/v1/produtores/` - Criar produtor
- `GET /api/v1/produtores/` - Listar produtores
- `GET /api/v1/produtores/{id}` - Buscar produtor
- `PUT /api/v1/produtores/{id}` - Atualizar produtor
- `DELETE /api/v1/produtores/{id}` - Deletar produtor

### Fazendas
- `POST /api/v1/produtores/{id}/fazendas/` - Criar fazenda
- `GET /api/v1/produtores/{id}/fazendas/` - Listar fazendas do produtor
- `GET /api/v1/fazendas/` - Listar todas as fazendas
- `PUT /api/v1/fazendas/{id}` - Atualizar fazenda
- `DELETE /api/v1/fazendas/{id}` - Deletar fazenda

### Culturas
- `POST /api/v1/fazendas/{id}/culturas/` - Criar cultura
- `GET /api/v1/fazendas/{id}/culturas/` - Listar culturas da fazenda
- `DELETE /api/v1/culturas/{id}` - Deletar cultura

### Dashboard
- `GET /api/v1/dashboard/` - Estatísticas gerais

## 🔧 Validações

- **CPF/CNPJ**: Validação completa com dígitos verificadores
- **Áreas**: Soma das áreas agricultável e vegetação não pode ultrapassar área total
- **Campos obrigatórios**: Todos os campos necessários são validados
- **Unicidade**: CPF/CNPJ deve ser único no sistema

## 📝 Logs

A aplicação possui logs detalhados para:
- Requisições HTTP
- Operações CRUD
- Erros e exceções
- Estatísticas do dashboard

## 🏗️ Arquitetura

```
backend/
├── app/
│   ├── __init__.py
│   ├── database.py      # Configuração do banco
│   ├── models.py        # Modelos SQLAlchemy
│   ├── schemas.py       # Schemas Pydantic
│   ├── crud.py          # Operações CRUD
│   └── api.py           # Endpoints da API
├── tests/
│   └── test_api.py      # Testes unitários
├── main.py              # Aplicação principal
├── requirements.txt     # Dependências
├── Dockerfile          # Container Docker
├── docker-compose.yml  # Orquestração
└── README.md           # Documentação
```

## 🚀 Deploy

A aplicação está configurada para deploy em containers Docker e pode ser facilmente implantada em:

- Docker Compose (desenvolvimento)
- Kubernetes
- AWS ECS
- Google Cloud Run
- Azure Container Instances

## 📄 Licença

Este projeto foi desenvolvido para o teste técnico da Brain Agriculture. 