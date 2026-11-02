import getpass
from pathlib import Path


# Caminho absoluto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Arquivo .env de configurações
ENV_FILE = BASE_DIR / '.env'

# Diretório de dados
DATA_DIR = BASE_DIR / 'data'

# Usuário local
USERNAME = getpass.getuser()

