from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_transformation import CustomClaimTransformation

from .custom_claim_transformation import CustomClaimTransformation

@dataclass
class ExtractTransformation(CustomClaimTransformation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.extractTransformation"
    # The type of extract transformation to apply.
    type: Optional[str] = None
    # The value to be used as part of the transformation.
    value: Optional[str] = None
    # An optional secondary value to be used when dealing with between extract operations.
    value2: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExtractTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExtractTransformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExtractTransformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_transformation import CustomClaimTransformation

        from .custom_claim_transformation import CustomClaimTransformation

        fields: dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "value2": lambda n : setattr(self, 'value2', n.get_str_value()),
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
        writer.write_str_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_str_value("value2", self.value2)
    

