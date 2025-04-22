"""
Este módulo contém funções para extrair tabelas de arquivos PDF.
"""

from pathlib import Path
import pdfplumber
from loguru import logger


def extrair_tabelas(pasta_entrada: Path, arquivo_especifico: str = None) -> list:
    """
    Extrai tabelas de um arquivo PDF específico ou de todos os arquivos na pasta.

    Args:
        pasta_entrada (Path): Caminho para a pasta contendo os arquivos PDF.
        arquivo_especifico (str, opcional): Arquivo PDF a ser processado. Se None, processa todos.

    Returns:
        list: Lista de tabelas extraídas de cada página dos PDFs.
    """
    tabelas_extraidas = []

    # Define os arquivos a serem processados
    arquivos = (
        [pasta_entrada / arquivo_especifico]
        if arquivo_especifico
        else pasta_entrada.glob("*.pdf")
    )

    for pdf_file in arquivos:
        if not pdf_file.exists():
            logger.error(f"Arquivo não encontrado: {pdf_file}")
            continue

        logger.info(f"Lendo arquivo: {pdf_file.name}")
        try:
            with pdfplumber.open(pdf_file) as pdf:
                for pagina in pdf.pages:
                    tabelas = pagina.extract_tables({
                        "vertical_strategy": "lines",
                        "horizontal_strategy": "lines",
                        "intersection_tolerance": 5,
                    })
                    if tabelas:
                        logger.info(f"Tabelas encontradas na página {pagina.page_number}")
                        tabelas_extraidas.extend(tabelas)
                    else:
                        logger.warning(f"Nenhuma tabela encontrada na página {pagina.page_number}")
        except FileNotFoundError as e:
            logger.error(f"Arquivo não encontrado: {e}")
        except OSError as e:
            logger.error(f"Erro ao abrir o arquivo {pdf_file.name}: {e}")

    return tabelas_extraidas
