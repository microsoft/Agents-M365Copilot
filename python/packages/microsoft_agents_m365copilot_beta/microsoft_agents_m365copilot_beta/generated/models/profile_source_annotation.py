from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProfileSourceAnnotation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the source is the default one.
    is_default_source: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Names of properties that have data from this source.
    properties: Optional[list[str]] = None
    # The sourceId property
    source_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileSourceAnnotation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileSourceAnnotation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileSourceAnnotation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isDefaultSource": lambda n : setattr(self, 'is_default_source', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_primitive_values(str)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
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
        writer.write_bool_value("isDefaultSource", self.is_default_source)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("properties", self.properties)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_additional_data_value(self.additional_data)
    

