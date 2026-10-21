from enum import Enum

class AppleDeviceDeliveryProtocol(str, Enum):
    # Default. Set if the client hasn't specified a value for an entity. Indicates the payload will be delivered to devices using Intune's default delivery protocol, which is Mobile Device Management (MDM). This protocol is not specific to the apps payload.
    Default = "default",
    # Indicates the payload will be delivered to devices using the Mobile Device Management (MDM) protocol. This protocol is not specific to the apps payload.
    MobileDeviceManagement = "mobileDeviceManagement",
    # Indicates the payload will be delivered to devices using the Declarative Device Management (DDM) protocol. This protocol is not specific to the apps payload.
    DeclarativeDeviceManagement = "declarativeDeviceManagement",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

