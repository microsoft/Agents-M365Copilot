from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_status import CertificateStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class SymantecCodeSigningCertificate(Entity, Parsable):
    # The Windows Symantec Code-Signing Certificate in the raw data format.
    content: Optional[bytes] = None
    # The Cert Expiration Date.
    expiration_date_time: Optional[datetime.datetime] = None
    # The Issuer value for the cert.
    issuer: Optional[str] = None
    # The Issuer Name for the cert.
    issuer_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Password required for .pfx file.
    password: Optional[str] = None
    # The status property
    status: Optional[CertificateStatus] = None
    # The Subject value for the cert.
    subject: Optional[str] = None
    # The Subject Name for the cert.
    subject_name: Optional[str] = None
    # The Type of the CodeSigning Cert as Symantec Cert.
    upload_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SymantecCodeSigningCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SymantecCodeSigningCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SymantecCodeSigningCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_status import CertificateStatus
        from .entity import Entity

        from .certificate_status import CertificateStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerName": lambda n : setattr(self, 'issuer_name', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CertificateStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "subjectName": lambda n : setattr(self, 'subject_name', n.get_str_value()),
            "uploadDateTime": lambda n : setattr(self, 'upload_date_time', n.get_datetime_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerName", self.issuer_name)
        writer.write_str_value("password", self.password)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("subjectName", self.subject_name)
        writer.write_datetime_value("uploadDateTime", self.upload_date_time)
    

