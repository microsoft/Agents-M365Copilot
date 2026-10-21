from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_subject_name_format import AppleSubjectNameFormat
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .device_configuration import DeviceConfiguration
    from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
    from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
    from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
    from .subject_alternative_name_type import SubjectAlternativeNameType

from .device_configuration import DeviceConfiguration

@dataclass
class MacOSCertificateProfileBase(DeviceConfiguration, Parsable):
    """
    Mac OS certificate profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # Certificate renewal threshold percentage.
    renewal_threshold_percentage: Optional[int] = None
    # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[SubjectAlternativeNameType] = None
    # Subject Name Format Options for Apple devices.
    subject_name_format: Optional[AppleSubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCertificateProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSImportedPFXCertificateProfile".casefold():
            from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile

            return MacOSImportedPFXCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSPkcsCertificateProfile".casefold():
            from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile

            return MacOSPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSScepCertificateProfile".casefold():
            from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile

            return MacOSScepCertificateProfile()
        return MacOSCertificateProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_subject_name_format import AppleSubjectNameFormat
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .subject_alternative_name_type import SubjectAlternativeNameType

        from .apple_subject_name_format import AppleSubjectNameFormat
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
        from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
        from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
        from .subject_alternative_name_type import SubjectAlternativeNameType

        fields: dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "subjectAlternativeNameType": lambda n : setattr(self, 'subject_alternative_name_type', n.get_collection_of_enum_values(SubjectAlternativeNameType)),
            "subjectNameFormat": lambda n : setattr(self, 'subject_name_format', n.get_enum_value(AppleSubjectNameFormat)),
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
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

