"""Cache."""

from chess.core.config import UIConfig
from chess.lib.schemas.enums.figure import FigureColor, FigureRole
from chess.ui.units.image import GameImage


class FigureImage:
    """Figure image."""

    _images: dict[str, GameImage] = {}

    @staticmethod
    def get_image(config: UIConfig, role: FigureRole, color: FigureColor) -> GameImage:
        """Get image from file."""
        filename = f"{color.value}/{role.value}.png"

        if filename not in FigureImage._images:
            FigureImage._images[filename] = GameImage.from_file(f"{config.static_dir}/figures", filename)

        return FigureImage._images[filename]
