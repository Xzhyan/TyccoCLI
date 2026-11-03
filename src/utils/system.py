import subprocess, sys

# core
from core import settings
from core.constants import USERNAME

# ui
from ui import Colors, alert_ui


def shutdown():
    """Finaliza a ferramenta"""

    alert_ui('info', "Finalizando a ferramenta...")
    sys.exit()


def clear():
    """Limpa a tela ferramenta"""

    subprocess.run('cls', shell=True)


def set_title(title: str):
    """Seta um título para o janela CLI da ferramenta"""

    subprocess.run(f'title {title}', shell=True)


def entry(normalize: bool = True) -> list:
    """Processa as entradas do usuário"""

    print(f'\n {Colors.UI_ONE}┌─({Colors.UI_TWO}{settings.TOOL_NAME}{Colors.UI_ONE})-[{Colors.UI_TWO}{USERNAME}{Colors.UI_ONE}]')
    entries = input(f" {Colors.UI_ONE}└───⋉ {Colors.TEXT_TWO}")

    if not entries:
        raise ValueError("nenhuma entrada foi inserida.")

    if normalize:
        entries.lower()

    return entries.split()
