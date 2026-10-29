from enum import Enum

class WindowsAppStartLayoutTileSize(str, Enum):
    # Hidden.
    Hidden = "hidden",
    # Small 1x1.
    Small = "small",
    # Medium 2x2.
    Medium = "medium",
    # Wide 4x2.
    Wide = "wide",
    # Large 4x4.
    Large = "large",

