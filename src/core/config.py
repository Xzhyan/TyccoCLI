from pydantic_settings import BaseSettings, SettingsConfigDict

# constants
from .constants import ENV_FILE


class Settings(BaseSettings):
    """Configurações da ferramenta"""

    TOOL_NAME: str = "Tycco"
    AUTHOR: str = "Zyandev"
    VERSION: str = "1.0"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )


settings = Settings()
