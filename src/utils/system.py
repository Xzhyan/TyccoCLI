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


def entry_validator(message: str, validator: bool = None, error: str = "valor inválido!"):
    """Função de entradas controladas por validação"""

    while True:
        value = input(f'\n{message}{Colors.TEXT_ONE}').strip()

        if not value:
            alert_ui('error', "este campo não pode ficar vazio!")
            continue

        if validator and not validator(value):
            alert_ui('error', error)
            continue

        return value


def entry(normalize: bool = True) -> list:
    """Processa as entradas do usuário"""

    print(f'\n {Colors.UI_ONE}┌─({Colors.UI_TWO}{settings.TOOL_NAME}{Colors.UI_ONE})-[{Colors.UI_TWO}{USERNAME}{Colors.UI_ONE}]')
    entries = input(f" {Colors.UI_ONE}└───⋉ {Colors.TEXT_TWO}")

    if not entries:
        raise ValueError("nenhuma entrada foi inserida.")

    if normalize:
        entries = entries.lower()

    return entries.split()
