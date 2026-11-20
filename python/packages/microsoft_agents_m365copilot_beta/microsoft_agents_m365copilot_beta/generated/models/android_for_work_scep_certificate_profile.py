from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
    from .certificate_store import CertificateStore
    from .custom_subject_alternative_name import CustomSubjectAlternativeName
    from .hash_algorithms import HashAlgorithms
    from .key_size import KeySize
    from .key_usages import KeyUsages
    from .managed_device_certificate_state import ManagedDeviceCertificateState

from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase

@dataclass
class AndroidForWorkScepCertificateProfile(AndroidForWorkCertificateProfileBase, Parsable):
    """
    Android For Work SCEP certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidForWorkScepCertificateProfile"
    # Target store certificate. Possible values are: user, machine.
    certificate_store: Optional[CertificateStore] = None
    # Custom Subject Alternative Name Settings. This collection can contain a maximum of 500 elements.
    custom_subject_alternative_names: Optional[list[CustomSubjectAlternativeName]] = None
    # Hash Algorithm Options.
    hash_algorithm: Optional[HashAlgorithms] = None
    # Key Size Options.
    key_size: Optional[KeySize] = None
    # Key Usage Options.
    key_usage: Optional[KeyUsages] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[list[ManagedDeviceCertificateState]] = None
    # SCEP Server Url(s)
    scep_server_urls: Optional[list[str]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidForWorkScepCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkScepCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidForWorkScepCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .certificate_store import CertificateStore
        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        from .android_for_work_certificate_profile_base import AndroidForWorkCertificateProfileBase
        from .certificate_store import CertificateStore
        from .custom_subject_alternative_name import CustomSubjectAlternativeName
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        fields: dict[str, Callable[[Any], None]] = {
            "certificateStore": lambda n : setattr(self, 'certificate_store', n.get_enum_value(CertificateStore)),
            "customSubjectAlternativeNames": lambda n : setattr(self, 'custom_subject_alternative_names', n.get_collection_of_object_values(CustomSubjectAlternativeName)),
            "hashAlgorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(HashAlgorithms)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(KeySize)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_collection_of_enum_values(KeyUsages)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "scepServerUrls": lambda n : setattr(self, 'scep_server_urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("customSubjectAlternativeNames", self.custom_subject_alternative_names)
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

