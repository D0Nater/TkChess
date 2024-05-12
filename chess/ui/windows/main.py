"""Main window."""

from tkinter import Tk

from chess.core.config import AppConfig

from .abc import BaseWindow


class MainWindow(BaseWindow):
    """Main window."""

    def __init__(self, app_config: AppConfig) -> None:
        self.__root = Tk()
        BaseWindow.__init__(self, self.__root, app_config.ui)

        config = app_config.window

        self.__root.title(config.title)
        self.__root.geometry(
            "{width}x{height}+{x}+{y}".format(
                width=config.width,
                height=config.height,
                x=int((self.__root.winfo_screenwidth() / 2) - (config.width / 2)),
                y=int((self.__root.winfo_screenheight() / 2) - (config.height / 2)),
            )
        )
        self.__root.minsize(width=config.width, height=config.height)
        self.__root.maxsize(width=config.width, height=config.height)
        self.__root.resizable(False, False)

    def start(self) -> None:
        """Start application."""
        try:
            self.__root.mainloop()
        except KeyboardInterrupt:
            pass
