"""Abstract base window class."""

from typing import TYPE_CHECKING, Any

from chess.core.config import UIConfig


if TYPE_CHECKING:
    from chess.ui.pages import BasePage


class BaseWindow:
    """Base window."""

    def __init__(self, parent: Any, config: UIConfig) -> None:
        self._parent = parent
        self.config = config
        self.__pages: dict[Any, "BasePage"] = {}

    def show_page(self, page: Any, parent: Any = None, is_new: bool = True, *args: Any, **kwargs: Any) -> None:
        """Show page."""
        if parent is None:
            parent = self._parent
        if is_new or page not in self.__pages:
            self.__init__page(page, parent, *args, **kwargs)

        frame = self.__pages[page]
        frame.tkraise()

    def __init__page(self, page: Any, parent: Any, *args: Any, **kwargs: Any) -> None:
        frame: "BasePage" = page(parent, self, *args, **kwargs)
        self.__pages[page] = frame
        frame.pack(expand=True)
