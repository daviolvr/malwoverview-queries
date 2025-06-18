#!/bin/bash

echo "Criando ambiente virtual..."
python3 -m venv .venv

echo "Ativando ambiente virtual..."
source .venv/bin/activate

echo "Instalando dependências..."
pip install -r requirements.txt

if [ ! -f .env ]; then
    echo "Criando arquivo .env..."
    touch .env
    echo -e "VIRUSTOTAL_APIKEY=\nALIENVAULT_APIKEY=\nHYBRID_APIKEY=\nTRIAGE_APIKEY=" > .env
else
    echo "Arquivo .env já existe. Pulando criação"
fi

echo "Subindo containers com Docker Compose..."
docker-compose up -d

echo "Rodando o servidor Django..."
cd api/
python3 manage.py runserver &

# Aguarda o Django estar disponível na porta 8000
echo "Aguardando Django iniciar..."
until curl -s http://localhost:8000/ > /dev/null; do
  echo "Esperando servidor responder em http://localhost:8000..."
  sleep 2
done

cd ..

echo "Executando o client..."
python3 client.py
