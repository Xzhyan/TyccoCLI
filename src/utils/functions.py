import json
from pathlib import Path


# ui
from ui import alert_ui


def read_json(path: Path) -> dict:
    """Lê e retorna os dados encontrados no json do path passado"""

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if len(data) == 0:
                raise ValueError(f"o arquivo {path} esta vazio")

            return data

    except FileNotFoundError:
        alert_ui('error', f"{path}: arquivo não encontrado")

    except Exception as e:
        alert_ui('error', f"erro desconhecido: {e}")

