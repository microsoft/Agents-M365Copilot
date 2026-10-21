from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .legal_hold_status import LegalHoldStatus
    from .site_source import SiteSource
    from .unified_group_source import UnifiedGroupSource
    from .user_source import UserSource

from ..entity import Entity

@dataclass
class LegalHold(Entity, Parsable):
    # KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
    content_query: Optional[str] = None
    # The user who created the legal hold.
    created_by: Optional[IdentitySet] = None
    # The date and time the legal hold was created.
    created_date_time: Optional[datetime.datetime] = None
    # The legal hold description.
    description: Optional[str] = None
    # The display name of the legal hold.
    display_name: Optional[str] = None
    # Lists any errors that happened while placing the hold.
    errors: Optional[list[str]] = None
    # Indicates whether the hold is enabled and actively holding content.
    is_enabled: Optional[bool] = None
    # the user who last modified the legal hold.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time the legal hold was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Data source entity for SharePoint sites associated with the legal hold.
    site_sources: Optional[list[SiteSource]] = None
    # The status of the legal hold. The possible values are: Pending, Error, Success, UnknownFutureValue.
    status: Optional[LegalHoldStatus] = None
    # The unifiedGroupSources property
    unified_group_sources: Optional[list[UnifiedGroupSource]] = None
    # Data source entity for a the legal hold. This is the container for a mailbox and OneDrive for Business site.
    user_sources: Optional[list[UserSource]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LegalHold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LegalHold
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LegalHold()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .legal_hold_status import LegalHoldStatus
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .legal_hold_status import LegalHoldStatus
        from .site_source import SiteSource
        from .unified_group_source import UnifiedGroupSource
        from .user_source import UserSource

        fields: dict[str, Callable[[Any], None]] = {
            "contentQuery": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "siteSources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(SiteSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LegalHoldStatus)),
            "unifiedGroupSources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(UnifiedGroupSource)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    

