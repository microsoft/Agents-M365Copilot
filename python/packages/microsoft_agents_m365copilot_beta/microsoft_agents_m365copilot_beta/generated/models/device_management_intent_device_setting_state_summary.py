from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceManagementIntentDeviceSettingStateSummary(Entity, Parsable):
    """
    Entity that represents device setting state summary for an intent
    """
    # Number of compliant devices
    compliant_count: Optional[int] = None
    # Number of devices in conflict
    conflict_count: Optional[int] = None
    # Number of error devices
    error_count: Optional[int] = None
    # Number of non compliant devices
    non_compliant_count: Optional[int] = None
    # Number of not applicable devices
    not_applicable_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of remediated devices
    remediated_count: Optional[int] = None
    # Name of a setting
    setting_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementIntentDeviceSettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentDeviceSettingStateSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementIntentDeviceSettingStateSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "compliantCount": lambda n : setattr(self, 'compliant_count', n.get_int_value()),
            "conflictCount": lambda n : setattr(self, 'conflict_count', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "nonCompliantCount": lambda n : setattr(self, 'non_compliant_count', n.get_int_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "remediatedCount": lambda n : setattr(self, 'remediated_count', n.get_int_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
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
        writer.write_int_value("compliantCount", self.compliant_count)
        writer.write_int_value("conflictCount", self.conflict_count)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("nonCompliantCount", self.non_compliant_count)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("remediatedCount", self.remediated_count)
        writer.write_str_value("settingName", self.setting_name)
    

