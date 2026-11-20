from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .certificate_store import CertificateStore
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .extended_key_usage import ExtendedKeyUsage
    from .hash_algorithms import HashAlgorithms
    from .key_size import KeySize
    from .key_storage_provider_option import KeyStorageProviderOption
    from .key_usages import KeyUsages
    from .windows10_x_certificate_profile import Windows10XCertificateProfile
    from .windows10_x_custom_subject_alternative_name import Windows10XCustomSubjectAlternativeName

from .windows10_x_certificate_profile import Windows10XCertificateProfile

@dataclass
class Windows10XSCEPCertificateProfile(Windows10XCertificateProfile, Parsable):
    """
    Windows X SCEP Certificate configuration profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10XSCEPCertificateProfile"
    # CertificateStore types
    certificate_store: Optional[CertificateStore] = None
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period
    certificate_validity_period_value: Optional[int] = None
    # Extended Key Usage (EKU) settings.
    extended_key_usages: Optional[list[ExtendedKeyUsage]] = None
    # SCEP Hash Algorithm.
    hash_algorithm: Optional[list[HashAlgorithms]] = None
    # Key Size Options.
    key_size: Optional[KeySize] = None
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[KeyStorageProviderOption] = None
    # Key Usage Options.
    key_usage: Optional[KeyUsages] = None
    # Certificate renewal threshold percentage
    renewal_threshold_percentage: Optional[int] = None
    # Trusted Root Certificate ID
    root_certificate_id: Optional[UUID] = None
    # SCEP Server Url(s).
    scep_server_urls: Optional[list[str]] = None
    # Custom AAD Attributes.
    subject_alternative_name_formats: Optional[list[Windows10XCustomSubjectAlternativeName]] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10XSCEPCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XSCEPCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10XSCEPCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_store import CertificateStore
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .extended_key_usage import ExtendedKeyUsage
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_storage_provider_option import KeyStorageProviderOption
        from .key_usages import KeyUsages
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_custom_subject_alternative_name import Windows10XCustomSubjectAlternativeName

        from .certificate_store import CertificateStore
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .extended_key_usage import ExtendedKeyUsage
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_storage_provider_option import KeyStorageProviderOption
        from .key_usages import KeyUsages
        from .windows10_x_certificate_profile import Windows10XCertificateProfile
        from .windows10_x_custom_subject_alternative_name import Windows10XCustomSubjectAlternativeName

        fields: dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(CertificateStore)),
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(ExtendedKeyUsage)),
            "hashAlgorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(HashAlgorithms)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(KeySize)),
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(KeyStorageProviderOption)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_collection_of_enum_values(KeyUsages)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "rootCertificateId": lambda n : setattr(self, 'root_certificate_id', n.get_uuid_value()),
            "scepServerUrls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
            "subjectAlternativeNameFormats": lambda n : setattr(self, 'subject_alternative_name_formats', n.get_collection_of_object_values(Windows10XCustomSubjectAlternativeName)),
            "subjectNameFormatString": lambda n : setattr(self, 'subject_name_format_string', n.get_str_value()),
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
        writer.write_enum_value("certificateStore", self.certificate_store)
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_collection_of_enum_values("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_uuid_value("rootCertificateId", self.root_certificate_id)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_collection_of_object_values("subjectAlternativeNameFormats", self.subject_alternative_name_formats)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

