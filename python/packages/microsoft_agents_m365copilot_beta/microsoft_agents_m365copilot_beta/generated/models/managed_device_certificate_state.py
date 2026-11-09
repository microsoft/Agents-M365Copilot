from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_issuance_states import CertificateIssuanceStates
    from .certificate_revocation_status import CertificateRevocationStatus
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .device_platform_type import DevicePlatformType
    from .entity import Entity
    from .key_storage_provider_option import KeyStorageProviderOption
    from .key_usages import KeyUsages
    from .subject_alternative_name_type import SubjectAlternativeNameType
    from .subject_name_format import SubjectNameFormat

from .entity import Entity

@dataclass
class ManagedDeviceCertificateState(Entity, Parsable):
    # Extended key usage
    certificate_enhanced_key_usage: Optional[str] = None
    # Error code
    certificate_error_code: Optional[int] = None
    # Certificate expiry date
    certificate_expiration_date_time: Optional[datetime.datetime] = None
    # Issuance date
    certificate_issuance_date_time: Optional[datetime.datetime] = None
    # Certificate Issuance State Options.
    certificate_issuance_state: Optional[CertificateIssuanceStates] = None
    # Issuer
    certificate_issuer: Optional[str] = None
    # Key length
    certificate_key_length: Optional[int] = None
    # Key Storage Provider (KSP) Import Options.
    certificate_key_storage_provider: Optional[KeyStorageProviderOption] = None
    # Key Usage Options.
    certificate_key_usage: Optional[KeyUsages] = None
    # Last certificate issuance state change
    certificate_last_issuance_state_changed_date_time: Optional[datetime.datetime] = None
    # Certificate profile display name
    certificate_profile_display_name: Optional[str] = None
    # Certificate Revocation Status.
    certificate_revoke_status: Optional[CertificateRevocationStatus] = None
    # Serial number
    certificate_serial_number: Optional[str] = None
    # Subject Alternative Name Options.
    certificate_subject_alternative_name_format: Optional[SubjectAlternativeNameType] = None
    # Subject alternative name format string for custom formats
    certificate_subject_alternative_name_format_string: Optional[str] = None
    # Subject Name Format Options.
    certificate_subject_name_format: Optional[SubjectNameFormat] = None
    # Subject name format string for custom subject name formats
    certificate_subject_name_format_string: Optional[str] = None
    # Thumbprint
    certificate_thumbprint: Optional[str] = None
    # Validity period
    certificate_validity_period: Optional[int] = None
    # Certificate Validity Period Options.
    certificate_validity_period_units: Optional[CertificateValidityPeriodScale] = None
    # Device display name
    device_display_name: Optional[str] = None
    # Supported platform types.
    device_platform: Optional[DevicePlatformType] = None
    # Last certificate issuance state change
    last_certificate_state_change_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User display name
    user_display_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceCertificateState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceCertificateState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceCertificateState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_issuance_states import CertificateIssuanceStates
        from .certificate_revocation_status import CertificateRevocationStatus
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_platform_type import DevicePlatformType
        from .entity import Entity
        from .key_storage_provider_option import KeyStorageProviderOption
        from .key_usages import KeyUsages
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat

        from .certificate_issuance_states import CertificateIssuanceStates
        from .certificate_revocation_status import CertificateRevocationStatus
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_platform_type import DevicePlatformType
        from .entity import Entity
        from .key_storage_provider_option import KeyStorageProviderOption
        from .key_usages import KeyUsages
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat

        fields: dict[str, Callable[[Any], None]] = {
            "certificateEnhancedKeyUsage": lambda n : setattr(self, 'certificate_enhanced_key_usage', n.get_str_value()),
            "certificateErrorCode": lambda n : setattr(self, 'certificate_error_code', n.get_int_value()),
            "certificateExpirationDateTime": lambda n : setattr(self, 'certificate_expiration_date_time', n.get_datetime_value()),
            "certificateIssuanceDateTime": lambda n : setattr(self, 'certificate_issuance_date_time', n.get_datetime_value()),
            "certificateIssuanceState": lambda n : setattr(self, 'certificate_issuance_state', n.get_enum_value(CertificateIssuanceStates)),
            "certificateIssuer": lambda n : setattr(self, 'certificate_issuer', n.get_str_value()),
            "certificateKeyLength": lambda n : setattr(self, 'certificate_key_length', n.get_int_value()),
            "certificateKeyStorageProvider": lambda n : setattr(self, 'certificate_key_storage_provider', n.get_enum_value(KeyStorageProviderOption)),
            "certificateKeyUsage": lambda n : setattr(self, 'certificate_key_usage', n.get_collection_of_enum_values(KeyUsages)),
            "certificateLastIssuanceStateChangedDateTime": lambda n : setattr(self, 'certificate_last_issuance_state_changed_date_time', n.get_datetime_value()),
            "certificateProfileDisplayName": lambda n : setattr(self, 'certificate_profile_display_name', n.get_str_value()),
            "certificateRevokeStatus": lambda n : setattr(self, 'certificate_revoke_status', n.get_enum_value(CertificateRevocationStatus)),
            "certificateSerialNumber": lambda n : setattr(self, 'certificate_serial_number', n.get_str_value()),
            "certificateSubjectAlternativeNameFormat": lambda n : setattr(self, 'certificate_subject_alternative_name_format', n.get_collection_of_enum_values(SubjectAlternativeNameType)),
            "certificateSubjectAlternativeNameFormatString": lambda n : setattr(self, 'certificate_subject_alternative_name_format_string', n.get_str_value()),
            "certificateSubjectNameFormat": lambda n : setattr(self, 'certificate_subject_name_format', n.get_enum_value(SubjectNameFormat)),
            "certificateSubjectNameFormatString": lambda n : setattr(self, 'certificate_subject_name_format_string', n.get_str_value()),
            "certificateThumbprint": lambda n : setattr(self, 'certificate_thumbprint', n.get_str_value()),
            "certificateValidityPeriod": lambda n : setattr(self, 'certificate_validity_period', n.get_int_value()),
            "certificateValidityPeriodUnits": lambda n : setattr(self, 'certificate_validity_period_units', n.get_enum_value(CertificateValidityPeriodScale)),
            "deviceDisplayName": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "devicePlatform": lambda n : setattr(self, 'device_platform', n.get_enum_value(DevicePlatformType)),
            "lastCertificateStateChangeDateTime": lambda n : setattr(self, 'last_certificate_state_change_date_time', n.get_datetime_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
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
        writer.write_str_value("certificateEnhancedKeyUsage", self.certificate_enhanced_key_usage)
        writer.write_int_value("certificateErrorCode", self.certificate_error_code)
        writer.write_datetime_value("certificateExpirationDateTime", self.certificate_expiration_date_time)
        writer.write_datetime_value("certificateIssuanceDateTime", self.certificate_issuance_date_time)
        writer.write_enum_value("certificateIssuanceState", self.certificate_issuance_state)
        writer.write_str_value("certificateIssuer", self.certificate_issuer)
        writer.write_int_value("certificateKeyLength", self.certificate_key_length)
        writer.write_enum_value("certificateKeyStorageProvider", self.certificate_key_storage_provider)
        writer.write_enum_value("certificateKeyUsage", self.certificate_key_usage)
        writer.write_datetime_value("certificateLastIssuanceStateChangedDateTime", self.certificate_last_issuance_state_changed_date_time)
        writer.write_str_value("certificateProfileDisplayName", self.certificate_profile_display_name)
        writer.write_enum_value("certificateRevokeStatus", self.certificate_revoke_status)
        writer.write_str_value("certificateSerialNumber", self.certificate_serial_number)
        writer.write_enum_value("certificateSubjectAlternativeNameFormat", self.certificate_subject_alternative_name_format)
        writer.write_str_value("certificateSubjectAlternativeNameFormatString", self.certificate_subject_alternative_name_format_string)
        writer.write_enum_value("certificateSubjectNameFormat", self.certificate_subject_name_format)
        writer.write_str_value("certificateSubjectNameFormatString", self.certificate_subject_name_format_string)
        writer.write_str_value("certificateThumbprint", self.certificate_thumbprint)
        writer.write_int_value("certificateValidityPeriod", self.certificate_validity_period)
        writer.write_enum_value("certificateValidityPeriodUnits", self.certificate_validity_period_units)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_enum_value("devicePlatform", self.device_platform)
        writer.write_datetime_value("lastCertificateStateChangeDateTime", self.last_certificate_state_change_date_time)
        writer.write_str_value("userDisplayName", self.user_display_name)
    

