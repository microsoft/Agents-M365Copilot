from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
    from .managed_device_certificate_state import ManagedDeviceCertificateState

from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase

@dataclass
class AndroidForWorkPkcsCertificateProfile(AndroidForWorkCertificateProfileBase, Parsable):
    """
    Android For Work PKCS certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkPkcsCertificateProfile"
    # PKCS Certificate Template Name
    certificate_template_name: Optional[str] = None
    # PKCS Certification Authority
    certification_authority: Optional[str] = None
    # PKCS Certification Authority Name
    certification_authority_name: Optional[str] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[list[ManagedDeviceCertificateState]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkPkcsCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkPkcsCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkPkcsCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        fields: dict[str, Callable[[Any], None]] = {
            "certificateTemplateName": lambda n : setattr(self, 'certificate_template_name', n.get_str_value()),
            "certificationAuthority": lambda n : setattr(self, 'certification_authority', n.get_str_value()),
            "certificationAuthorityName": lambda n : setattr(self, 'certification_authority_name', n.get_str_value()),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "subjectAlternativeNameFormatString": lambda n : setattr(self, 'subject_alternative_name_format_string', n.get_str_value()),
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
        writer.write_str_value("certificateTemplateName", self.certificate_template_name)
        writer.write_str_value("certificationAuthority", self.certification_authority)
        writer.write_str_value("certificationAuthorityName", self.certification_authority_name)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
    

