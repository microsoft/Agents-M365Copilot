from enum import Enum

class HardwareConfigurationFormat(str, Enum):
    # Dell
    Dell = "dell",
    # Surface
    Surface = "surface",
    # Surface dock
    SurfaceDock = "surfaceDock",

