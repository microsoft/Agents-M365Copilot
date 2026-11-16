from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_facet import ItemFacet
    from .service_information import ServiceInformation

from .item_facet import ItemFacet

@dataclass
class WebAccount(ItemFacet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.webAccount"
    # Contains the description the user has provided for the account on the service being referenced.
    description: Optional[str] = None
    # Contains basic detail about the service that is being associated.
    service: Optional[ServiceInformation] = None
    # Contains a status message from the cloud service if provided or synchronized.
    status_message: Optional[str] = None
    # The thumbnailUrl property
    thumbnail_url: Optional[str] = None
    # The user name  displayed for the webaccount.
    user_id: Optional[str] = None
    # Contains a link to the user's profile on the cloud service if one exists.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebAccount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebAccount
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebAccount()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_facet import ItemFacet
        from .service_information import ServiceInformation

        from .item_facet import ItemFacet
        from .service_information import ServiceInformation

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_object_value(ServiceInformation)),
            "statusMessage": lambda n : setattr(self, 'status_message', n.get_str_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("service", self.service)
        writer.write_str_value("statusMessage", self.status_message)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("webUrl", self.web_url)
    

