from enum import Enum

class DeviceManagementConfigurationStringFormat(str, Enum):
    # Indicates a string with no well-defined format expected.
    None_ = "none",
    # Indicates a string that is expected to be a valid email address.
    Email = "email",
    # Indicates a string that is expected to be a valid GUID.
    Guid = "guid",
    # Indicates a string that is expected to be a valid IP address.
    Ip = "ip",
    # Indicates a string that is base64 encoded.
    Base64 = "base64",
    # Indicates a string that is expected to be a valid URL.
    Url = "url",
    # Indicates a string that should refer to a version.
    Version = "version",
    # Indicates a string that is expected to be a valid XML.
    Xml = "xml",
    # Indicates a string that is expected to be a valid date.
    Date = "date",
    # Indicates a string that is expected to be a valid time.
    Time = "time",
    Binary = "binary",
    # Indicates a string that is expected to be a valid Regex string.
    RegEx = "regEx",
    # Indicates a string that is expected to be a valid JSON string.
    Json = "json",
    # Indicates a string that is expected to be a valid Datetime.
    DateTime = "dateTime",
    # Indicates a Windows SKU applicability value that maps to Intune.
    SurfaceHub = "surfaceHub",
    # String whose value is a bash script
    BashScript = "bashScript",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

