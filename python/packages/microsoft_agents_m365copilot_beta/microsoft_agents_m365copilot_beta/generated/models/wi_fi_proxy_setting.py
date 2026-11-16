from enum import Enum

class WiFiProxySetting(str, Enum):
    # Default. Indicates Wi-Fi Proxy is not set.
    None_ = "none",
    # Indicates Wi-Fi Proxy is set by manually specifying an address and port as well as an optional list of hostnames that are exculded. This value is not supported for AndroidWorkProfileWiFiConfigurations.
    Manual = "manual",
    # Indicates Wi-Fi Proxy is set automatically by providing the URL to a PAC (Proxy Auto Configuration) file which contains a list of proxy servers to use.
    Automatic = "automatic",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

