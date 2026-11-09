from enum import Enum

class MacOSSoftwareUpdateCategory(str, Enum):
    # A critical update
    Critical = "critical",
    # A configuration data file update
    ConfigurationDataFile = "configurationDataFile",
    # A firmware update
    Firmware = "firmware",
    # All other update types
    Other = "other",

