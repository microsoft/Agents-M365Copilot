from enum import Enum

class PluginSettingDisplayType(str, Enum):
    None_ = "none",
    Textbox = "textbox",
    Checkbox = "checkbox",
    Dropdown = "dropdown",
    UnknownFutureValue = "unknownFutureValue",

