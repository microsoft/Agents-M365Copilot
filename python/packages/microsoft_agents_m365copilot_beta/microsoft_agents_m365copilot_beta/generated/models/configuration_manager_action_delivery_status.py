from enum import Enum

class ConfigurationManagerActionDeliveryStatus(str, Enum):
    # Pending to deliver the action to ConfigurationManager
    Unknown = "unknown",
    # Pending to deliver the action to ConfigurationManager
    PendingDelivery = "pendingDelivery",
    # Action is sent to ConfigurationManager Connector service (cloud)
    DeliveredToConnectorService = "deliveredToConnectorService",
    # Failed to send the action to ConfigurationManager Connector service (cloud)
    FailedToDeliverToConnectorService = "failedToDeliverToConnectorService",
    # Action is delivered to ConfigurationManager on-prem server
    DeliveredToOnPremisesServer = "deliveredToOnPremisesServer",

