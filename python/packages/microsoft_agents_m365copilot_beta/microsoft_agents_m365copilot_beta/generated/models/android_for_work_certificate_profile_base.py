from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
    from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
    from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
    from .certificate_validity_period_scale import CertificateValidityPeriodScale
    from .device_configuration import DeviceConfiguration
    from .extended_key_usage import ExtendedKeyUsage
    from .subject_alternative_name_type import SubjectAlternativeNameType
    from .subject_name_format import SubjectNameFormat

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidForWorkCertificateProfileBase(DeviceConfiguration, Parsable):
    """
    Android For Work certificate profile base.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkCertificateProfileBase"
    # Certificate Validity Period Options.
    certificate_validity_period_scale: Optional[CertificateValidityPeriodScale] = None
    # Value for the Certificate Validity Period.
    certificate_validity_period_value: Optional[int] = None
    # Extended Key Usage (EKU) settings. This collection can contain a maximum of 500 elements.
    extended_key_usages: Optional[list[ExtendedKeyUsage]] = None
    # Certificate renewal threshold percentage. Valid values 1 to 99
    renewal_threshold_percentage: Optional[int] = None
    # Trusted Root Certificate.
    root_certificate: Optional[AndroidForWorkTrustedRootCertificate] = None
    # Certificate Subject Alternative Name Type. Possible values are: none, emailAddress, userPrincipalName, customAzureADAttribute, domainNameService, universalResourceIdentifier.
    subject_alternative_name_type: Optional[SubjectAlternativeNameType] = None
    # Subject Name Format Options.
    subject_name_format: Optional[SubjectNameFormat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkCertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkCertificateProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkPkcsCertificateProfile".casefold():
            from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile

            return AndroidForWorkPkcsCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidForWorkScepCertificateProfile".casefold():
            from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile

            return AndroidForWorkScepCertificateProfile()
        return AndroidForWorkCertificateProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat

        from .android_for_work_pkcs_certificate_profile import AndroidForWorkPkcsCertificateProfile
        from .android_for_work_scep_certificate_profile import AndroidForWorkScepCertificateProfile
        from .android_for_work_trusted_root_certificate import AndroidForWorkTrustedRootCertificate
        from .certificate_validity_period_scale import CertificateValidityPeriodScale
        from .device_configuration import DeviceConfiguration
        from .extended_key_usage import ExtendedKeyUsage
        from .subject_alternative_name_type import SubjectAlternativeNameType
        from .subject_name_format import SubjectNameFormat

        fields: dict[str, Callable[[Any], None]] = {
            "certificateValidityPeriodScale": lambda n : setattr(self, 'certificate_validity_period_scale', n.get_enum_value(CertificateValidityPeriodScale)),
            "certificateValidityPeriodValue": lambda n : setattr(self, 'certificate_validity_period_value', n.get_int_value()),
            "extendedKeyUsages": lambda n : setattr(self, 'extended_key_usages', n.get_collection_of_object_values(ExtendedKeyUsage)),
            "renewalThresholdPercentage": lambda n : setattr(self, 'renewal_threshold_percentage', n.get_int_value()),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(AndroidForWorkTrustedRootCertificate)),
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
        writer.write_collection_of_object_values("extendedKeyUsages", self.extended_key_usages)
        writer.write_int_value("renewalThresholdPercentage", self.renewal_threshold_percentage)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_enum_value("subjectAlternativeNameType", self.subject_alternative_name_type)
        writer.write_enum_value("subjectNameFormat", self.subject_name_format)
    

