from enum import Enum

class MlClassificationMatchTolerance(str, Enum):
    Exact = "exact",
    Near = "near",

