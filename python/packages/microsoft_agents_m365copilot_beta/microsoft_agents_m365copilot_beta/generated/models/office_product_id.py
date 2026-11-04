from enum import Enum

class OfficeProductId(str, Enum):
    O365ProPlusRetail = "o365ProPlusRetail",
    O365BusinessRetail = "o365BusinessRetail",
    VisioProRetail = "visioProRetail",
    ProjectProRetail = "projectProRetail",

