# core
from core.exceptions import CommandNotFoundError

# utils
from utils import entry
from utils import shutdown, clear, set_title

# ui
from ui import alert_ui
from ui.banners import Banners

# commands
from commands import CATEGORIES, DEFAULT_COMMANDS, SPECIAL_COMMANDS


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

                cmd = entries[0] # usa o primeiro parametro como comando principal

                if cmd in CATEGORIES:
                    CATEGORIES[cmd]['handler'](entries)

                elif cmd in DEFAULT_COMMANDS:
                    DEFAULT_COMMANDS[cmd]['handler']()

                elif cmd in SPECIAL_COMMANDS:
                    SPECIAL_COMMANDS[cmd]['handler'](entries)

                else:
                    raise CommandNotFoundError(cmd)

            except Exception as e:
                alert_ui('error', str(e))


if __name__ == '__main__':
    try:
        tool = Main()
        tool.startup()

    except KeyboardInterrupt:
        shutdown()
