# Brain Agriculture Frontend

Interface web moderna para gerenciamento de produtores rurais desenvolvida com Next.js e TypeScript.

## 🚀 Tecnologias

- **Next.js 14** - Framework React com App Router
- **TypeScript** - Tipagem estática
- **Redux Toolkit** - Gerenciamento de estado
- **Styled Components** - CSS-in-JS
- **Recharts** - Gráficos interativos
- **React Hook Form** - Formulários
- **Axios** - Cliente HTTP
- **React Hot Toast** - Notificações

## 📋 Funcionalidades

- ✅ Dashboard com estatísticas e gráficos
- ✅ Cadastro completo de produtores rurais
- ✅ Validação de CPF/CNPJ em tempo real
- ✅ Gerenciamento de fazendas e culturas
- ✅ Validação de áreas (agricultável + vegetação ≤ total)
- ✅ Interface responsiva e moderna
- ✅ Notificações de sucesso/erro
- ✅ Navegação intuitiva

## 🛠️ Instalação

### Pré-requisitos

- Node.js 18+
- npm ou yarn

### Instalação

1. Clone o repositório
2. Navegue para a pasta do frontend:
```bash
cd frontend
```

3. Instale as dependências:
```bash
npm install
# ou
yarn install
```

4. Configure as variáveis de ambiente:
```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

> **Observação:**
> - Se você rodar o frontend via **Docker Compose**, a variável `NEXT_PUBLIC_API_URL` já será definida automaticamente como `http://localhost:8000` (não precisa criar `.env.local`).
> - Se rodar o frontend localmente (fora do Docker), crie o arquivo `.env.local` conforme acima.

5. Execute em modo de desenvolvimento:
```