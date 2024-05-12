"""Resource path."""

import sys
from os import path


def resource_path(relative: str) -> str:
    """Get resource path."""
    if hasattr(sys, "_MEIPASS"):
        return path.join(sys._MEIPASS, relative)
    return path.join(relative)
