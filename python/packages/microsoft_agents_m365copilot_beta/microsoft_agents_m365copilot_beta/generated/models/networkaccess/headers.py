from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Headers(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the origin or source from which the request is being made.
    origin: Optional[str] = None
    # Represents the referring URL or the URL of the web page that the current request originates from.
    referrer: Optional[str] = None
    # Represents the information about the client original IP address when the request passes through one or more proxy servers or load balancers.
    x_forwarded_for: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Headers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Headers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Headers()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "referrer": lambda n : setattr(self, 'referrer', n.get_str_value()),
            "xForwardedFor": lambda n : setattr(self, 'x_forwarded_for', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("referrer", self.referrer)
        writer.write_str_value("xForwardedFor", self.x_forwarded_for)
        writer.write_additional_data_value(self.additional_data)
    

