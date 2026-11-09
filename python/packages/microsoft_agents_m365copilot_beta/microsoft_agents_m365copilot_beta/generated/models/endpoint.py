from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class Endpoint(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.endpoint"
    # Describes the capability that is associated with this resource. (for example, Messages, Conversations, etc.) Not nullable. Read-only.
    capability: Optional[str] = None
    # Application id of the publishing underlying service. Not nullable. Read-only.
    provider_id: Optional[str] = None
    # Name of the publishing underlying service. Read-only.
    provider_name: Optional[str] = None
    # For Microsoft 365 groups, this is set to a well-known name for the resource (for example, Yammer.FeedURL etc.). Not nullable. Read-only.
    provider_resource_id: Optional[str] = None
    # URL of the published resource. Not nullable. Read-only.
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Endpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Endpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Endpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "capability": lambda n : setattr(self, 'capability', n.get_str_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_str_value()),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "providerResourceId": lambda n : setattr(self, 'provider_resource_id', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_str_value("capability", self.capability)
        writer.write_str_value("providerId", self.provider_id)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_str_value("providerResourceId", self.provider_resource_id)
        writer.write_str_value("uri", self.uri)
    

