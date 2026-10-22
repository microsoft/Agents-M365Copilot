from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsNotAutopilotReadyDevice(Entity, Parsable):
    """
    The user experience analytics Device not windows autopilot ready.
    """
    # The intune device's autopilotProfileAssigned.
    auto_pilot_profile_assigned: Optional[bool] = None
    # The intune device's autopilotRegistered.
    auto_pilot_registered: Optional[bool] = None
    # The intune device's azure Ad joinType.
    azure_ad_join_type: Optional[str] = None
    # The intune device's azureAdRegistered.
    azure_ad_registered: Optional[bool] = None
    # The intune device's name.
    device_name: Optional[str] = None
    # The intune device's managed by.
    managed_by: Optional[str] = None
    # The intune device's manufacturer.
    manufacturer: Optional[str] = None
    # The intune device's model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The intune device's serial number.
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsNotAutopilotReadyDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsNotAutopilotReadyDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsNotAutopilotReadyDevice()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "autoPilotProfileAssigned": lambda n : setattr(self, 'auto_pilot_profile_assigned', n.get_bool_value()),
            "autoPilotRegistered": lambda n : setattr(self, 'auto_pilot_registered', n.get_bool_value()),
            "azureAdJoinType": lambda n : setattr(self, 'azure_ad_join_type', n.get_str_value()),
            "azureAdRegistered": lambda n : setattr(self, 'azure_ad_registered', n.get_bool_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
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
        writer.write_bool_value("autoPilotProfileAssigned", self.auto_pilot_profile_assigned)
        writer.write_bool_value("autoPilotRegistered", self.auto_pilot_registered)
        writer.write_str_value("azureAdJoinType", self.azure_ad_join_type)
        writer.write_bool_value("azureAdRegistered", self.azure_ad_registered)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("serialNumber", self.serial_number)
    

