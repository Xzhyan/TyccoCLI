from colorama import Fore as fg

# core
from core import settings
from core.constants import USERNAME

class Colors:
    """Esquema de cores do UI da ferramenta"""

    # Cores principais
    UI_ONE = fg.LIGHTGREEN_EX
    UI_TWO = fg.LIGHTWHITE_EX

    # Cores de textos
    TEXT_ONE = fg.LIGHTGREEN_EX
    TEXT_TWO = fg.LIGHTWHITE_EX
    TEXT_THREE = fg.WHITE

    # Cores dos alertas
    UI_SUCCESS = fg.GREEN
    UI_ERROR = fg.RED
    UI_INFO = fg.BLUE
    UI_WARNING = fg.YELLOW


def alert_ui(type_: str, text: str, line_brk: bool = True):
    """Imprime alertas padronizados na tela"""

    types: dict = {
        'succes': Colors.UI_SUCCESS,
        'error': Colors.UI_ERROR,
        'info': Colors.UI_INFO,
        'warning': Colors.UI_WARNING
    }

    alert_color = types.get(type_, Colors.UI_INFO)

    if line_brk: # usa um print() vazio para quebra de linha
        print()

    print(f'{alert_color}[{type_.upper()}] > {Colors.TEXT_TWO}{text}')


def list_commands(name: str, commands: dict):
    """Lista os comandos de forma organizada na ferramenta"""

    print('')
    print(f" {Colors.UI_ONE}┌─[ {Colors.TEXT_TWO}{name} {Colors.UI_ONE}]")

    for cmd, data in commands.items():
        print(f' {Colors.UI_ONE}│')
        print(f' {Colors.UI_ONE}├─┬─ {Colors.TEXT_THREE}nome: {Colors.TEXT_TWO}{cmd}')
        print(f' {Colors.UI_ONE}│ ├─ {Colors.TEXT_THREE}desc: {Colors.TEXT_TWO}{data['desc']}')
        print(f' {Colors.UI_ONE}│ └─ {Colors.TEXT_THREE}uso: {Colors.TEXT_TWO}{data['usage']}')
    
    print(f' {Colors.UI_ONE}└╼')

