from enum import Enum

class KioskModeManagedHomeScreenPinComplexity(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Numeric values only.
    Simple = "simple",
    # Alphanumerical value.
    Complex = "complex",

