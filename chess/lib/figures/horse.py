"""Horse figure."""

from chess.core.config import UIConfig

from .base import BaseFigure, FigureColor, FigureRole


class HorseFigure(BaseFigure):
    """Horse figure."""

    def __init__(self, config: UIConfig, color: FigureColor):
        super().__init__(config, role=FigureRole.HORSE, color=color)

    def get_steps(self, row: int, column: int, figures_map: list[list[BaseFigure | None]]) -> list[list[int]]:
        """Get available steps."""
        return [
            [row - 2, column - 1],
            [row - 2, column + 1],
            [row - 1, column + 2],
            [row + 1, column + 2],
            [row + 2, column + 1],
            [row + 2, column - 1],
            [row + 1, column - 2],
            [row - 1, column - 2],
        ]
