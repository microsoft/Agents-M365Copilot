from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_transformation import CustomClaimTransformation
    from .transformation_attribute import TransformationAttribute

from .custom_claim_transformation import CustomClaimTransformation

@dataclass
class JoinTransformation(CustomClaimTransformation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.joinTransformation"
    # The input2 property
    input2: Optional[TransformationAttribute] = None
    # The separator value to be used.
    separator: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JoinTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JoinTransformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JoinTransformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_attribute import TransformationAttribute

        from .custom_claim_transformation import CustomClaimTransformation
        from .transformation_attribute import TransformationAttribute

        fields: dict[str, Callable[[Any], None]] = {
            "input2": lambda n : setattr(self, 'input2', n.get_object_value(TransformationAttribute)),
            "separator": lambda n : setattr(self, 'separator', n.get_str_value()),
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
        writer.write_object_value("input2", self.input2)
        writer.write_str_value("separator", self.separator)
    

