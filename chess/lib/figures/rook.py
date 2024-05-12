"""Rook figure."""

from chess.core.config import UIConfig

from .base import BaseFigure, FigureColor, FigureRole


class RookFigure(BaseFigure):
    """Rook figure."""

    def __init__(self, config: UIConfig, colour: FigureColor):
        super().__init__(config, role=FigureRole.ROOK, color=colour)

    def get_steps(self, row: int, column: int, figures_map: list[list[BaseFigure | None]]) -> list[list[int]]:
        """Get available steps."""

        def _get_steps(r_action: int, c_action: int) -> list[list[int]]:
            r = row + r_action
            c = column + c_action
            steps = []

            while r >= 0 and r <= 7 and c >= 0 and c <= 7:
                figure = figures_map[r][c]
                if figure:
                    if figure.color == self.color:
                        break
                    else:
                        steps.append([r, c])
                        break

                steps.append([r, c])
                r += r_action
                c += c_action

            return steps
        # up
        steps1 = _get_steps(-1, 0)
        # right
        steps2 = _get_steps(0, 1)
        # down
        steps3 = _get_steps(1, 0)
        #  left
        steps4 = _get_steps(0, -1)

        return self._create_steps(steps_map=[*steps1, *steps2, *steps3, *steps4], figures_map=figures_map)
