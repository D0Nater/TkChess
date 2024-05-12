"""Abstract base page class."""

from tkinter import Frame
from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from chess.ui.windows import BaseWindow


class BasePage(Frame):
    """Base page."""

    def __init__(self, parent: Any, controller: "BaseWindow", **kwargs: Any) -> None:
        Frame.__init__(self, parent, **kwargs)

        self._controller = controller
