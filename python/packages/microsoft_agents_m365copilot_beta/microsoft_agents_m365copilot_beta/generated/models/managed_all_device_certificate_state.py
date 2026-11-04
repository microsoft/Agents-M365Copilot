from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_revocation_status import CertificateRevocationStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class ManagedAllDeviceCertificateState(Entity, Parsable):
    # Certificate expiry date
    certificate_expiration_date_time: Optional[datetime.datetime] = None
    # Enhanced Key Usage
    certificate_extended_key_usages: Optional[str] = None
    # Issuance date
    certificate_issuance_date_time: Optional[datetime.datetime] = None
    # Issuer
    certificate_issuer_name: Optional[str] = None
    # Key Usage
    certificate_key_usages: Optional[int] = None
    # Certificate Revocation Status.
    certificate_revoke_status: Optional[CertificateRevocationStatus] = None
    # The time the revoke status was last changed
    certificate_revoke_status_last_change_date_time: Optional[datetime.datetime] = None
    # Serial number
    certificate_serial_number: Optional[str] = None
    # Certificate subject name
    certificate_subject_name: Optional[str] = None
    # Thumbprint
    certificate_thumbprint: Optional[str] = None
    # Device display name
    managed_device_display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User principal name
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAllDeviceCertificateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAllDeviceCertificateState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAllDeviceCertificateState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_revocation_status import CertificateRevocationStatus
        from .entity import Entity

        from .certificate_revocation_status import CertificateRevocationStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "certificateExpirationDateTime": lambda n : setattr(self, 'certificate_expiration_date_time', n.get_datetime_value()),
            "certificateExtendedKeyUsages": lambda n : setattr(self, 'certificate_extended_key_usages', n.get_str_value()),
            "certificateIssuanceDateTime": lambda n : setattr(self, 'certificate_issuance_date_time', n.get_datetime_value()),
            "certificateIssuerName": lambda n : setattr(self, 'certificate_issuer_name', n.get_str_value()),
            "certificateKeyUsages": lambda n : setattr(self, 'certificate_key_usages', n.get_int_value()),
            "certificateRevokeStatus": lambda n : setattr(self, 'certificate_revoke_status', n.get_enum_value(CertificateRevocationStatus)),
            "certificateRevokeStatusLastChangeDateTime": lambda n : setattr(self, 'certificate_revoke_status_last_change_date_time', n.get_datetime_value()),
            "certificateSerialNumber": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificateSubjectName": lambda n : setattr(self, 'certificate_subject_name', n.get_str_value()),
            "certificateThumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "managedDeviceDisplayName": lambda n : setattr(self, 'managed_device_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_datetime_value("certificateExpirationDateTime", self.certificate_expiration_date_time)
        writer.write_str_value("certificateExtendedKeyUsages", self.certificate_extended_key_usages)
        writer.write_datetime_value("certificateIssuanceDateTime", self.certificate_issuance_date_time)
        writer.write_str_value("certificateIssuerName", self.certificate_issuer_name)
        writer.write_int_value("certificateKeyUsages", self.certificate_key_usages)
        writer.write_enum_value("certificateRevokeStatus", self.certificate_revoke_status)
        writer.write_datetime_value("certificateRevokeStatusLastChangeDateTime", self.certificate_revoke_status_last_change_date_time)
        writer.write_str_value("certificateSerialNumber", self.certificate_serial_number)
        writer.write_str_value("certificateSubjectName", self.certificate_subject_name)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_str_value("managedDeviceDisplayName", self.managed_device_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

