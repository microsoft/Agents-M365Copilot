from enum import Enum

class MacOSSystemExtensionType(str, Enum):
    # Enables driver extensions.
    DriverExtensionsAllowed = "driverExtensionsAllowed",
    # Enables network extensions.
    NetworkExtensionsAllowed = "networkExtensionsAllowed",
    # Enables endpoint security extensions.
    EndpointSecurityExtensionsAllowed = "endpointSecurityExtensionsAllowed",

