from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_destination_store import CertificateDestinationStore
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class Windows81TrustedRootCertificate(DeviceConfiguration, Parsable):
    """
    Windows 8.1 Trusted Certificate configuration profile
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows81TrustedRootCertificate"
    # File name to display in UI.
    cert_file_name: Optional[str] = None
    # Possible values for the Certificate Destination Store.
    destination_store: Optional[CertificateDestinationStore] = None
    # Trusted Root Certificate
    trusted_root_certificate: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows81TrustedRootCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows81TrustedRootCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows81TrustedRootCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_destination_store import CertificateDestinationStore
        from .device_configuration import DeviceConfiguration

        from .certificate_destination_store import CertificateDestinationStore
        from .device_configuration import DeviceConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "certFileName": lambda n : setattr(self, 'cert_file_name', n.get_str_value()),
            "destinationStore": lambda n : setattr(self, 'destination_store', n.get_enum_value(CertificateDestinationStore)),
            "trustedRootCertificate": lambda n : setattr(self, 'trusted_root_certificate', n.get_bytes_value()),
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
        writer.write_str_value("certFileName", self.cert_file_name)
        writer.write_enum_value("destinationStore", self.destination_store)
        writer.write_bytes_value("trustedRootCertificate", self.trusted_root_certificate)
    

