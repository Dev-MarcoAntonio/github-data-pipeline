# GitHub Data Pipeline

Pipeline de dados desenvolvido em Python para consumir a GitHub REST API, coletar informações de repositórios, validar e transformar os dados e armazenar os resultados em formato JSON.

O projeto tem como objetivo praticar conceitos de Engenharia de Dados, integração com APIs REST, processamento de dados, testes automatizados e organização de aplicações Python.

## Funcionalidades

- **Consumo de API:** consulta à GitHub REST API utilizando a biblioteca Requests.
- **Extração de dados:** coleta informações de até 30 repositórios Python com maior número de estrelas, conforme os critérios da consulta.
- **Validação de dados:** verifica campos obrigatórios e tipos de dados, descartando registros inválidos.
- **Processamento:** organiza e transforma os dados coletados em uma estrutura padronizada.
- **Armazenamento:** salva os dados processados em um arquivo JSON.
- **Logging:** registra informações sobre a execução do pipeline no terminal e em arquivo.
- **Tratamento de erros:** utiliza mecanismos de tratamento de exceções para lidar com falhas nas requisições HTTP.
- **Testes automatizados:** utiliza Pytest e mocks para validar as funcionalidades sem depender de chamadas reais à API durante os testes.

## Tecnologias utilizadas

- Python
- Requests
- JSON
- Pytest
- Logging
- Git e GitHub

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
│   └── logging_config.py
│
├── tests/
│   └── test_pipeline.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Dev-MarcoAntonio/github-data-pipeline.git
```

### 2. Acesse a pasta

```bash
cd github-data-pipeline
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute o pipeline

```bash
python main.py
```

Após a execução, os dados processados serão armazenados em:

```text
data/processed/repositories.json
```

Os registros de execução serão armazenados em:

```text
logs/pipeline.log
```

## Executando os testes

Para executar os testes automatizados, utilize:

```bash
python -m pytest -v
```

Os testes verificam funcionalidades como:

- Processamento e validação dos repositórios.
- Tratamento de dados inválidos.
- Respostas bem-sucedidas da API.
- Tratamento de erros HTTP e de conexão.
- Tratamento de respostas JSON inválidas.
- Salvamento dos dados processados.

## Fluxo do pipeline

```text
GitHub REST API
       |
       v
Fetch Repositories
       |
       v
Process and Validate
       |
       v
Save as JSON
       |
       v
Execution Logs
```

## Autor

**Marco Antônio Loureiro dos Santos**

Estudante de Ciência da Computação na UNESC, interessado em Engenharia de Dados, desenvolvimento Python, APIs e tecnologias relacionadas a dados.

- GitHub: [Dev-MarcoAntonio](https://github.com/Dev-MarcoAntonio)
- Projeto: [GitHub Data Pipeline](https://github.com/Dev-MarcoAntonio/github-data-pipeline)