from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_base import PolicyBase
    from .site_source import SiteSource
    from .user_source import UserSource

from .policy_base import PolicyBase

@dataclass
class EdiscoveryHoldPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ediscoveryHoldPolicy"
    # KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
    content_query: Optional[str] = None
    # Lists any errors that happened while placing the hold.
    errors: Optional[list[str]] = None
    # Indicates whether the hold is enabled and actively holding content.
    is_enabled: Optional[bool] = None
    # Data sources that represent SharePoint sites.
    site_sources: Optional[list[SiteSource]] = None
    # Data sources that represent Exchange mailboxes.
    user_sources: Optional[list[UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryHoldPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryHoldPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryHoldPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_base import PolicyBase
        from .site_source import SiteSource
        from .user_source import UserSource

        from .policy_base import PolicyBase
        from .site_source import SiteSource
        from .user_source import UserSource

        fields: dict[str, Callable[[Any], None]] = {
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "siteSources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(SiteSource)),
            "userSources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(UserSource)),
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
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    

