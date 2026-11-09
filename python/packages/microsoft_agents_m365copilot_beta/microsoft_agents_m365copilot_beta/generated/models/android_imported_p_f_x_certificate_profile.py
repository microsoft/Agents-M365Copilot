from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_certificate_profile_base import AndroidCertificateProfileBase
    from .intended_purpose import IntendedPurpose
    from .managed_device_certificate_state import ManagedDeviceCertificateState

from .android_certificate_profile_base import AndroidCertificateProfileBase

@dataclass
class AndroidImportedPFXCertificateProfile(AndroidCertificateProfileBase, Parsable):
    """
    Android PFX Import certificate profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidImportedPFXCertificateProfile"
    # PFX Import Options.
    intended_purpose: Optional[IntendedPurpose] = None
    # Certificate state for devices. This collection can contain a maximum of 2147483647 elements.
    managed_device_certificate_states: Optional[list[ManagedDeviceCertificateState]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidImportedPFXCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidImportedPFXCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidImportedPFXCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        from .android_certificate_profile_base import AndroidCertificateProfileBase
        from .intended_purpose import IntendedPurpose
        from .managed_device_certificate_state import ManagedDeviceCertificateState

        fields: dict[str, Callable[[Any], None]] = {
            "intendedPurpose": lambda n : setattr(self, 'intended_purpose', n.get_enum_value(IntendedPurpose)),
            "managedDeviceCertificateStates": lambda n : setattr(self, 'managed_device_certificate_states', n.get_collection_of_object_values(ManagedDeviceCertificateState)),
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
        writer.write_enum_value("intendedPurpose", self.intended_purpose)
        writer.write_collection_of_object_values("managedDeviceCertificateStates", self.managed_device_certificate_states)
    

