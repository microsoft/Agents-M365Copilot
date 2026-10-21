from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_authority_as_entity import CertificateAuthorityAsEntity
    from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class TrustedCertificateAuthorityAsEntityBase(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.trustedCertificateAuthorityAsEntityBase"
    # Collection of trusted certificate authorities.
    trusted_certificate_authorities: Optional[list[CertificateAuthorityAsEntity]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrustedCertificateAuthorityAsEntityBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrustedCertificateAuthorityAsEntityBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedApplicationConfiguration".casefold():
            from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration

            return CertificateBasedApplicationConfiguration()
        return TrustedCertificateAuthorityAsEntityBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_authority_as_entity import CertificateAuthorityAsEntity
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .directory_object import DirectoryObject

        from .certificate_authority_as_entity import CertificateAuthorityAsEntity
        from .certificate_based_application_configuration import CertificateBasedApplicationConfiguration
        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "trustedCertificateAuthorities": lambda n : setattr(self, 'trusted_certificate_authorities', n.get_collection_of_object_values(CertificateAuthorityAsEntity)),
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
        writer.write_collection_of_object_values("trustedCertificateAuthorities", self.trusted_certificate_authorities)
    

