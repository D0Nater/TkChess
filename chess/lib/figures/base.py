"""Abstract base figure."""

from abc import ABC, abstractmethod
from typing import Optional

from chess.core.config import UIConfig
from chess.lib.schemas.enums.figure import FigureColor, FigureRole
from chess.lib.utils.cache import FigureImage


class BaseFigure(ABC):
    """Abstract base figure."""

    def __init__(self, config: UIConfig, role: FigureRole, color: FigureColor):
        self.color = color
        self.role = role
        self.image = FigureImage.get_image(config, role, color)

    @abstractmethod
    def get_steps(self, row: int, column: int, figures_map: list[list[Optional["BaseFigure"]]]) -> list[list[int]]:
        """Get available steps."""
        raise NotImplementedError

    def _create_steps(
        self, steps_map: list[list[int]], figures_map: list[list[Optional["BaseFigure"]]]
    ) -> list[list[int]]:
        steps = []

        for r, c in steps_map:
            if r < 0 or c < 0:
                continue
            if r > 7 or c > 7:
                continue

            try:
                figure_step = figures_map[r][c]
            except IndexError:
                continue

            if figure_step and self.color == figure_step.color:
                continue

            steps.append([r, c])

        return steps
