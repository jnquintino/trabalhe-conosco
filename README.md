# **Brain Agriculture - Teste Técnico v2**

Olá! Bem-vindo(a) ao nosso teste técnico. Estamos muito animados para conhecer mais sobre você, suas habilidades técnicas e sua forma de resolver problemas. Este teste foi pensado para ser um reflexo do que valorizamos em nosso time, e esperamos que você se sinta confortável e confiante durante o processo.

## **O que queremos avaliar?**

Nosso objetivo com este teste é entender melhor como você:

- Resolve problemas relacionados à lógica de programação e orientação a objetos.
- Interpreta requisitos de negócio e os transforma em soluções técnicas.
- Aplica boas práticas de desenvolvimento, com foco em código limpo, testável, de fácil manutenção e observável.
- Garante que o sistema seja escalável e confiável, principalmente ao lidar com grande volume de dados.
- Escreve documentações claras para facilitar a integração e manutenção por outros desenvolvedores ou clientes.

**Dica:** Imagine que você está criando uma aplicação que será utilizada por clientes, parceiros ou até mesmo por outros desenvolvedores. Queremos ver sua atenção aos detalhes!

## **O que você precisa desenvolver?**

A proposta é criar uma aplicação para gerenciar o cadastro de produtores rurais, com os seguintes dados:

- CPF ou CNPJ
- Nome do produtor
- Nome da fazenda (propriedade)
- Cidade
- Estado
- Área total da fazenda (em hectares)
- Área agricultável (em hectares)
- Área de vegetação (em hectares)
- Safras (ex: Safra 2021, Safra 2022)
- Culturas plantadas (ex.: Soja na Safra 2021, Milho na Safra 2021, Café na Safra 2022)

### **Requisitos de negócio**

1. Permitir o cadastro, edição e exclusão de produtores rurais.
2. Validar o CPF ou CNPJ fornecido pelo usuário.
3. Garantir que a soma das áreas agricultável e de vegetação não ultrapasse a área total da fazenda.
4. Permitir o registro de várias culturas plantadas por fazenda do produtor.
5. Um produtor pode estar associado a 0, 1 ou mais propriedades rurais.
6. Uma propriedade rural pode ter 0, 1 ou mais culturas plantadas por safra.
7. Exibir um dashboard com:
   - Total de fazendas cadastradas (quantidade).
   - Total de hectares registrados (área total).
   - Gráficos de pizza:
     - Por estado.
     - Por cultura plantada.
     - Por uso do solo (área agricultável e vegetação).

---

## **Tecnologias sugeridas**

Sabemos que você pode ter seu próprio estilo, mas aqui estão algumas tecnologias e boas práticas que valorizamos:

- **Conceitos**: SOLID, KISS, Clean Code, API Contracts, Testes, Arquitetura em camadas.
- **Documentações**: Para facilitar o entendimento do funcionamento do sistema, é importante incluir um README claro, uma especificação OpenAPI e, caso necessário, diagramas que ajudem a visualizar a arquitetura ou os processos.
- **Bônus**: Se conseguir disponibilizar a aplicação na nuvem e acessível via internet, será um diferencial!

### **Se você for desenvolvedor FRONTEND:**

- Utilize **TypeScript**.
- Utilize **ReactJS**.
- Use **Redux** para gerenciar o estado da aplicação.
  - Se preferir, você pode usar **Context API** como alternativa ou complemento ao Redux (opcional).
- Estruture dados "mockados" para simular cenários.
- Desenvolva testes unitários com **Jest** e **React Testing Library**.
- Estruture os componentes utilizando atomic design patterns.
- Utilize css in js com bibliotecas como **Styled Components** ou **Emotion**.
- Estruture o projeto como um microfrontend (opcional);

### **Se você for desenvolvedor BACKEND:**

- Desenvolva uma **API REST**.
- Utilize **Docker** para distribuir a aplicação.
- Utilize **Postgres** como banco de dados.
- Crie os endpoints necessários para atender os requisitos de negócio.
- Desenvolva testes unitários e integrados.
- Estruture dados "mockados" para testes.
- Inclua logs para garantir a observabilidade do sistema, facilitando o monitoramento e a identificação de possíveis problemas.
- Utilize um framework de ORM.

#### **Se você for desenvolvedor BACKEND Node:**

- Utilize **TypeScript**.
- Utilize **NestJS** ou **AdonisJS**

#### **Se você for desenvolvedor BACKEND Python:**

- Utilize **Python 3**.
- Utilize **Django**, **Flask** ou **FastAPI**.

### **Se você for desenvolvedor FULLSTACK:**

- Conclua tanto o FRONTEND quanto o BACKEND, garantindo a integração entre eles.

---

## **Como enviar seu projeto?**

Ao concluir o desenvolvimento, suba o código-fonte para um repositório no **GitHub** (ou outro provedor de sua escolha). Certifique-se de que o repositório seja público ou que possamos acessá-lo, e nos envie o link.

---

**Nota final:** Queremos que você aproveite esse desafio para mostrar suas habilidades, mas também para aprender e se divertir. Se tiver dúvidas ou precisar de alguma orientação durante o processo, estamos aqui para ajudar! Boa sorte! 🌟

---

## 🚀 Como rodar o projeto completo (Backend + Frontend)

### Pré-requisitos
- **Docker e Docker Compose** (recomendado)
- **Python 3.11+** (para rodar o backend localmente)
- **Node.js 18+** (para rodar o frontend)

### 🐳 **Opção 1: Docker Compose Completo (RECOMENDADO)**

**Subir todo o sistema com um comando:**
```bash
docker-compose up --build -d
```

**O que acontece:**
- ✅ **Banco de dados** (PostgreSQL) sobe e fica pronto
- ✅ **Backend Tests** executa todos os testes e para (exit 0 se passou)
- ✅ **Frontend Tests** executa todos os testes e para (exit 0 se passou)
- ✅ **Backend** (FastAPI) sobe com dados mockados automáticos
- ✅ **Frontend** (Next.js) sobe e fica disponível

**Acessos:**
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs

**Verificar status:**
```bash
docker-compose ps
```

**Ver logs dos testes:**
```bash
docker-compose logs backend-tests frontend-tests
```

**Parar tudo:**
```bash
docker-compose down
```

### 🔧 **Opção 2: Serviços Individuais**

#### 1. Subindo o banco de dados (PostgreSQL)

```bash
# Sobe apenas o banco de dados
docker-compose up db
```

O banco estará disponível em `localhost:5432` com:
- Usuário: `postgres`
- Senha: `postgres`
- Banco: `brain_agriculture`

#### 2. Rodando o Backend (FastAPI)

**Com Docker:**
```bash
# Sobe backend + banco
docker-compose up backend
```

**Localmente (fora do Docker):**
```bash
cd backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/brain_agriculture"
python main.py
```

- Documentação Swagger: http://localhost:8000/docs
- Documentação Redoc: http://localhost:8000/redoc

#### 3. Rodando o Frontend (Next.js)

**Com Docker:**
```bash
# Sobe frontend + backend + banco
docker-compose up frontend
```
Acesse: http://localhost:3000

**Localmente:**
```bash
cd frontend
npm install
npm run dev
```
Acesse: http://localhost:3000

Se quiser buildar para produção:
```bash
npm run build
npm start
```
Acesse: http://localhost:3000

#### 4. Rodando Testes

**Backend:**
```bash
# Via Docker
docker-compose up backend-tests

# Localmente
cd backend
pytest tests/
```

**Frontend:**
```bash
# Via Docker
docker-compose up frontend-tests

# Localmente
cd frontend
npm test
```

### 5. Inicialização Automática do Banco de Dados

**✨ Dados Mockados Automáticos**

O sistema foi projetado para sempre ter dados para trabalhar desde o primeiro start:

- **Script de inicialização**: `backend/init_db.py` insere automaticamente dados mockados no banco
- **Execução automática**: O Dockerfile executa o script antes de iniciar a aplicação
- **Dados incluídos**: 4 produtores, 5 fazendas e 15 culturas distribuídas em diferentes estados
- **Verificação inteligente**: Se já existem dados no banco, o script pula a inserção
- **Healthcheck**: Docker Compose garante que o banco esteja pronto antes de executar o script

**Dados mockados incluídos:**
- **João Silva** (SP): 2 fazendas com Soja, Milho, Feijão, Café e Laranja
- **Maria Santos** (SP): 1 fazenda com Cana-de-açúcar, Soja e Milho  
- **Pedro Oliveira** (MG): 1 fazenda com Soja, Milho, Algodão e Trigo
- **Ana Costa** (GO): 1 fazenda com Arroz, Feijão e Soja

**Vantagens desta abordagem:**
- ✅ Aplicação sempre funcional desde o primeiro start
- ✅ Dashboard com dados reais para demonstração
- ✅ Testes com dados consistentes
- ✅ Sem erros de "banco vazio" na primeira execução
- ✅ Dados distribuídos em diferentes estados para gráficos

### 6. Observações importantes
- O backend pode ser rodado localmente ou via Docker, mas o banco precisa estar rodando (pode ser o do Docker Compose).
- O frontend se comunica com o backend em `http://localhost:8000` (ajustável em `.env.local` se necessário).
- Para ambiente de produção, recomenda-se usar Docker para ambos ou deploy em serviços como Vercel (frontend) e AWS/GCP/Azure (backend).
- Os dados mockados são criados automaticamente ao iniciar o backend, mas podem ser removidos/ajustados conforme necessidade.

---

**Dúvidas ou problemas?**
- Verifique se as portas 5432 (Postgres), 8000 (API) e 3000 (Frontend) estão livres.
- Confira as variáveis de ambiente e dependências instaladas.
- Consulte os READMEs das pastas `backend/` e `frontend/` para detalhes específicos.

---

**Bom uso e bons testes!**

---

## 🧪 Testes Automatizados

O projeto possui **testes automatizados** tanto no backend quanto no frontend, garantindo a qualidade, robustez e confiabilidade das principais regras de negócio e componentes.

### ✨ **Execução Automática de Testes**

**🚀 Testes antes do Start (Docker)**

O sistema foi configurado para executar testes automaticamente antes de iniciar os serviços:

- **Backend**: Executa `pytest tests/` antes de iniciar a API
- **Frontend**: Executa `npm test` antes de iniciar o Next.js
- **Garantia**: Se os testes falharem, o serviço não inicia
- **Logs**: Resultados dos testes aparecem nos logs do Docker Compose

**Comandos para verificar testes:**
```bash
# Ver logs dos testes do backend
docker-compose logs backend-tests

# Ver logs dos testes do frontend  
docker-compose logs frontend-tests

# Executar apenas os testes
docker-compose up backend-tests frontend-tests
```

### Por que testar?
- Garante que as regras de negócio (validação de CPF/CNPJ, áreas, etc) funcionam corretamente.
- Evita regressões ao evoluir o sistema.
- Facilita a manutenção e a confiança no código.
- É um diferencial importante em processos seletivos e projetos profissionais.

### O que está coberto nos testes?

#### **Backend (Pytest)**
- Cadastro de produtor (com e sem fazenda/cultura)
- Validação de CPF/CNPJ (válido e inválido)
- Validação de áreas (agricultável + vegetação ≤ total)
- Duplicidade de CPF/CNPJ
- Listagem de produtores
- Dashboard (estatísticas)
- Erros esperados (422, 400, 404)

**Arquivo principal:**
- `backend/tests/test_api.py`

**Rodando os testes:**
```bash
cd backend
pytest tests/
```

#### **Frontend (Jest + Testing Library)**
- Validação de CPF/CNPJ e áreas (unitário)
- Renderização de componentes do dashboard
- Comportamento de formulários
- Feedback visual de erros

**Arquivos principais:**
- `frontend/src/utils/validation.test.ts`
- `frontend/src/components/Dashboard/DashboardStats.test.tsx`

**Rodando os testes:**
```bash
cd frontend
npm test
```

### Exemplos de cenários testados
- Não permite cadastrar produtor com CPF inválido
- Não permite cadastrar fazenda com soma de áreas inválida
- Exibe corretamente estatísticas no dashboard
- Valida e formata CPF/CNPJ no frontend
- Renderiza cards e gráficos do dashboard

### Onde encontrar os testes?
- **Backend:** `backend/tests/`
- **Frontend:** `frontend/src/**/*.test.ts(x)`

### Dicas para aumentar a cobertura
- Adicione mais testes para fluxos de erro, exclusão e edição.
- Teste componentes de formulário e integração frontend-backend.
- Use ferramentas como `pytest-cov` e `jest --coverage` para medir cobertura.

### Interpretação dos resultados
- Todos os testes devem passar (status 0) para garantir que o sistema está íntegro.
- Falhas indicam problemas de regra de negócio, integração ou regressão.

---

**Testes são essenciais para a qualidade do projeto!**
Se quiser aumentar a cobertura ou adicionar novos cenários, basta criar novos arquivos de teste seguindo os exemplos já existentes.

## 🖥️ Exemplos de Execução

### Backend rodando com sucesso

```bash
cd backend
python main.py
```

Saída esperada:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Acesse: http://localhost:8000

---

### Frontend rodando com sucesso

```bash
cd frontend
npm run dev
```

Saída esperada:
```
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
info  - Loaded env from .../.env.local
...
```

Acesse: http://localhost:3000

---

Esses exemplos comprovam que o backend e o frontend sobem corretamente e estão prontos para uso e testes.

## ✅ Rodando os testes antes da aplicação

### Testes do Backend

```bash
cd backend
pytest tests/
```

Saída esperada:
```
============================= test session starts =============================
collected 8 items

tests/test_api.py ........                                              [100%]

============================== 8 passed in 1.23s =============================
```

---

### Testes do Frontend

```bash
cd frontend
npm test
```

Saída esperada:
```
PASS src/utils/validation.test.ts
PASS src/components/Dashboard/DashboardStats.test.tsx
...
Test Suites: 2 passed, 2 total
Tests:       15 passed, 15 total
```

---

**Todos os testes passando! O sistema está pronto para uso.**

## 🐳 Subindo o Backend com Docker Compose (após rodar os testes)

Antes de subir o backend em produção/desenvolvimento, rode os testes para garantir que está tudo certo:

```bash
cd backend
pytest tests/
```

Saída esperada:
```
============================= test session starts =============================
collected 8 items

tests/test_api.py ........                                              [100%]

============================== 8 passed in 1.23s =============================
```

Se todos os testes passarem, suba o backend normalmente:

```bash
docker-compose up --build
```

A API estará disponível em: http://localhost:8000

## 🏃 Rodando todos os serviços juntos com Docker Compose

Você pode subir o banco de dados, rodar os testes automatizados e iniciar o backend simultaneamente com:

```bash
docker-compose up --build
```

**O que acontece:**
- O serviço `db` (PostgreSQL) sobe e fica disponível.
- O serviço `backend-tests` executa todos os testes do backend e encerra (exit 0 se passou, exit 1 se falhou). O resultado aparece no terminal.
- O serviço `backend` sobe e fica rodando normalmente (servidor FastAPI).

**Importante:**
- O backend não espera os testes terminarem para subir. Portanto, sempre confira o log do `backend-tests` no terminal.
- Se os testes falharem, corrija antes de usar o backend em produção.
- O container de testes para sozinho após rodar.

**Exemplo de comando:**
```bash
docker-compose up --build
```

**Para rodar só os testes:**
```bash
docker-compose up --build backend-tests
```

**Para rodar só o backend e o banco:**
```bash
docker-compose up --build db backend
```

Assim, você garante que todos os serviços necessários estão rodando e pode acompanhar o resultado dos testes automatizados diretamente no terminal!
