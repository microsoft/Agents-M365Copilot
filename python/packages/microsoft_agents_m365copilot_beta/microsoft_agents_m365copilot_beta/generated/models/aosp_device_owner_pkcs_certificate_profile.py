from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
    from .certificate_store import CertificateStore
    from .custom_subject_alternative_name import CustomSubjectAlternativeName
    from .device_management_certification_authority import DeviceManagementCertificationAuthority
    from .managed_device_certificate_state import ManagedDeviceCertificateState

from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase

@dataclass
class AospDeviceOwnerPkcsCertificateProfile(AospDeviceOwnerCertificateProfileBase, Parsable):
    """
    AOSP Device Owner PKCS certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aospDeviceOwnerPkcsCertificateProfile"
    # CertificateStore types
    certificate_store: Optional[CertificateStore] = None
    # PKCS Certificate Template Name
    certificate_template_name: Optional[str] = None
    # PKCS Certification Authority
    certification_authority: Optional[str] = None
    # PKCS Certification Authority Name
    certification_authority_name: Optional[str] = None
    # Device Management Certification Authority Types.
    certification_authority_type: Optional[DeviceManagementCertificationAuthority] = None
    # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
    custom_subject_alternative_names: Optional[list[CustomSubjectAlternativeName]] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[list[ManagedDeviceCertificateState]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AospDeviceOwnerPkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AospDeviceOwnerPkcsCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AospDeviceOwnerPkcsCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .certificate_store import CertificateStore
        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .device_management_certification_authority import DeviceManagementCertificationAuthority
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        from .aosp_device_owner_certificate_profile_base import AospDeviceOwnerCertificateProfileBase
        from .certificate_store import CertificateStore
        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .device_management_certification_authority import DeviceManagementCertificationAuthority
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        fields: dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(CertificateStore)),
            "certificateTemplateName": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificationAuthority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certificationAuthorityName": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "certificationAuthorityType": lambda n : setattr(self, 'certification_authority_type', n.get_enum_value(DeviceManagementCertificationAuthority)),
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(CustomSubjectAlternativeName)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "subjectAlternativeNameFormatString": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
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
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_enum_value("certificationAuthorityType", self.certification_authority_type)
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

