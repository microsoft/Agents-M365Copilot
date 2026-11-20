from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .tls_certificate_status import TlsCertificateStatus
    from .validity_date import ValidityDate

from ..entity import Entity

@dataclass
class ExternalCertificateAuthorityCertificate(Entity, Parsable):
    # The signed X.509 certificate in PEM format.
    certificate: Optional[str] = None
    # The Certificate Signing Request (CSR) generated when creating the CA. This CSR should be signed using the customer's PKI infrastructure. Read-only.
    certificate_signing_request: Optional[str] = None
    # The certificate chain in PEM format, containing all intermediate certificates up to the root CA.
    chain: Optional[str] = None
    # The common name (CN) field of the certificate. Supports $filter (eq, ne, startsWith)
    common_name: Optional[str] = None
    # The display name of the CA. Supports $filter (eq, ne, startsWith)
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organization name (OU) field of the certificate. Supports $filter (eq, ne, startsWith)
    organization_name: Optional[str] = None
    # The status property
    status: Optional[TlsCertificateStatus] = None
    # The validity property
    validity: Optional[ValidityDate] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalCertificateAuthorityCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalCertificateAuthorityCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalCertificateAuthorityCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .tls_certificate_status import TlsCertificateStatus
        from .validity_date import ValidityDate

        from ..entity import Entity
        from .tls_certificate_status import TlsCertificateStatus
        from .validity_date import ValidityDate

        fields: dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "certificateSigningRequest": lambda n : setattr(self, 'certificate_signing_request', n.get_str_value()),
            "chain": lambda n : setattr(self, 'chain', n.get_str_value()),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(TlsCertificateStatus)),
            "validity": lambda n : setattr(self, 'validity', n.get_object_value(ValidityDate)),
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
        writer.write_str_value("certificate", self.certificate)
        writer.write_str_value("certificateSigningRequest", self.certificate_signing_request)
        writer.write_str_value("chain", self.chain)
        writer.write_str_value("commonName", self.common_name)
        writer.write_str_value("name", self.name)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("validity", self.validity)
    

