"""Main."""

from chess.core.config import AppConfig
from chess.ui.pages import GamePage
from chess.ui.windows import MainWindow


def start() -> None:
    """Start application."""
    app_config = AppConfig.from_env()
    app = MainWindow(app_config)
    app.show_page(GamePage)
    app.start()
