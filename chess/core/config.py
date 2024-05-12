"""Global application configuration."""

from os import environ
from pathlib import Path
from typing import Any, Self

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """Base configuration."""

    model_config = SettingsConfigDict(env_file_encoding="utf-8", env_nested_delimiter="__", extra="ignore")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize config."""
        super().__init__(*args, **kwargs)

    @classmethod
    def from_env(cls) -> Self:
        """Create config from environment variables."""
        return cls(
            _env_file=environ.get("ENV_FILE", ".env"),
            _secrets_dir=environ.get("SECRETS_DIR"),
        )


class WindowConfig(BaseSettings):
    """Window config."""

    title: str
    width: int
    height: int


class UIConfig(BaseSettings):
    """UI config."""

    static_dir: Path


class AppConfig(BaseConfig):
    """App config."""

    window: WindowConfig
    ui: UIConfig
