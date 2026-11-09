from enum import Enum

class SiteAccessType(str, Enum):
    Block = "block",
    Full = "full",
    Limited = "limited",

