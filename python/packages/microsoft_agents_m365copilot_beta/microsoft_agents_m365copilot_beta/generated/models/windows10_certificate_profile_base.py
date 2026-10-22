from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
    from .windows_certificate_profile_base import WindowsCertificateProfileBase

from .windows_certificate_profile_base import WindowsCertificateProfileBase

@dataclass
class Windows10CertificateProfileBase(WindowsCertificateProfileBase, Parsable):
    """
    Base class for Windows 10 certificate profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10CertificateProfileBase"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10CertificateProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10CertificateProfileBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10PkcsCertificateProfile".casefold():
            from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile

            return Windows10PkcsCertificateProfile()
        return Windows10CertificateProfileBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
        from .windows_certificate_profile_base import WindowsCertificateProfileBase

        fields: dict[str, Callable[[Any], None]] = {
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
    

