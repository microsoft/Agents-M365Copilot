from enum import Enum

class DeviceManagementConfigurationControlType(str, Enum):
    # Default. UX uses default UX element base on setting type for the setting.
    Default = "default",
    # Display the setting in dropdown box.
    Dropdown = "dropdown",
    # Display text input in small text input.
    SmallTextBox = "smallTextBox",
    # Display text input in large text input.
    LargeTextBox = "largeTextBox",
    # Allow for toggle control type.
    Toggle = "toggle",
    # Allow for multiheader grid control type.
    MultiheaderGrid = "multiheaderGrid",
    # Allow for context pane control type.
    ContextPane = "contextPane",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

