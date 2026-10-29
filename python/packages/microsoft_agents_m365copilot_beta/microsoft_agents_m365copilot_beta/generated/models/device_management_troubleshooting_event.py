from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
    from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
    from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

from .entity import Entity

@dataclass
class DeviceManagementTroubleshootingEvent(Entity, Parsable):
    """
    Event representing an general failure.
    """
    # A set of string key and string value pairs which provides additional information on the Troubleshooting event
    additional_information: Optional[list[KeyValuePair]] = None
    # Id used for tracing the failure in the service.
    correlation_id: Optional[str] = None
    # Time when the event occurred .
    event_date_time: Optional[datetime.datetime] = None
    # Event Name corresponding to the Troubleshooting Event. It is an Optional field
    event_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Object containing detailed information about the error and its remediation.
    troubleshooting_error_details: Optional[DeviceManagementTroubleshootingErrorDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementTroubleshootingEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleVppTokenTroubleshootingEvent".casefold():
            from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent

            return AppleVppTokenTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentTroubleshootingEvent".casefold():
            from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent

            return EnrollmentTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingEvent".casefold():
            from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

            return MobileAppTroubleshootingEvent()
        return DeviceManagementTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
        from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

        from .apple_vpp_token_troubleshooting_event import AppleVppTokenTroubleshootingEvent
        from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_collection_of_object_values(KeyValuePair)),
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "troubleshootingErrorDetails": lambda n : setattr(self, 'troubleshooting_error_details', n.get_object_value(DeviceManagementTroubleshootingErrorDetails)),
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
        writer.write_collection_of_object_values("additionalInformation", self.additional_information)
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_object_value("troubleshootingErrorDetails", self.troubleshooting_error_details)
    

