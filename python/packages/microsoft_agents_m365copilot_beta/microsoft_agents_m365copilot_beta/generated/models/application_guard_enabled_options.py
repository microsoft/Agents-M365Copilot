from enum import Enum

class ApplicationGuardEnabledOptions(str, Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Enabled For Edge
    EnabledForEdge = "enabledForEdge",
    # Enabled For Office
    EnabledForOffice = "enabledForOffice",
    # Enabled For Edge And Office
    EnabledForEdgeAndOffice = "enabledForEdgeAndOffice",

