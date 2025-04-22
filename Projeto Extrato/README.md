# Projeto de Extração de Dados de PDFs

Este projeto realiza a extração de dados de arquivos PDF e os converte em arquivos CSV formatados.

# 📄 Extração de Tabelas de PDF para CSV com Python

Este projeto automatiza a extração de dados tabulares de arquivos PDF e os converte em arquivos CSV estruturados, prontos para análise.

## 🚀 Funcionalidades

- Leitura automática de PDFs com tabelas
- Processamento e limpeza dos dados
- Conversão para CSV formatado
- Logging com histórico completo
- Geração automática de múltiplos arquivos, se necessário

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- pdfplumber
- pandas
- loguru
- pathlib

## 📁 Estrutura do Projeto

- `data/input/`: PDFs de entrada #
- `data/output/`: CSVs gerados
- `src/`: Código fonte do projeto
- `tests/`: Testes unitários
- `main.py`: Script principal para rodar o projeto

- extrator-pdf-csv/
│
├── extrator/                  # Pacote principal
│   ├── __init__.py            # Torna a pasta um pacote Python
│   ├── extrator.py            # Código principal de extração
│   └── utils.py               # Funções auxiliares (opcional)
│
├── input/                     # PDFs de entrada
│   └── data/                  # Subpasta com arquivos PDF
│
├── output/                    # CSVs gerados
│
├── tests/                     # Testes automatizados
│   └── test_extrator.py       # Testes com pytest
│
├── README.md                  # Descrição do projeto
├── requirements.txt           # Dependências do projeto
├── .gitignore                 # Arquivos/pastas ignoradas pelo Git
└── main.py                    # Script para execução principal

