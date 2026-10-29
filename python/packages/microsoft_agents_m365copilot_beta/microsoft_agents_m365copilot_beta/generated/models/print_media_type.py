from enum import Enum

class PrintMediaType(str, Enum):
    Stationery = "stationery",
    Transparency = "transparency",
    Envelope = "envelope",
    EnvelopePlain = "envelopePlain",
    Continuous = "continuous",
    Screen = "screen",
    ScreenPaged = "screenPaged",
    ContinuousLong = "continuousLong",
    ContinuousShort = "continuousShort",
    EnvelopeWindow = "envelopeWindow",
    MultiPartForm = "multiPartForm",
    MultiLayer = "multiLayer",
    Labels = "labels",

