from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .payload_request import PayloadRequest
    from .payload_response import PayloadResponse

from .entity import Entity

@dataclass
class Command(Entity, Parsable):
    # The appServiceName property
    app_service_name: Optional[str] = None
    # The error property
    error: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The packageFamilyName property
    package_family_name: Optional[str] = None
    # The payload property
    payload: Optional[PayloadRequest] = None
    # The permissionTicket property
    permission_ticket: Optional[str] = None
    # The postBackUri property
    post_back_uri: Optional[str] = None
    # The responsepayload property
    responsepayload: Optional[PayloadResponse] = None
    # The status property
    status: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Command:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Command
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Command()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .payload_request import PayloadRequest
        from .payload_response import PayloadResponse

        from .entity import Entity
        from .payload_request import PayloadRequest
        from .payload_response import PayloadResponse

        fields: dict[str, Callable[[Any], None]] = {
            "appServiceName": lambda n : setattr(self, 'app_service_name', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "packageFamilyName": lambda n : setattr(self, 'package_family_name', n.get_str_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_object_value(PayloadRequest)),
            "permissionTicket": lambda n : setattr(self, 'permission_ticket', n.get_str_value()),
            "postBackUri": lambda n : setattr(self, 'post_back_uri', n.get_str_value()),
            "responsepayload": lambda n : setattr(self, 'responsepayload', n.get_object_value(PayloadResponse)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("appServiceName", self.app_service_name)
        writer.write_str_value("error", self.error)
        writer.write_str_value("packageFamilyName", self.package_family_name)
        writer.write_object_value("payload", self.payload)
        writer.write_str_value("permissionTicket", self.permission_ticket)
        writer.write_str_value("postBackUri", self.post_back_uri)
        writer.write_object_value("responsepayload", self.responsepayload)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
    

