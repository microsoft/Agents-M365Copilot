from enum import Enum

class PluginCatalogScope(str, Enum):
    None_ = "none",
    User = "user",
    Workspace = "workspace",
    Tenant = "tenant",
    Global_ = "global",
    GeoGlobal = "geoGlobal",
    UserWorkspace = "userWorkspace",
    UnknownFutureValue = "unknownFutureValue",

