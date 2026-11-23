from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class IdJagEnabledClient(AdditionalDataHolder, Parsable):
    """
    Maps an enabled Entra client application to its identifier at the Resource Authorization Server.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Required and non-null in each enabled-client entry. The appId of the client application in Microsoft Entra.
    client_id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Required and non-null in each enabled-client entry. The client identifier registered for this client at the Resource Authorization Server.
    resource_authorization_server_client_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdJagEnabledClient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdJagEnabledClient
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdJagEnabledClient()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_uuid_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceAuthorizationServerClientId": lambda n : setattr(self, 'resource_authorization_server_client_id', n.get_str_value()),
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
        writer.write_uuid_value("clientId", self.client_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceAuthorizationServerClientId", self.resource_authorization_server_client_id)
        writer.write_additional_data_value(self.additional_data)
    

