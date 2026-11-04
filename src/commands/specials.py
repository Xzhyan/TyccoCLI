
# core
from core.constants import SHORTS_JSON

# utils
from utils.functions import read_json


class Short:
    def __init__(self, params: list):
        self.cmds: dict = {
            'add': {
                'desc': "Inicia o diálogo para adicionar novo atalho",
                'usage': "short add",
                'handler': self.add
            }
        }

        self.manage(params)


    def add(self):
        """Adiciona um novo atalho"""

    def list_(self):
        """Lista os atalhos adicionados"""

    def remove(self):
        """Remove um atalho"""

    def help(self):
        """Exibe o menu de ajuda dos atalhos personalizados"""

    def manage(self, params: list):
        """Controla os comandos do Short"""

        data = read_json(SHORTS_JSON)

        


SPECIAL_COMMANDS = {
    'short': {
        'desc': "Sistema de atalhos personalizados",
        'usage': "short help",
        'handler': lambda params: Short(params)
    }
}
