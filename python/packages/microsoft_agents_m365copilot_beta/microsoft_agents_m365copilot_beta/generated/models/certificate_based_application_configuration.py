from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

@dataclass
class CertificateBasedApplicationConfiguration(TrustedCertificateAuthorityAsEntityBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.certificateBasedApplicationConfiguration"
    # The description of the trusted certificate authorities.
    description: Optional[str] = None
    # The display name of the trusted certificate authorities.
    display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateBasedApplicationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateBasedApplicationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateBasedApplicationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

        from .trusted_certificate_authority_as_entity_base import TrustedCertificateAuthorityAsEntityBase

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

