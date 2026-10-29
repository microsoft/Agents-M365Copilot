from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class HardwareConfigurationUserState(Entity, Parsable):
    """
    Contains properties for User state of the hardware configuration
    """
    # Error device count for specific user.
    error_device_count: Optional[int] = None
    # Failed device count for specific user.
    failed_device_count: Optional[int] = None
    # Last timestamp when the hardware configuration executed
    last_state_update_date_time: Optional[datetime.datetime] = None
    # Not applicable device count for specific user.
    not_applicable_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Pending device count for specific user.
    pending_device_count: Optional[int] = None
    # Success device count for specific user.
    successful_device_count: Optional[int] = None
    # Unknown device count for specific user.
    unknown_device_count: Optional[int] = None
    # User Principal Name (UPN).
    upn: Optional[str] = None
    # User Email address.
    user_email: Optional[str] = None
    # User name
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwareConfigurationUserState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwareConfigurationUserState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwareConfigurationUserState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "lastStateUpdateDateTime": lambda n : setattr(self, 'last_state_update_date_time', n.get_datetime_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "pendingDeviceCount": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "successfulDeviceCount": lambda n : setattr(self, 'successful_device_count', n.get_int_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_datetime_value("lastStateUpdateDateTime", self.last_state_update_date_time)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_int_value("successfulDeviceCount", self.successful_device_count)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
        writer.write_str_value("upn", self.upn)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userName", self.user_name)
    

