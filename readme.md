# GitHub Data Pipeline

Pipeline de dados desenvolvido em Python para coleta, processamento, validação e armazenamento de informações de repositórios do GitHub.

O projeto consome a GitHub REST API, processa os dados recebidos e realiza o armazenamento em arquivos JSON e em um banco de dados PostgreSQL.

## Objetivo

Desenvolver um pipeline de dados aplicando conceitos de Engenharia de Dados, integração com APIs, validação de informações, persistência de dados e tratamento de erros.

## Tecnologias utilizadas

- **Python** — desenvolvimento do pipeline.
- **Requests** — consumo da API do GitHub.
- **PostgreSQL** — armazenamento dos dados.
- **Psycopg 3** — conexão e operações com o banco de dados.
- **JSON** — armazenamento complementar dos dados processados.
- **Pytest** — testes automatizados.
- **Logging** — monitoramento e registro de eventos.
- **Git e GitHub** — versionamento do projeto.

## Funcionalidades

- Consumo da GitHub REST API.
- Coleta de informações de repositórios Python.
- Validação e processamento dos dados recebidos.
- Armazenamento dos dados em arquivos JSON.
- Integração com PostgreSQL.
- Prevenção de registros duplicados.
- Tratamento de erros e gerenciamento de transações.
- Registro de eventos e erros utilizando Logging.
- Testes automatizados com Pytest.

## Estrutura do projeto

```text
github-data-pipeline/
│
├── data/
│   └── processed/
│       └── repositories.json
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── database.py
│   └── logging_config.py
│
├── tests/
│   └── test_pipeline.py
│
├── main.py
├── requirements.txt
├── readme.md
└── .gitignore
```

## Configuração e execução

### 1. Clone o repositório

```bash
git clone https://github.com/Dev-MarcoAntonio/github-data-pipeline.git
```

Entre na pasta:

```bash
cd github-data-pipeline
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o PostgreSQL

Crie um banco de dados chamado:

```sql
CREATE DATABASE github_data_pipeline;
```

Dentro dele, crie a tabela:

```sql
CREATE TABLE repositories (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL UNIQUE,
    language VARCHAR(100),
    stars INTEGER NOT NULL CHECK (stars >= 0),
    forks INTEGER NOT NULL CHECK (forks >= 0),
    collected_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Configure as variáveis de ambiente

No PowerShell, configure as credenciais da conexão:

```powershell
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="github_data_pipeline"
$env:DB_USER="postgres"
$env:DB_PASSWORD="SUA_SENHA"
```

**Importante:** substitua `SUA_SENHA` pela senha configurada no PostgreSQL. Não compartilhe ou envie suas credenciais ao GitHub.

### 6. Execute o pipeline

```bash
python main.py
```

Os dados serão processados e armazenados em:

- `data/processed/repositories.json`
- Banco PostgreSQL, na tabela `repositories`.

## Testes

Para executar os testes automatizados:

```bash
pytest
```

## Funcionamento do pipeline

1. Realiza uma requisição à GitHub REST API.
2. Obtém informações dos repositórios.
3. Valida os dados recebidos.
4. Processa e organiza as informações.
5. Salva os resultados em JSON.
6. Insere os registros no PostgreSQL.
7. Evita duplicações utilizando `ON CONFLICT`.
8. Registra eventos e possíveis erros nos arquivos de log.

## Armazenamento

Cada repositório processado possui as seguintes informações:

| Campo | Descrição |
|---|---|
| name | Nome do repositório |
| full_name | Nome completo do repositório |
| language | Linguagem principal |
| stars | Quantidade de estrelas |
| forks | Quantidade de forks |

## Autor

**Marco Antônio Loureiro dos Santos**

Estudante de Ciência da Computação na UNESC, interessado em Engenharia de Dados, Python e desenvolvimento de soluções envolvendo processamento e integração de dados.

GitHub: [Dev-MarcoAntonio](https://github.com/Dev-MarcoAntonio)