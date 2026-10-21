from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class HardwarePasswordDetail(Entity, Parsable):
    """
    Device BIOS password information for devices with managed BIOS and firmware configuration, which provides device serial number, list of previous passwords, and current password.
    """
    # The current device's BIOS password. Supports: $filter, $select, $top, $OrderBy, $skip. This property is read-only.
    current_password: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of all the previous device BIOS passwords. Supports: $filter, $select, $top, $skip. This property is read-only.
    previous_passwords: Optional[list[str]] = None
    # The device serial number as defined by the device manufacturer. Supports: $filter, $select, $top, $OrderBy, $skip. This property is read-only.
    serial_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HardwarePasswordDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HardwarePasswordDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HardwarePasswordDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "currentPassword": lambda n : setattr(self, 'current_password', n.get_str_value()),
            "previousPasswords": lambda n : setattr(self, 'previous_passwords', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("serialNumber", self.serial_number)
    

