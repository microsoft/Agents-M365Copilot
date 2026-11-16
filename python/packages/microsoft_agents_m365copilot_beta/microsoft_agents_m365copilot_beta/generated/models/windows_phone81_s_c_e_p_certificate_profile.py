from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hash_algorithms import HashAlgorithms
    from .key_size import KeySize
    from .key_usages import KeyUsages
    from .managed_device_certificate_state import ManagedDeviceCertificateState
    from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
    from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate

from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase

@dataclass
class WindowsPhone81SCEPCertificateProfile(WindowsPhone81CertificateProfileBase, Parsable):
    """
    Windows Phone 8.1+ SCEP certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81SCEPCertificateProfile"
    # Hash Algorithm Options.
    hash_algorithm: Optional[HashAlgorithms] = None
    # Key Size Options.
    key_size: Optional[KeySize] = None
    # Key Usage Options.
    key_usage: Optional[KeyUsages] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[list[ManagedDeviceCertificateState]] = None
    # Trusted Root Certificate.
    root_certificate: Optional[WindowsPhone81TrustedRootCertificate] = None
    # SCEP Server Url(s).
    scep_server_urls: Optional[list[str]] = None
    # Custom String that defines the AAD Attribute.
    subject_alternative_name_format_string: Optional[str] = None
    # Custom format to use with SubjectNameFormat = Custom. Example: CN={{EmailAddress}},E={{EmailAddress}},OU=Enterprise Users,O=Contoso Corporation,L=Redmond,ST=WA,C=US
    subject_name_format_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhone81SCEPCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81SCEPCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81SCEPCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate

        from .hash_algorithms import HashAlgorithms
        from .key_size import KeySize
        from .key_usages import KeyUsages
        from .managed_device_certificate_state import ManagedDeviceCertificateState
        from .windows_phone81_certificate_profile_base import WindowsPhone81CertificateProfileBase
        from .windows_phone81_trusted_root_certificate import WindowsPhone81TrustedRootCertificate

        fields: dict[str, Callable[[Any], None]] = {
            "hashAlgorithm": lambda n : setattr(self, 'hash_algorithm', n.get_collection_of_enum_values(HashAlgorithms)),
            "keySize": lambda n : setattr(self, 'key_size', n.get_enum_value(KeySize)),
            "keyUsage": lambda n : setattr(self, 'key_usage', n.get_collection_of_enum_values(KeyUsages)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
            "rootCertificate": lambda n : setattr(self, 'root_certificate', n.get_object_value(WindowsPhone81TrustedRootCertificate)),
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
        writer.write_enum_value("hashAlgorithm", self.hash_algorithm)
        writer.write_enum_value("keySize", self.key_size)
        writer.write_enum_value("keyUsage", self.key_usage)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
        writer.write_object_value("rootCertificate", self.root_certificate)
        writer.write_collection_of_primitive_values("scepServerUrls", self.scep_server_urls)
        writer.write_str_value("subjectAlternativeNameFormatString", self.subject_alternative_name_format_string)
        writer.write_str_value("subjectNameFormatString", self.subject_name_format_string)
    

