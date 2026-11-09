from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_transformation import CustomClaimTransformation
    from .sourced_attribute import SourcedAttribute

from .custom_claim_transformation import CustomClaimTransformation

@dataclass
class RegexReplaceTransformation(CustomClaimTransformation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.regexReplaceTransformation"
    # Additional attributes that can be referenced within the replacement string.
    additional_attributes: Optional[list[SourcedAttribute]] = None
    # The regular expression to be applied on the input directory attribute or constant.
    regex: Optional[str] = None
    # The transformation output replacement pattern with regular expression output group and input parameter group reference.
    replacement: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RegexReplaceTransformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegexReplaceTransformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RegexReplaceTransformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_transformation import CustomClaimTransformation
        from .sourced_attribute import SourcedAttribute

        from .custom_claim_transformation import CustomClaimTransformation
        from .sourced_attribute import SourcedAttribute

        fields: dict[str, Callable[[Any], None]] = {
            "additionalAttributes": lambda n : setattr(self, 'additional_attributes', n.get_collection_of_object_values(SourcedAttribute)),
            "regex": lambda n : setattr(self, 'regex', n.get_str_value()),
            "replacement": lambda n : setattr(self, 'replacement', n.get_str_value()),
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
        writer.write_collection_of_object_values("additionalAttributes", self.additional_attributes)
        writer.write_str_value("regex", self.regex)
        writer.write_str_value("replacement", self.replacement)
    

