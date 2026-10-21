from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .open_id_connect_provider import OpenIdConnectProvider

from .entity import Entity

@dataclass
class IdentityProvider(Entity, Parsable):
    # The client ID for the application obtained when registering the application with the identity provider. This is a required field. Required. Not nullable.
    client_id: Optional[str] = None
    # The client secret for the application obtained when registering the application with the identity provider. This is write-only. A read operation returns . This is a required field. Required. Not nullable.
    client_secret: Optional[str] = None
    # The display name of the identity provider. Not nullable.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity provider type is a required field. For B2B scenario: Google, Facebook. For B2C scenario: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo,QQ, WeChat, OpenIDConnect. Not nullable.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openIdConnectProvider".casefold():
            from .open_id_connect_provider import OpenIdConnectProvider

            return OpenIdConnectProvider()
        return IdentityProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .open_id_connect_provider import OpenIdConnectProvider

        from .entity import Entity
        from .open_id_connect_provider import OpenIdConnectProvider

        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("name", self.name)
        writer.write_str_value("type", self.type)
    

