from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration(AdditionalDataHolder, Parsable):
    """
    Configuration settings for DNS over TLS (DoT) service
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Expected subject name or subject alternative name in the server's TLS certificate
    certificate_subject_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Port for DoT queries (0-65535). Valid values 0 to 65535
    tls_port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsZtdnsSecureDnsServerDnsOverTlsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "certificateSubjectName": lambda n : setattr(self, 'certificate_subject_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tlsPort": lambda n : setattr(self, 'tls_port', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("certificateSubjectName", self.certificate_subject_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("tlsPort", self.tls_port)
        writer.write_additional_data_value(self.additional_data)
    

