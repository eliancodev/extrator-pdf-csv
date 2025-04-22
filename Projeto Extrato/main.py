"""
Script principal: extração e processamento de dados de PDFs para CSV.
"""

import sys
from pathlib import Path
import pandas as pd
from loguru import logger
from src.extrator import extrair_tabelas
from src.processador import processar_tabelas
from src.config import INPUT_DIR, OUTPUT_DIR

RESULTADO_CSV = "transacoes_formatadas.csv"


def salvar_csv(dataframe: pd.DataFrame, caminho_saida: Path) -> None:
    """
    Salva um DataFrame como CSV, evitando sobrescrever arquivos existentes.

    Args:
        dataframe (pd.DataFrame): Dados estruturados.
        caminho_saida (Path): Caminho completo do arquivo CSV.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Verifica se o arquivo já existe e adiciona um sufixo único
    if caminho_saida.exists():
        contador = 1
        while True:
            novo_caminho = caminho_saida.with_stem(f"{caminho_saida.stem}_{contador}")
            if not novo_caminho.exists():
                caminho_saida = novo_caminho
                break
            contador += 1

    dataframe.to_csv(caminho_saida, index=False, encoding="utf-8-sig", sep=";")
    logger.success(f"Arquivo CSV salvo em: {caminho_saida}")


def main() -> None:
    """
    Executa o fluxo principal:
    - Extrai tabelas
    - Processa dados
    - Salva em CSV
    """
    # Verifica se um arquivo específico foi passado como argumento
    arquivo_especifico = sys.argv[1] if len(sys.argv) > 1 else None

    logger.info("Iniciando extração de tabelas...")
    tabelas = extrair_tabelas(INPUT_DIR, arquivo_especifico)

    if not tabelas:
        logger.warning("Nenhuma tabela foi extraída dos PDFs.")
        return

    logger.info("Processando as tabelas extraídas...")
    df_tabelas = processar_tabelas(tabelas)

    if df_tabelas.empty:
        logger.warning("O DataFrame está vazio após o processamento.")
        return

    salvar_csv(df_tabelas, OUTPUT_DIR / RESULTADO_CSV)


if __name__ == "__main__":
    main()
