
# core
from core.constants import SHORTS_JSON

# utils
from utils.functions import read_json, write_json

# ui
from ui.ui_cli import alert_ui


class Short:
    def __init__(self, params: list):
        self.SUB_COMMANDS: dict = {
            'add': {
                'desc': "Inicia o diálogo para adicionar novo atalho",
                'usage': "short add",
                'handler': self.add
            },
            'reset': {
                'desc': "Cria um arquivo shorts.json vazio",
                'usage': "short reset",
                'handler': self.reset
            }
        }

        self.manage(params)


    def add(self):
        """Adiciona um novo atalho"""

    def list_(self):
        """Lista os atalhos adicionados"""

    def remove(self):
        """Remove um atalho"""

    def reset(self):
        """Cria um novo arquivo shorts.json"""

        print("sss")

        data = {
            'app': {},
            'dir': {}
        }

        write_json(SHORTS_JSON, data)

    def help(self):
        """Exibe o menu de ajuda dos atalhos personalizados"""

    def manage(self, params: list):
        """Controla os comandos do Short"""

        sub_cmd = params[1]

        if sub_cmd in self.SUB_COMMANDS:
            self.SUB_COMMANDS[sub_cmd]['handler']()

        else:
            print("tente short help")


SPECIAL_COMMANDS = {
    'short': {
        'desc': "Sistema de atalhos personalizados",
        'usage': "short help",
        'handler': lambda params: Short(params)
    }
}
