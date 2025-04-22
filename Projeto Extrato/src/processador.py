"""
Módulo de processamento de textos ou tabelas extraídos de arquivos PDF.
"""

from typing import List
import pandas as pd
from loguru import logger


def processar_tabelas(tabelas: List[List[List[str]]]) -> pd.DataFrame:
    """
    Processa listas de tabelas em DataFrames dinamicamente com base nas colunas encontradas.

    Args:
        tabelas (List[List[List[str]]]): Tabelas extraídas.

    Returns:
        pd.DataFrame: Dados estruturados.
    """
    dataframes = []

    for tabela in tabelas:
        # Remove linhas vazias
        tabela = [linha for linha in tabela if any(celula.strip() for celula in linha)]

        if not tabela:
            logger.debug("Tabela ignorada por estar vazia após limpeza.")
            continue

        # Usa a primeira linha como header, se possível
        headers = tabela[0]
        dados = tabela[1:] if len(tabela) > 1 else []

        try:
            df = pd.DataFrame(dados, columns=headers if all(headers) else None)
            dataframes.append(df)
        except ValueError as err:
            logger.warning(f"Erro ao criar DataFrame para a tabela: {tabela} | Erro: {err}")
            continue

    if not dataframes:
        logger.warning("Nenhuma tabela válida foi processada.")
        return pd.DataFrame()

    df_geral = pd.concat(dataframes, ignore_index=True)
    logger.info(f"Total de linhas processadas: {len(df_geral)}")
    return df_geral
