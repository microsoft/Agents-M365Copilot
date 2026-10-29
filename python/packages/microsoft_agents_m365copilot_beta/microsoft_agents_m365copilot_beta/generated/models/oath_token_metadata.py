from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value import KeyValue

@dataclass
class OathTokenMetadata(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The enabled property
    enabled: Optional[bool] = None
    # The manufacturer property
    manufacturer: Optional[str] = None
    # The manufacturerProperties property
    manufacturer_properties: Optional[list[KeyValue]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The serialNumber property
    serial_number: Optional[str] = None
    # The tokenType property
    token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OathTokenMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OathTokenMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OathTokenMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value import KeyValue

        from .key_value import KeyValue

        fields: dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "manufacturerProperties": lambda n : setattr(self, 'manufacturer_properties', n.get_collection_of_object_values(KeyValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "tokenType": lambda n : setattr(self, 'token_type', n.get_str_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_collection_of_object_values("manufacturerProperties", self.manufacturer_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("tokenType", self.token_type)
        writer.write_additional_data_value(self.additional_data)
    

