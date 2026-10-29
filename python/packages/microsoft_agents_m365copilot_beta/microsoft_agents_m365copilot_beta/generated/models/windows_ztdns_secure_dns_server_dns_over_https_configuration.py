from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration(AdditionalDataHolder, Parsable):
    """
    Configuration settings for DNS over HTTPS (DoH) service
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Port for DoH queries (0-65535). Valid values 0 to 65535
    https_port: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # URL template for DoH queries
    query_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsZtdnsSecureDnsServerDnsOverHttpsConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "httpsPort": lambda n : setattr(self, 'https_port', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "queryUrl": lambda n : setattr(self, 'query_url', n.get_str_value()),
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
        writer.write_int_value("httpsPort", self.https_port)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("queryUrl", self.query_url)
        writer.write_additional_data_value(self.additional_data)
    

