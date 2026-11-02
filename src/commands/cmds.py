# core
from core.exceptions import CommandNotFoundError

from .defaults import DEFAULT_COMMANDS
from .specials import SPECIAL_COMMANDS


def commands(params: list):
    """Trata os comandos de entrada do usuário"""

    cmd = params[0]

    if cmd in DEFAULT_COMMANDS:
        DEFAULT_COMMANDS[cmd]['handler']()

    elif cmd in SPECIAL_COMMANDS:
        SPECIAL_COMMANDS[cmd]['handler'](params)

    else:
        raise CommandNotFoundError(cmd)

