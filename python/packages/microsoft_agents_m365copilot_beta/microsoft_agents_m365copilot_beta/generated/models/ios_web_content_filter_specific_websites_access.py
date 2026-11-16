from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_bookmark import IosBookmark
    from .ios_web_content_filter_base import IosWebContentFilterBase

from .ios_web_content_filter_base import IosWebContentFilterBase

@dataclass
class IosWebContentFilterSpecificWebsitesAccess(IosWebContentFilterBase, Parsable):
    """
    Represents an iOS Web Content Filter setting type, which installs URL bookmarks into iOS built-in browser. An example scenario is in the classroom where teachers would like the students to navigate websites through browser bookmarks configured on their iOS devices, and no access to other sites.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosWebContentFilterSpecificWebsitesAccess"
    # URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
    specific_websites_only: Optional[list[IosBookmark]] = None
    # URL bookmarks which will be installed into built-in browser and user is only allowed to access websites through bookmarks. This collection can contain a maximum of 500 elements.
    website_list: Optional[list[IosBookmark]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosWebContentFilterSpecificWebsitesAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosWebContentFilterSpecificWebsitesAccess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosWebContentFilterSpecificWebsitesAccess()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_bookmark import IosBookmark
        from .ios_web_content_filter_base import IosWebContentFilterBase

        from .ios_bookmark import IosBookmark
        from .ios_web_content_filter_base import IosWebContentFilterBase

        fields: dict[str, Callable[[Any], None]] = {
            "specificWebsitesOnly": lambda n : setattr(self, 'specific_websites_only', n.get_collection_of_object_values(IosBookmark)),
            "websiteList": lambda n : setattr(self, 'website_list', n.get_collection_of_object_values(IosBookmark)),
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
        writer.write_collection_of_object_values("specificWebsitesOnly", self.specific_websites_only)
        writer.write_collection_of_object_values("websiteList", self.website_list)
    

