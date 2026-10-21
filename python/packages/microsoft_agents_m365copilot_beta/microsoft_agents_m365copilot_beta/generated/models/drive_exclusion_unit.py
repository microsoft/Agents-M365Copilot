from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .exclusion_unit_base import ExclusionUnitBase

from .exclusion_unit_base import ExclusionUnitBase

@dataclass
class DriveExclusionUnit(ExclusionUnitBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.driveExclusionUnit"
    # The unique identifier of the directory object (user) associated with the drive.
    directory_object_id: Optional[str] = None
    # The display name of the user associated with the drive.
    display_name: Optional[str] = None
    # The email address of the user associated with the drive.
    email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveExclusionUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveExclusionUnit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveExclusionUnit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .exclusion_unit_base import ExclusionUnitBase

        from .exclusion_unit_base import ExclusionUnitBase

        fields: dict[str, Callable[[Any], None]] = {
            "directoryObjectId": lambda n : setattr(self, 'directory_object_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
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
        writer.write_str_value("directoryObjectId", self.directory_object_id)
    

