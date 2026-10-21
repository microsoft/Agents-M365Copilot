from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_attribute_base import CustomClaimAttributeBase

from .custom_claim_attribute_base import CustomClaimAttributeBase

@dataclass
class SourcedAttribute(CustomClaimAttributeBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sourcedAttribute"
    # The identifier of the attribute on the specified source.
    id: Optional[str] = None
    # A flag that indicates if the name specified is that of an extension attribute.
    is_extension_attribute: Optional[bool] = None
    # The source where the claim is going to retrieve its value. Valid sources include user, application, resource, audience and company.
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourcedAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourcedAttribute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourcedAttribute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_attribute_base import CustomClaimAttributeBase

        from .custom_claim_attribute_base import CustomClaimAttributeBase

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isExtensionAttribute": lambda n : setattr(self, 'is_extension_attribute', n.get_bool_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isExtensionAttribute", self.is_extension_attribute)
        writer.write_str_value("source", self.source)
    

