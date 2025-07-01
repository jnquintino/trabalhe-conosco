FROM node:18-alpine

WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./
COPY jest.config.js ./
COPY jest.setup.js ./
COPY tsconfig.json ./
COPY next.config.js ./

# Instalar dependências
RUN npm ci

# Copiar código fonte
COPY . .

# Expor porta
EXPOSE 3000

# Script de inicialização para produção
CMD ["sh", "-c", "npm run build && npm start"] 