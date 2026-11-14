# utils
from utils import shutdown, clear

# ui
from ui import list_commands

# commands
from .specials import SPECIAL_COMMANDS



def list_handler(category):
    """Com base na categoria usa o list_commands para listar"""

    category = category[0]

    Categories = {
        'defaults': DEFAULT_COMMANDS,
        'specials': SPECIAL_COMMANDS
    }

    # Obtem o dict de comandos com base no primeiro parametro passado
    commands = Categories.get(category, DEFAULT_COMMANDS)

    # Finalmente usa o list_commands para listar organizadamente
    list_commands(name=category, commands=commands)


CATEGORIES = {
    'defaults': {
        'desc': "Comandos normais",
        'usage': "defaults",
        'handler': lambda category: list_handler(category)
    },
    'specials': {
        'desc': "Comandos especiais",
        'usage': "specials",
        'handler': lambda category: list_handler(category)
    }
}


def help_menu():
    """Comando de ajuda da ferramenta"""

    list_commands('Comandos separados por categoria', CATEGORIES)


DEFAULT_COMMANDS: dict = {
    'shutdown': {
        'desc': "Finaliza a ferramenta",
        'usage': "shutdown",
        'handler': shutdown
    },
    'clear': {
        'desc': "Limpa a tela da ferramenta",
        'usage': "clear",
        'handler': clear
    },
    'help': {
        'desc': "Exibe o menu de ajuda",
        'usage': "help",
        'handler': help_menu
    }
}

