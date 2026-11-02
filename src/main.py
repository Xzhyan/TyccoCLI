# core
from core.exceptions import CommandNotFoundError

# utils
from utils import entry
from utils import shutdown, clear, set_title

# ui
from ui import alert_ui
from ui.banners import Banners

# commands
from commands import commands


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        clear()
        set_title("TyccoCLI")
        print(Banners.TOOL_LOGO)

        self.dispatch()

    def dispatch(self):
        while self.running:
            try:
                entries = entry()
                commands(entries)

            except CommandNotFoundError as e:
                alert_ui('error', str(e))

            except ValueError as e:
                alert_ui('error', str(e))

            except Exception as e:
                alert_ui('error', str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        shutdown()
