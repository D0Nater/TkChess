"""This file defines the figure enums."""

from .abc import BaseEnum


class FigureColor(BaseEnum):
    """Figure color."""

    WHITE = "white"
    BLACK = "black"


class FigureRole(BaseEnum):
    """Figure role."""

    KING = "king"
    QUEEN = "queen"
    ELEPHANT = "elephant"
    HORSE = "horse"
    ROOK = "rook"
    PAWN = "pawn"
