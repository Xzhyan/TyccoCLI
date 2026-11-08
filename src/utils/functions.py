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

        alert_ui('info', "para criar um novo json, use: short reset")

    except Exception as e:
        alert_ui('error', f"erro desconhecido: {e}")


def write_json(path: Path, data: dict):
    """Escreve dados no arquivo json do path passado"""

    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except Exception as e:
        alert_ui('error', f"erro desconhecido: {e}")
