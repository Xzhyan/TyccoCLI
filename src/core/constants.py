import getpass
from pathlib import Path


# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Diretório de dados
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)

# Diretório de arquivos json
JSON_DIR = DATA_DIR / 'json'
JSON_DIR.mkdir(exist_ok=True)

# Aquivo json de atalhos
SHORTS_JSON = JSON_DIR / 'shorts.json'

# Usuário local
USERNAME = getpass.getuser()

