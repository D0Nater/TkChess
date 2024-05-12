"""Pawn figure."""

from chess.core.config import UIConfig

from .base import BaseFigure, FigureColor, FigureRole


class PawnFigure(BaseFigure):
    """Pawn figure."""

    def __init__(self, config: UIConfig, colour: FigureColor):
        super().__init__(config, role=FigureRole.PAWN, color=colour)
        self.__is_first_step = True

    def step_done(self) -> None:
        """Set is_first_step `False`."""
        self.__is_first_step = False

    def get_steps(self, row: int, column: int, figures_map: list[list[BaseFigure | None]]) -> list[list[int]]:
        """Get available steps."""
        # up left
        figure1 = figures_map[row - 1][column - 1] if column > 0 else None
        # up right
        figure2 = figures_map[row - 1][column + 1] if column < 7 else None

        steps = []

        if figures_map[row - 1][column] is None:
            # up first step
            steps.append([row - 1, column])
            if self.__is_first_step and figures_map[row - 2][column] is None:
                # up second step
                steps.append([row - 2, column])
        if figure1 is not None and figure1.color != self.color:
            # up left
            steps.append([row - 1, column - 1])
        if figure2 is not None and figure2.color != self.color:
            # up right
            steps.append([row - 1, column + 1])

        return self._create_steps(steps_map=steps, figures_map=figures_map)
