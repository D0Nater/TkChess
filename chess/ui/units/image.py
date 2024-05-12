"""Game image."""

from os import path
from tkinter import PhotoImage
from typing import Self

from chess.lib.utils import resource_path


class GameImage(PhotoImage):
    """Game image."""

    @classmethod
    def from_file(cls, folder: str, filename: str) -> Self:
        """Get GameImage instance from file."""
        return cls(file=resource_path(path.join(folder, filename)))
