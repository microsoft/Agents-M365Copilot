from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

from .device_configuration import DeviceConfiguration

@dataclass
class IosDerivedCredentialAuthenticationConfiguration(DeviceConfiguration, Parsable):
    """
    iOS Derived Credential profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosDerivedCredentialAuthenticationConfiguration"
    # Tenant level settings for the Derived Credentials to be used for authentication.
    derived_credential_settings: Optional[DeviceManagementDerivedCredentialSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosDerivedCredentialAuthenticationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosDerivedCredentialAuthenticationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosDerivedCredentialAuthenticationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

        from .device_configuration import DeviceConfiguration
        from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings

        fields: dict[str, Callable[[Any], None]] = {
            "derivedCredentialSettings": lambda n : setattr(self, 'derived_credential_settings', n.get_object_value(DeviceManagementDerivedCredentialSettings)),
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
        writer.write_object_value("derivedCredentialSettings", self.derived_credential_settings)
    

