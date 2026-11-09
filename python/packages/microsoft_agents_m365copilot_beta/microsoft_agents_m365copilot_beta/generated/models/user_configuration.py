from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .structured_data_entry import StructuredDataEntry

from .entity import Entity

@dataclass
class UserConfiguration(Entity, Parsable):
    # Arbitrary binary data.
    binary_data: Optional[bytes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Key-value pairs of supported data types.
    structured_data: Optional[list[StructuredDataEntry]] = None
    # Binary data for storing serialized XML.
    xml_data: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .structured_data_entry import StructuredDataEntry

        from .entity import Entity
        from .structured_data_entry import StructuredDataEntry

        fields: dict[str, Callable[[Any], None]] = {
            "binaryData": lambda n : setattr(self, 'binary_data', n.get_bytes_value()),
            "structuredData": lambda n : setattr(self, 'structured_data', n.get_collection_of_object_values(StructuredDataEntry)),
            "xmlData": lambda n : setattr(self, 'xml_data', n.get_bytes_value()),
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
        writer.write_bytes_value("binaryData", self.binary_data)
        writer.write_collection_of_object_values("structuredData", self.structured_data)
        writer.write_bytes_value("xmlData", self.xml_data)
    

