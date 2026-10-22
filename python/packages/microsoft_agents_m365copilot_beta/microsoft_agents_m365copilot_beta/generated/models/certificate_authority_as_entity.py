from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CertificateAuthorityAsEntity(Entity, Parsable):
    # The trusted certificate.
    certificate: Optional[bytes] = None
    # Indicates if the certificate is a root authority. In a certificateBasedApplicationConfiguration object, at least one object in the trustedCertificateAuthorities collection must be a root authority.
    is_root_authority: Optional[bool] = None
    # The issuer of the trusted certificate.
    issuer: Optional[str] = None
    # The subject key identifier of the trusted certificate.
    issuer_subject_key_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateAuthorityAsEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthorityAsEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateAuthorityAsEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "isRootAuthority": lambda n : setattr(self, 'is_root_authority', n.get_bool_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerSubjectKeyIdentifier": lambda n : setattr(self, 'issuer_subject_key_identifier', n.get_str_value()),
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
        writer.write_bytes_value("certificate", self.certificate)
        writer.write_bool_value("isRootAuthority", self.is_root_authority)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerSubjectKeyIdentifier", self.issuer_subject_key_identifier)
    

