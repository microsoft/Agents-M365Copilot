from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .jws_header import JwsHeader

@dataclass
class AgentCardSignature(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The unprotected JWS header values.
    header: Optional[JwsHeader] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The protected JWS header for the signature. This is a Base64url-encoded JSON object, as per RFC 7515.
    protected: Optional[str] = None
    # The computed signature, Base64url-encoded.
    signature: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentCardSignature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentCardSignature
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentCardSignature()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .jws_header import JwsHeader

        from .jws_header import JwsHeader

        fields: dict[str, Callable[[Any], None]] = {
            "header": lambda n : setattr(self, 'header', n.get_object_value(JwsHeader)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protected": lambda n : setattr(self, 'protected', n.get_str_value()),
            "signature": lambda n : setattr(self, 'signature', n.get_str_value()),
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
        writer.write_object_value("header", self.header)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("protected", self.protected)
        writer.write_str_value("signature", self.signature)
        writer.write_additional_data_value(self.additional_data)
    

