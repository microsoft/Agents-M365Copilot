from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .token_details import TokenDetails

@dataclass
class LinkableIdentifiers(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents a unique identifier for the device from which a user is interacting with an application.
    device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a unique identifier for an entire session and is generated when a user does interactive authentication. This ID helps link all authentication artifacts issued from a single root authentication.
    session_id: Optional[str] = None
    # Property that represents an access token's unique identifier and the time when the token was issued.
    token_details: Optional[TokenDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LinkableIdentifiers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LinkableIdentifiers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LinkableIdentifiers()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .token_details import TokenDetails

        from .token_details import TokenDetails

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "tokenDetails": lambda n : setattr(self, 'token_details', n.get_object_value(TokenDetails)),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_object_value("tokenDetails", self.token_details)
        writer.write_additional_data_value(self.additional_data)
    

