# utils
from utils import shutdown, clear


def help_menu():
    """Menu de ajuda da ferramenta"""

    pass


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

