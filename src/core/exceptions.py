

class CommandNotFoundError(Exception):
    def __init__(self, cmd):
        super().__init__(f"{cmd}: comando não encontrado! Tente >> help <<")
