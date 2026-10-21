from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExtendedKeyUsage(AdditionalDataHolder, Parsable):
    """
    The Custom Extended Key Usage definition
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The extended key usage (EKU) name that provides a user-friendly way to identify an EKU.
    name: Optional[str] = None
    # The object identifier (OID) of an extended key usage of a certificate. For example, '1.3.6.1.5.5.7.3.2' for client authentication.
    object_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExtendedKeyUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExtendedKeyUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExtendedKeyUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectIdentifier": lambda n : setattr(self, 'object_identifier', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("objectIdentifier", self.object_identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

