from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verified_credential_claims import VerifiedCredentialClaims

@dataclass
class VerifiedCredentialData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The authority ID for the issuer.
    authority: Optional[str] = None
    # Key-value pair of claims retrieved from the credential that the user presented, and the service verified.
    claims: Optional[VerifiedCredentialClaims] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of credential types provided by the issuer.
    type: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiedCredentialData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedCredentialData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiedCredentialData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .verified_credential_claims import VerifiedCredentialClaims

        from .verified_credential_claims import VerifiedCredentialClaims

        fields: dict[str, Callable[[Any], None]] = {
            "authority": lambda n : setattr(self, 'authority', n.get_str_value()),
            "claims": lambda n : setattr(self, 'claims', n.get_object_value(VerifiedCredentialClaims)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("authority", self.authority)
        writer.write_object_value("claims", self.claims)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

