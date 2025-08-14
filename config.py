from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8082
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "mcp_server.log"
    LOG_ROTATION: str = "500 MB"

    class Config:
        env_file = ".env"

settings = Settings()