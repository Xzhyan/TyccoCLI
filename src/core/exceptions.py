

class CommandNotFoundError(Exception):
    def __init__(self, cmd):
        super().__init__(f"{cmd}: comando não encontrado! Tente >> help <<")


class MissingParametersError(Exception):
    def __init__(self, cmd):
        super().__init__(f"{cmd}: esse comando utiliza mais parâmetros, tente >> help <<")


class SubcommandNotFoundError(Exception):
    def __init__(self, subcmd):
        super().__init__(f"{subcmd}: parametro/subcomando errado, tente >> help <<")
