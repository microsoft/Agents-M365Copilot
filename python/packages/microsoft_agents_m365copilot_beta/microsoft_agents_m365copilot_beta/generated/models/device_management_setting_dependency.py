from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_constraint import DeviceManagementConstraint

@dataclass
class DeviceManagementSettingDependency(AdditionalDataHolder, Parsable):
    """
    Dependency information for a setting
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of constraints for the dependency setting value
    constraints: Optional[list[DeviceManagementConstraint]] = None
    # The setting definition ID of the setting depended on
    definition_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingDependency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingDependency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettingDependency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_constraint import DeviceManagementConstraint

        from .device_management_constraint import DeviceManagementConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "constraints": lambda n : setattr(self, 'constraints', n.get_collection_of_object_values(DeviceManagementConstraint)),
            "definitionId": lambda n : setattr(self, 'definition_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("constraints", self.constraints)
        writer.write_str_value("definitionId", self.definition_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

