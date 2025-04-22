"""
Módulo de processamento de textos ou tabelas extraídos de arquivos PDF.
"""

from typing import Any, List
import pandas as pd
from loguru import logger


def limpar_valor(valor: str) -> float:
    """
    Limpa e converte um valor monetário para float.

    Args:
        valor (str): Valor monetário como string.

    Returns:
        float: Valor convertido.
    """
    try:
        # Remove "R$", espaços e substitui vírgula por ponto
        valor = valor.replace("R$", "").replace(",", ".").strip()
        # Remove o sinal de negativo, se presente
        if valor.startswith("-"):
            return -float(valor[1:])
        return float(valor)
    except ValueError as exc:
        raise ValueError(f"Não foi possível converter o valor: {valor}") from exc


def processar_tabelas(tabelas: List[List[List[str]]]) -> pd.DataFrame:
    """
    Processa listas de tabelas em DataFrame com colunas formatadas.

    Args:
        tabelas (List[List[List[str]]]): Tabelas extraídas.

    Returns:
        pd.DataFrame: Dados estruturados com colunas nomeadas.
    """
    dados_formatados: List[List[Any]] = []

    for tabela in tabelas:
        for linha in tabela:
            if not linha or len(linha) < 5:
                logger.debug(f"Linha ignorada por formato inválido: {linha}")
                continue

            linha = [col.strip() if col else "" for col in linha]

            try:
                # Remove quebras de linha na coluna de data
                data = linha[0].replace("\n", " ")
                detalhes = linha[1]
                valor = limpar_valor(linha[2])
                saldo = limpar_valor(linha[3]) if linha[3] != "-" else None
                saldo_sacavel = limpar_valor(linha[4]) if linha[4] != "-" else None

                dados_formatados.append([data, detalhes, valor, saldo, saldo_sacavel])
            except (ValueError, IndexError) as err:
                logger.debug(f"Linha ignorada por erro de formato: {linha} | Erro: {err}")
                continue

    colunas = ["Data", "Detalhes", "Valor", "Saldo", "Saldo_Sacavel"]
    df = pd.DataFrame(dados_formatados, columns=colunas)
    logger.info(f"Total de linhas processadas: {len(df)}")
    return df
