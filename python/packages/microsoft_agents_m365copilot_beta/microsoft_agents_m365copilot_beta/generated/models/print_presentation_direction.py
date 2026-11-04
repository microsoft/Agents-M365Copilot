from enum import Enum

class PrintPresentationDirection(str, Enum):
    ClockwiseFromTopLeft = "clockwiseFromTopLeft",
    CounterClockwiseFromTopLeft = "counterClockwiseFromTopLeft",
    CounterClockwiseFromTopRight = "counterClockwiseFromTopRight",
    ClockwiseFromTopRight = "clockwiseFromTopRight",
    CounterClockwiseFromBottomLeft = "counterClockwiseFromBottomLeft",
    ClockwiseFromBottomLeft = "clockwiseFromBottomLeft",
    CounterClockwiseFromBottomRight = "counterClockwiseFromBottomRight",
    ClockwiseFromBottomRight = "clockwiseFromBottomRight",

