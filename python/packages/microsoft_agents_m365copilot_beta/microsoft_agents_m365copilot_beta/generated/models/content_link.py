from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_link_capability import ContentLinkCapability
    from .content_link_type import ContentLinkType
    from .extension_field_collection import ExtensionFieldCollection
    from .identity_set import IdentitySet
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class ContentLink(PlannerDelta, Parsable):
    # Server-computed, read-only capability flags indicating which optional features are enabled for the entity.
    capabilities: Optional[ContentLinkCapability] = None
    # Identity of the user (or application) who created the entity. Read-only.
    created_by: Optional[IdentitySet] = None
    # Display label for the link.
    display_name: Optional[str] = None
    # Custom extension field values set on the entity. Supports $select.
    extensions: Optional[ExtensionFieldCollection] = None
    # Identity of the user (or application) who last modified the entity. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the entity was last modified. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Type of content the link points to. The possible values are: documentReference, webReference, unknownFutureValue.
    link_type: Optional[ContentLinkType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # URL the link points to.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_link_capability import ContentLinkCapability
        from .content_link_type import ContentLinkType
        from .extension_field_collection import ExtensionFieldCollection
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta

        from .content_link_capability import ContentLinkCapability
        from .content_link_type import ContentLinkType
        from .extension_field_collection import ExtensionFieldCollection
        from .identity_set import IdentitySet
        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(ContentLinkCapability)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(ExtensionFieldCollection)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_enum_value(ContentLinkType)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extensions", self.extensions)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("linkType", self.link_type)
        writer.write_str_value("webUrl", self.web_url)
    

