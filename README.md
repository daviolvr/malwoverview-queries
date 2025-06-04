# Passos para fazer as queries

## 1. Criar e ativar ambiente virtual
```bash
python3 -m venv .venv
. .venv/bin/activate
```

## 2. Instalar as dependências
```bash
pip install -r requirements.txt
```

## 3. Criar arquivo .env
```bash
touch .env
```

## 4. Inserir no arquivo .env
```bash
VIRUSTOTAL_APIKEY=
ALIENVAULT_APIKEY=
HYBRID_APIKEY=
TRIAGE_APIKEY=
```

Inserir no .env as chaves pra cada uma das APIs

## 5. Rodar o comando para fazer as queries
```bash
python3 main.py
```
