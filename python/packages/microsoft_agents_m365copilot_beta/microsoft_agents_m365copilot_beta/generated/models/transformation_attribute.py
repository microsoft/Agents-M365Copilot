from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_attribute_base import CustomClaimAttributeBase

@dataclass
class TransformationAttribute(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The attribute property
    attribute: Optional[CustomClaimAttributeBase] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This flag is only relevant in the case where the attribute is multivalued. By default, transformations are only applied to the first element in a multi-valued claim, however setting this flag to true ensures the transformation is applied to all values, resulting in a multivalued output.
    treat_as_multi_value: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TransformationAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TransformationAttribute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TransformationAttribute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_attribute_base import CustomClaimAttributeBase

        from .custom_claim_attribute_base import CustomClaimAttributeBase

        fields: dict[str, Callable[[Any], None]] = {
            "attribute": lambda n : setattr(self, 'attribute', n.get_object_value(CustomClaimAttributeBase)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "treatAsMultiValue": lambda n : setattr(self, 'treat_as_multi_value', n.get_bool_value()),
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
        writer.write_object_value("attribute", self.attribute)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("treatAsMultiValue", self.treat_as_multi_value)
        writer.write_additional_data_value(self.additional_data)
    

