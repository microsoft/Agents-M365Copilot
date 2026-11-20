from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
    from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
    from .device_configuration import DeviceConfiguration
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration(DeviceConfiguration, Parsable):
    """
    Android COBO Derived Credential profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidDeviceOwnerDerivedCredentialAuthenticationConfiguration"
    # Certificate access type. Possible values are: userApproval, specificApps, unknownFutureValue.
    certificate_access_type: Optional[AndroidDeviceOwnerCertificateAccessType] = None
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    # Certificate access information. This collection can contain a maximum of 50 elements.
    silent_certificate_access_details: Optional[list[AndroidDeviceOwnerSilentCertificateAccess]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerDerivedCredentialAuthenticationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
        from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
        from .device_configuration import DeviceConfiguration
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

        from .android_device_owner_certificate_access_type import AndroidDeviceOwnerCertificateAccessType
        from .android_device_owner_silent_certificate_access import AndroidDeviceOwnerSilentCertificateAccess
        from .device_configuration import DeviceConfiguration
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

        fields: dict[str, Callable[[Any], None]] = {
            "certificateAccessType": lambda n : setattr(self, 'certificate_access_type', n.get_enum_value(AndroidDeviceOwnerCertificateAccessType)),
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
            "silentCertificateAccessDetails": lambda n : setattr(self, 'silent_certificate_access_details', n.get_collection_of_object_values(AndroidDeviceOwnerSilentCertificateAccess)),
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
        writer.write_enum_value("certificateAccessType", self.certificate_access_type)
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
        writer.write_collection_of_object_values("silentCertificateAccessDetails", self.silent_certificate_access_details)
    

