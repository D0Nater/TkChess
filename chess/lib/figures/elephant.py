"""Elephant figure."""

from chess.core.config import UIConfig

from .base import BaseFigure, FigureColor, FigureRole


class ElephantFigure(BaseFigure):
    """Elephant figure."""

    def __init__(self, config: UIConfig, color: FigureColor):
        super().__init__(config, role=FigureRole.ELEPHANT, color=color)

    def get_steps(self, row: int, column: int, figures_map: list[list[BaseFigure | None]]) -> list[list[int]]:
        """Get available steps."""

        def _get_steps(r_action: int, c_action: int) -> list[list[int]]:
            r = row + r_action
            c = column + c_action
            steps = []

            while 0 <= r <= 7 and 0 <= c <= 7:
                figure = figures_map[r][c]
                if figure:
                    if figure.color != self.color:
                        steps.append([r, c])
                    break

                steps.append([r, c])
                r += r_action
                c += c_action

            return steps

        # up left
        steps1 = _get_steps(-1, -1)
        # up right
        steps2 = _get_steps(-1, 1)
        # down right
        steps3 = _get_steps(1, 1)
        # down left
        steps4 = _get_steps(1, -1)

        return self._create_steps(steps_map=[*steps1, *steps2, *steps3, *steps4], figures_map=figures_map)
