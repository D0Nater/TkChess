"""This file defines the game map enums."""

from .abc import BaseEnum


class CellColor(BaseEnum):
    """Cell color."""

    FIRST_CELL = "#b08f6f"
    SECOND_CELL = "#573411"
    STEP_CELL = "#6b5c4e"
    KILL_STEP_CELL = "#cc8d85"
