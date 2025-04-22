"""
Este módulo contém as configurações do projeto, como os caminhos de entrada e saída.
"""

from pathlib import Path
from loguru import logger

# Caminhos de entrada e saída
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

# Configuração do log
logger.add("logs/debug.log", rotation="500 KB", retention="7 days", level="DEBUG")
