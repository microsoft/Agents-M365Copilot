from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_site_page import BaseSitePage
    from .sharepoint_ids import SharepointIds

from .base_site_page import BaseSitePage

@dataclass
class NewsLinkPage(BaseSitePage, Parsable):
    # A link to the banner image for the newsLinkPage.
    banner_image_web_url: Optional[str] = None
    # The SharePoint IDs of the referenced news article if it's recognized as a SharePoint resource. Read-only.
    news_sharepoint_ids: Optional[SharepointIds] = None
    # The URL of the news article referenced by the newsLinkPage. It can be an external link.
    news_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NewsLinkPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NewsLinkPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NewsLinkPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_site_page import BaseSitePage
        from .sharepoint_ids import SharepointIds

        from .base_site_page import BaseSitePage
        from .sharepoint_ids import SharepointIds

        fields: dict[str, Callable[[Any], None]] = {
            "bannerImageWebUrl": lambda n : setattr(self, 'banner_image_web_url', n.get_str_value()),
            "newsSharepointIds": lambda n : setattr(self, 'news_sharepoint_ids', n.get_object_value(SharepointIds)),
            "newsWebUrl": lambda n : setattr(self, 'news_web_url', n.get_str_value()),
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
        writer.write_str_value("bannerImageWebUrl", self.banner_image_web_url)
        writer.write_object_value("newsSharepointIds", self.news_sharepoint_ids)
        writer.write_str_value("newsWebUrl", self.news_web_url)
    

