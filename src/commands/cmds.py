# core
from core.exceptions import CommandNotFoundError

# ui
from ui.ui_cli import list_commands

# commands
from .defaults import DEFAULT_COMMANDS
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


def commands(params: list):
    """Trata os comandos de entrada do usuário"""

    cmd = params[0] # usa o primeiro parametro como comando principal

    if cmd in CATEGORIES:
        CATEGORIES[cmd]['handler'](params)

    elif cmd in DEFAULT_COMMANDS:
        DEFAULT_COMMANDS[cmd]['handler']()

    elif cmd in SPECIAL_COMMANDS:
        SPECIAL_COMMANDS[cmd]['handler'](params)

    else:
        raise CommandNotFoundError(cmd)

