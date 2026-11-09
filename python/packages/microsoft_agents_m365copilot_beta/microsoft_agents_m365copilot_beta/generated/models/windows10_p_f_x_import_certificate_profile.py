from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .key_storage_provider_option import KeyStorageProviderOption

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10PFXImportCertificateProfile(DeviceConfiguration, Parsable):
    """
    Deprecated
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10PFXImportCertificateProfile"
    # Key Storage Provider (KSP) Import Options.
    key_storage_provider: Optional[KeyStorageProviderOption] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10PFXImportCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10PFXImportCertificateProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10PFXImportCertificateProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .key_storage_provider_option import KeyStorageProviderOption

        from .device_configuration import DeviceConfiguration
        from .key_storage_provider_option import KeyStorageProviderOption

        fields: dict[str, Callable[[Any], None]] = {
            "keyStorageProvider": lambda n : setattr(self, 'key_storage_provider', n.get_enum_value(KeyStorageProviderOption)),
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
        writer.write_enum_value("keyStorageProvider", self.key_storage_provider)
    

