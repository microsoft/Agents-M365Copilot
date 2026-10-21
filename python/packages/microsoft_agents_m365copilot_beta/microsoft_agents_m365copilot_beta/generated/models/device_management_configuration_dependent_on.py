from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceManagementConfigurationDependentOn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of parent setting/ parent setting option dependent on
    dependent_on: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of parent setting/ parent setting id dependent on
    parent_setting_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationDependentOn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationDependentOn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationDependentOn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dependentOn": lambda n : setattr(self, 'dependent_on', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentSettingId": lambda n : setattr(self, 'parent_setting_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("dependentOn", self.dependent_on)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("parentSettingId", self.parent_setting_id)
        writer.write_additional_data_value(self.additional_data)
    

