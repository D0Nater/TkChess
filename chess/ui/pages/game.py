"""Game page."""

from functools import partial
from tkinter import Button
from typing import TYPE_CHECKING, Any

from chess.lib.figures import PawnFigure
from chess.lib.schemas.enums.figure import FigureColor
from chess.lib.schemas.enums.game_map import CellColor
from chess.lib.utils.game_map import GameMap

from .abc import BasePage


if TYPE_CHECKING:
    from chess.ui.windows import BaseWindow


class GamePage(BasePage):
    """Game page."""

    def __init__(self, parent: Any, controller: "BaseWindow") -> None:
        BasePage.__init__(self, parent, controller)

        self._game_map = GameMap.generate(self._controller.config)
        self.__buttons_map = self._generate_map()

        self._step_color = FigureColor.WHITE
        self.__is_figure_selected = False
        self.__steps: list[list[int]] = []
        self.__selected_coords: list[int] | None = None

        self._update_buttons_map(grid=True)

    def _generate_map(self) -> list[list[Button]]:
        return [[Button(self) for _ in range(len(row))] for row in self._game_map.figures_map]

    def _update_buttons_map(self, grid: bool = False) -> None:
        for row_idx in range(len(self.__buttons_map)):
            for column_idx, figure in enumerate(self._game_map.figures_map[row_idx]):
                self.__buttons_map[row_idx][column_idx].configure(
                    image=figure.image if figure else "",
                    width=68 if figure else 6,
                    height=70 if figure else 3,
                    bg=CellColor.FIRST_CELL if (row_idx + column_idx) % 2 == 0 else CellColor.SECOND_CELL,
                    bd=1,
                    padx=10,
                    pady=10,
                    command=partial(self._click_field, row_idx, column_idx),
                )
                if grid:
                    self.__buttons_map[row_idx][column_idx].grid(row=row_idx, column=column_idx, ipadx=0, ipady=0)

    def _click_field(self, selected_row: int, selected_column: int) -> None:
        selected_btn = self.__buttons_map[selected_row][selected_column]
        selected_figure = self._game_map.figures_map[selected_row][selected_column]
        selected_coords: list[int] = [selected_row, selected_column]

        if selected_btn["bg"] in {CellColor.STEP_CELL, CellColor.KILL_STEP_CELL}:
            before_r, before_c = self.__selected_coords  # type: ignore[misc]
            before_btn = self.__buttons_map[before_r][before_c]
            before_figure = self._game_map.figures_map[before_r][before_c]

            selected_btn.configure(image=before_btn["image"], width=64, height=68)
            before_btn.configure(image="", width=6, height=3)

            self._game_map.figures_map[selected_row][selected_column] = before_figure
            self._game_map.figures_map[before_r][before_c] = None

            if isinstance(before_figure, PawnFigure):
                before_figure.step_done()

            self.__is_figure_selected = False
            self.__selected_coords = None
            self._change_step_color()
            self._game_map.reverce()
            self._update_buttons_map()
            return None
        elif selected_figure is None or selected_coords == self.__selected_coords:
            if self.__is_figure_selected:
                self._set_default_colors()
            self.__is_figure_selected = False
            self.__selected_coords = None
            return None
        elif self._step_color != selected_figure.color:
            return None
        elif self.__is_figure_selected:
            self._set_default_colors()

        self.__is_figure_selected = True
        self.__selected_coords = selected_coords
        self.__steps.clear()

        steps = selected_figure.get_steps(selected_row, selected_column, self._game_map.figures_map)

        for r, c in steps:
            if r >= 0 and r <= 7 and c >= 0 and c <= 7:
                figure_step = self._game_map.figures_map[r][c]
                btn_step = self.__buttons_map[r][c]

                if figure_step:
                    if selected_figure.color != figure_step.color:
                        btn_step.configure(bg=CellColor.KILL_STEP_CELL)
                else:
                    btn_step.configure(bg=CellColor.STEP_CELL)
                self.__steps.append([r, c])

    def _set_default_colors(self) -> None:
        for row, column in self.__steps:
            btn = self.__buttons_map[row][column]
            btn.configure(bg=(CellColor.FIRST_CELL if (row + column) % 2 == 0 else CellColor.SECOND_CELL))

    def _change_step_color(self) -> None:
        self._step_color = FigureColor.BLACK if self._step_color == FigureColor.WHITE else FigureColor.WHITE
