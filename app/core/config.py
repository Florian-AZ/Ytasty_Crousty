"""Configuration lue dans les variables d'environnement (ou le fichier .env)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Parametres de l'application."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql+psycopg://ytasty:ytasty@db:5432/ytasty"
    jwt_secret_key: str = "change-me-en-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60


settings = Settings()
