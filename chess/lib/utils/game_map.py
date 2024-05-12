"""Game map."""

from typing import Callable, Self

from chess.core.config import UIConfig
from chess.lib.figures import BaseFigure, ElephantFigure, HorseFigure, KingFigure, PawnFigure, QueenFigure, RookFigure
from chess.lib.schemas.enums.figure import FigureColor


class GameMap:
    """Game map."""

    def __init__(self, figures_map: list[list[BaseFigure | None]]):
        self.figures_map = figures_map

    @classmethod
    def generate(cls, config: UIConfig) -> Self:
        """Get GameMap instance."""
        first_row: Callable[[FigureColor], list[BaseFigure | None]] = lambda color: [
            RookFigure(config, color),
            HorseFigure(config, color),
            ElephantFigure(config, color),
            QueenFigure(config, color),
            KingFigure(config, color),
            ElephantFigure(config, color),
            HorseFigure(config, color),
            RookFigure(config, color),
        ]
        second_row: Callable[[FigureColor], list[BaseFigure | None]] = lambda color: [
            PawnFigure(config, color) for _ in range(8)
        ]
        empty_row: Callable[[], list[BaseFigure | None]] = lambda: [None for _ in range(8)]

        return cls(
            [
                first_row(FigureColor.BLACK),
                second_row(FigureColor.BLACK),
                empty_row(),
                empty_row(),
                empty_row(),
                empty_row(),
                second_row(FigureColor.WHITE),
                first_row(FigureColor.WHITE),
            ]
        )

    def reverce(self) -> None:
        """Reverce game map."""
        self.figures_map = [i[::-1] for i in self.figures_map[::-1]]
