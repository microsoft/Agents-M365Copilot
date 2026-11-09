from enum import Enum

class WindowsAutoUpdateCatalogAppDeliveryOptimizationPriority(str, Enum):
    # Indicates that no delivery optimization priority is configured. The download uses normal background priority, which minimizes impact on other network activity. This is the default value when the property is omitted.
    NotConfigured = "notConfigured",
    # Indicates that the app content download uses foreground priority, which prioritizes the download over background network tasks. This may result in faster installation but increased network bandwidth consumption. In National Cloud environments, this value is accepted and stored but has no effect on device behavior.
    Foreground = "foreground",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

