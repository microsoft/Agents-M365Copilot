from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_claim_base import CustomClaimBase
    from .saml_attribute_name_format import SamlAttributeNameFormat
    from .token_format import TokenFormat

from .custom_claim_base import CustomClaimBase

@dataclass
class CustomClaim(CustomClaimBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customClaim"
    # The name of the claim to be emitted.
    name: Optional[str] = None
    # An optional namespace to be included as part of the claim name.
    namespace: Optional[str] = None
    # If specified, it sets the nameFormat attribute associated with the claim in the SAML response. The possible values are: unspecified, uri, basic, unknownFutureValue.
    saml_attribute_name_format: Optional[SamlAttributeNameFormat] = None
    # List of token formats for which this claim should be emitted. The possible values are: saml,jwt, unknownFutureValue
    token_format: Optional[list[TokenFormat]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomClaim:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomClaim
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomClaim()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_claim_base import CustomClaimBase
        from .saml_attribute_name_format import SamlAttributeNameFormat
        from .token_format import TokenFormat

        from .custom_claim_base import CustomClaimBase
        from .saml_attribute_name_format import SamlAttributeNameFormat
        from .token_format import TokenFormat

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "samlAttributeNameFormat": lambda n : setattr(self, 'saml_attribute_name_format', n.get_enum_value(SamlAttributeNameFormat)),
            "tokenFormat": lambda n : setattr(self, 'token_format', n.get_collection_of_enum_values(TokenFormat)),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_enum_value("samlAttributeNameFormat", self.saml_attribute_name_format)
        writer.write_collection_of_enum_values("tokenFormat", self.token_format)
    

