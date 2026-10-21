from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_cleanup_rule_platform_type import DeviceCleanupRulePlatformType
    from .entity import Entity

from .entity import Entity

@dataclass
class ManagedDeviceCleanupRule(Entity, Parsable):
    """
    Define the rule when the admin wants the devices to be cleaned up.
    """
    # Indicates the description for the device clean up rule.
    description: Optional[str] = None
    # Define the platform type for which the admin wants to create the device clean up rule
    device_cleanup_rule_platform_type: Optional[DeviceCleanupRulePlatformType] = None
    # Indicates the number of days when the device has not contacted Intune. Valid values 0 to 2147483647
    device_inactivity_before_retirement_in_days: Optional[int] = None
    # Indicates the display name of the device cleanup rule.
    display_name: Optional[str] = None
    # Indicates the date and time when the device cleanup rule was last modified. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceCleanupRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceCleanupRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceCleanupRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_cleanup_rule_platform_type import DeviceCleanupRulePlatformType
        from .entity import Entity

        from .device_cleanup_rule_platform_type import DeviceCleanupRulePlatformType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceCleanupRulePlatformType": lambda n : setattr(self, 'device_cleanup_rule_platform_type', n.get_enum_value(DeviceCleanupRulePlatformType)),
            "deviceInactivityBeforeRetirementInDays": lambda n : setattr(self, 'device_inactivity_before_retirement_in_days', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_enum_value("deviceCleanupRulePlatformType", self.device_cleanup_rule_platform_type)
        writer.write_int_value("deviceInactivityBeforeRetirementInDays", self.device_inactivity_before_retirement_in_days)
        writer.write_str_value("displayName", self.display_name)
    

