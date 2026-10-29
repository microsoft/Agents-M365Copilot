from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .setting_source import SettingSource

from .entity import Entity

@dataclass
class DeviceConfigurationConflictSummary(Entity, Parsable):
    """
    Conflict summary for a set of device configuration policies.
    """
    # The set of policies in conflict with the given setting
    conflicting_device_configurations: Optional[list[SettingSource]] = None
    # The set of settings in conflict with the given policies
    contributing_settings: Optional[list[str]] = None
    # The count of checkins impacted by the conflicting policies and settings
    device_checkins_impacted: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfigurationConflictSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationConflictSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceConfigurationConflictSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .setting_source import SettingSource

        from .entity import Entity
        from .setting_source import SettingSource

        fields: dict[str, Callable[[Any], None]] = {
            "conflictingDeviceConfigurations": lambda n : setattr(self, 'conflicting_device_configurations', n.get_collection_of_object_values(SettingSource)),
            "contributingSettings": lambda n : setattr(self, 'contributing_settings', n.get_collection_of_primitive_values(str)),
            "deviceCheckinsImpacted": lambda n : setattr(self, 'device_checkins_impacted', n.get_int_value()),
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
        writer.write_collection_of_object_values("conflictingDeviceConfigurations", self.conflicting_device_configurations)
        writer.write_collection_of_primitive_values("contributingSettings", self.contributing_settings)
        writer.write_int_value("deviceCheckinsImpacted", self.device_checkins_impacted)
    

