#!/bin/bash

echo "Ativando ambiente virtual..."
source .venv/bin/activate

# Verifica se o .env existe
if [ ! -f .env ]; then
    echo "Criando arquivo .env..."
    touch .env
    echo "VIRUSTOTAL_APIKEY=" >> .env
    echo "ALIENVAULT_APIKEY=" >> .env
    echo "HYBRID_APIKEY=" >> .env
    echo "TRIAGE_APIKEY=" >> .env
    echo "MONGO_INITDB_ROOT_USERNAME=" >> .env
    echo "MONGO_INITDB_ROOT_PASSWORD=" >> .env
    echo "MONGO_INITDB_DATABASE=" >> .env
    echo "MONGO_HOST=" >> .env
    echo "MONGO_PORT=27017" >> .env
    echo "Arquivo .env criado. Preencha as variáveis antes de continuar."
    exit 1
else
    echo "Arquivo .env já existe. Pulando criação"
fi

echo "Subindo containers com Docker Compose..."
docker compose up -d

echo "Rodando o servidor Django..."
cd api
python3 manage.py runserver &
SERVER_PID=$!
cd ..

sleep 2  # Tempo para o servidor iniciar

echo "Executando o client..."
python3 client.py

# Encerrando o servidor após o client rodar (opcional)
echo "Parando o servidor Django..."
kill $SERVER_PID
