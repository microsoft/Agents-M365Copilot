from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_management_constraint import DeviceManagementConstraint

from .device_management_constraint import DeviceManagementConstraint

@dataclass
class DeviceManagementSettingProfileConstraint(DeviceManagementConstraint, Parsable):
    """
    Constraint enforcing a given profile metadata
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceManagementSettingProfileConstraint"
    # The source of the entity
    source: Optional[str] = None
    # A collection of types this entity carries
    types: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettingProfileConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingProfileConstraint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettingProfileConstraint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_management_constraint import DeviceManagementConstraint

        from .device_management_constraint import DeviceManagementConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "types": lambda n : setattr(self, 'types', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("source", self.source)
        writer.write_collection_of_primitive_values("types", self.types)
    

