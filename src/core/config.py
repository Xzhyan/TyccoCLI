from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da ferramenta"""

    # Informações da ferramenta
    TOOL_NAME: str = "Tycco"
    AUTHOR: str = "Zyandev"
    VERSION: str = "1.0"


settings = Settings()
