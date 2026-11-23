from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .id_jag_client_configuration import IdJagClientConfiguration
    from .id_jag_resource_authorization_server_configuration import IdJagResourceAuthorizationServerConfiguration

@dataclass
class IdJagApplicationConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The client property
    client: Optional[IdJagClientConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceAuthorizationServer property
    resource_authorization_server: Optional[IdJagResourceAuthorizationServerConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdJagApplicationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdJagApplicationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdJagApplicationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .id_jag_client_configuration import IdJagClientConfiguration
        from .id_jag_resource_authorization_server_configuration import IdJagResourceAuthorizationServerConfiguration

        from .id_jag_client_configuration import IdJagClientConfiguration
        from .id_jag_resource_authorization_server_configuration import IdJagResourceAuthorizationServerConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "client": lambda n : setattr(self, 'client', n.get_object_value(IdJagClientConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceAuthorizationServer": lambda n : setattr(self, 'resource_authorization_server', n.get_object_value(IdJagResourceAuthorizationServerConfiguration)),
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
        writer.write_object_value("client", self.client)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("resourceAuthorizationServer", self.resource_authorization_server)
        writer.write_additional_data_value(self.additional_data)
    

