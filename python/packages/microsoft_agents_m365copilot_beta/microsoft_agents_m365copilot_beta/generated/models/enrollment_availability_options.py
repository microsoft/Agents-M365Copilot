from enum import Enum

class EnrollmentAvailabilityOptions(str, Enum):
    # Device enrollment flow is shown to the end user with guided enrollment prompts
    AvailableWithPrompts = "availableWithPrompts",
    # Device enrollment flow is available to the end user without guided enrollment prompts
    AvailableWithoutPrompts = "availableWithoutPrompts",
    # Device enrollment flow is unavailable to the enduser
    Unavailable = "unavailable",

