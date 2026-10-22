from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_web_content_filter_base import IosWebContentFilterBase

from .ios_web_content_filter_base import IosWebContentFilterBase

@dataclass
class IosWebContentFilterAutoFilter(IosWebContentFilterBase, Parsable):
    """
    Represents an iOS Web Content Filter setting type, which enables iOS automatic filter feature and allows for additional URL access control. When constructed with no property values, the iOS device will enable the automatic filter regardless.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosWebContentFilterAutoFilter"
    # Additional URLs allowed for access
    allowed_urls: Optional[list[str]] = None
    # Additional URLs blocked for access
    blocked_urls: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosWebContentFilterAutoFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosWebContentFilterAutoFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosWebContentFilterAutoFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_web_content_filter_base import IosWebContentFilterBase

        from .ios_web_content_filter_base import IosWebContentFilterBase

        fields: dict[str, Callable[[Any], None]] = {
            "allowedUrls": lambda n : setattr(self, 'allowed_urls', n.get_collection_of_primitive_values(str)),
            "blockedUrls": lambda n : setattr(self, 'blocked_urls', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedUrls", self.allowed_urls)
        writer.write_collection_of_primitive_values("blockedUrls", self.blocked_urls)
    

