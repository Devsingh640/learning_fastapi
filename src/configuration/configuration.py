from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    APPLICATION_HOST:str = "0.0.0.0"
    APPLICATION_PORT:int = 8001
    APPLICATION_RELOAD:bool = True

    POSTGRESQL_HOST:str = "127.0.0.0"
    POSTGRESQL_PORT:int = 5432
    POSTGRESQL_DB:str = "test_db"
    POSTGRESQL_USERNAME: str = "admin"
    POSTGRESQL_PASSWORD: str = "Admin@123"

    REDIS_HOST:str = "127.0.0.0"
    REDIS_port:int = 6379
    REDIS_PASSWORD:str = "Admin@123"
    REDIS_DB:int = 0






settings = Settings()