from enum import Enum

class PrintColorConfiguration(str, Enum):
    BlackAndWhite = "blackAndWhite",
    Grayscale = "grayscale",
    Color = "color",
    Auto = "auto",

