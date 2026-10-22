from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_log_collection_request import AppLogCollectionRequest
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem

from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

@dataclass
class MobileAppTroubleshootingEvent(DeviceManagementTroubleshootingEvent, Parsable):
    """
    Event representing a users device application install status.
    """
    # Indicates collection of App Log Upload Request.
    app_log_collection_requests: Optional[list[AppLogCollectionRequest]] = None
    # Intune application identifier.
    application_id: Optional[str] = None
    # Device identifier created or collected by Intune.
    device_id: Optional[str] = None
    # Intune Mobile Application Troubleshooting History Item
    history: Optional[list[MobileAppTroubleshootingHistoryItem]] = None
    # Device identifier created or collected by Intune.
    managed_device_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier for the user that tried to enroll the device.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_collection_request import AppLogCollectionRequest
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem

        from .app_log_collection_request import AppLogCollectionRequest
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem

        fields: dict[str, Callable[[Any], None]] = {
            "appLogCollectionRequests": lambda n : setattr(self, 'app_log_collection_requests', n.get_collection_of_object_values(AppLogCollectionRequest)),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(MobileAppTroubleshootingHistoryItem)),
            "managedDeviceIdentifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("appLogCollectionRequests", self.app_log_collection_requests)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
        writer.write_str_value("userId", self.user_id)
    

