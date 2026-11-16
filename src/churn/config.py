from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_path: str = "artifacts/model.joblib"
    database_url: str | None = None
    log_level: str = "INFQ"

    model_config = {"env_file": ".env"}

settings = Settings()