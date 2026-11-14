
# core
from core.constants import SHORTS_JSON
from core.exceptions import MissingParametersError, SubcommandNotFoundError

# utils
from utils import read_json, write_json, entry_validator

# ui
from ui import alert_ui, Colors


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

        # verifica se o comando veio com parametros
        if len(params) <= 1:
            raise MissingParametersError(cmd=params[0])

        self.data = read_json(SHORTS_JSON)

        self.manage(params)


    def add(self):
        """Adiciona um novo atalho"""

        print(f'\n {Colors.UI_ONE}[ {Colors.TEXT_TWO}dir {Colors.TEXT_THREE}= atalho de diretório - {Colors.TEXT_TWO}app {Colors.TEXT_THREE}= atalho de aplicativo {Colors.UI_ONE}]')

        type_ = entry_validator(
            f" {Colors.UI_ONE}└ {Colors.TEXT_TWO}tipo do atalho (dir/app) > ",
            validator=lambda v: v.lower() in ('dir', 'app'),
            error="digite >> dir << ou >> app <<"
        )

        name = entry_validator(f" {Colors.UI_ONE}└ {Colors.TEXT_TWO}apelido do atalho > ")

        path = entry_validator(f" {Colors.UI_ONE}└ {Colors.TEXT_TWO}caminho completo do atalho > ")

        # salva os dados
        self.data[type_] = {
            'nane': name,
            'path': path
        }

        write_json(SHORTS_JSON, self.data)

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
            raise SubcommandNotFoundError(subcmd=sub_cmd)


SPECIAL_COMMANDS = {
    'short': {
        'desc': "Sistema de atalhos personalizados",
        'usage': "short help",
        'handler': lambda params: Short(params)
    }
}
