from enum import Enum

class SiteTemplateType(str, Enum):
    Sitepagepublishing = "sitepagepublishing",
    Sts = "sts",
    UnknownFutureValue = "unknownFutureValue",

