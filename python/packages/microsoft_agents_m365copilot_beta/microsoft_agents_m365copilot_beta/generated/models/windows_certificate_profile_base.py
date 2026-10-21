from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .device_configuration import DeviceConfiguration
    from .key_storage_provider_option import KeyStorageProviderOption
    from .subject_alternative_name_type import SubjectAlternativeNameType
    from .subject_name_format import SubjectNameFormat
    from .windows10_certificate_profile_base import Windows10CertificateProfileBase
    from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
    from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
    from .windows81_certificate_profile_base import Windows81CertificateProfileBase
    from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
    from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsCertificateProfileBase(DeviceConfiguration, Parsable):
    """
    Device Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period
    certificate_validity_period_value: Optional[int] = None
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[KeyStorageProviderOption] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[SubjectAlternativeNameType] = None
    # Subject Name Format Options.
    subject_name_format: Optional[SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsCertificateProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CertificateProfileBase".casefold():
            from .windows10_certificate_profile_base import Windows10CertificateProfileBase

            return Windows10CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10ImportedPFXCertificateProfile".casefold():
            from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile

            return Windows10ImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile

            return Windows10PkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CertificateProfileBase".casefold():
            from .windows81_certificate_profile_base import Windows81CertificateProfileBase

            return Windows81CertificateProfileBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81SCEPCertificateProfile".casefold():
            from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile

            return Windows81SCEPCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81ImportedPFXCertificateProfile".casefold():
            from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

            return WindowsPhone81ImportedPFXCertificateProfile()
        return WindowsCertificateProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .key_storage_provider_option import KeyStorageProviderOption
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .key_storage_provider_option import KeyStorageProviderOption
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat
        from .windows10_certificate_profile_base import Windows10CertificateProfileBase
        from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows81_certificate_profile_base import Windows81CertificateProfileBase
        from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
        from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile

        fields: dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(KeyStorageProviderOption)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_collection_of_enum_values(SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(SubjectNameFormat)),
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
        writer.write_enum_value("certificateValidityPeriodScale", self.certificate_validity_period_scale)
        writer.write_int_value("certificateValidityPeriodValue", self.certificate_validity_period_value)
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

