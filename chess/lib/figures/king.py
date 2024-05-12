"""King figure."""

from chess.core.config import UIConfig

from .base import BaseFigure, FigureColor, FigureRole


class KingFigure(BaseFigure):
    """King figure."""

    def __init__(self, config: UIConfig, color: FigureColor):
        super().__init__(config, role=FigureRole.KING, color=color)

    def get_steps(self, row: int, column: int, figures_map: list[list[BaseFigure | None]]) -> list[list[int]]:
        """Get available steps."""
        return self._create_steps(
            steps_map=[
                [row - 1, column - 1],
                [row - 1, column],
                [row - 1, column + 1],
                [row, column - 1],
                [row, column + 1],
                [row + 1, column - 1],
                [row + 1, column],
                [row + 1, column + 1],
            ],
            figures_map=figures_map,
        )
