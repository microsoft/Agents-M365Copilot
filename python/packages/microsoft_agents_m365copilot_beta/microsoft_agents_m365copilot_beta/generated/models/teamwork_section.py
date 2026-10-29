from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .section_display_icon import SectionDisplayIcon
    from .section_sort_type import SectionSortType
    from .section_type import SectionType
    from .teamwork_section_item import TeamworkSectionItem

from .entity import Entity

@dataclass
class TeamworkSection(Entity, Parsable):
    # Date and time when the section was created. Read-only. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The icon displayed for the section.
    display_icon: Optional[SectionDisplayIcon] = None
    # The display name of the section. Required. Maximum length is 50 characters. Display names are case-sensitive and must be unique within a user's sections. The following names are reserved for system-defined sections and can't be used when creating a user-defined section: RecentChats, QuickViews, TeamsAndChannels, MutedChats, MeetingChats, EngageCommunities.
    display_name: Optional[str] = None
    # Indicates whether the section is expanded in the user interface. The default value is true.
    is_expanded: Optional[bool] = None
    # Indicates whether the hierarchical view is enabled for the section. Read-only.
    is_hierarchical_view_enabled: Optional[bool] = None
    # The items (chats, channels, meetings, or communities) organized within the section.
    items: Optional[list[TeamworkSectionItem]] = None
    # Date and time when the section was last modified. Read-only. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the section. The possible values are: userDefined, systemDefined, unknownFutureValue. Read-only.
    section_type: Optional[SectionType] = None
    # The sort order of items in the section. The valid values depend on the sectionType. The possible values are: mostRecent, unreadThenMostRecent, nameAlphabetical, userDefinedCustomOrder, unknownFutureValue.
    sort_type: Optional[SectionSortType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkSection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkSection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .section_display_icon import SectionDisplayIcon
        from .section_sort_type import SectionSortType
        from .section_type import SectionType
        from .teamwork_section_item import TeamworkSectionItem

        from .entity import Entity
        from .section_display_icon import SectionDisplayIcon
        from .section_sort_type import SectionSortType
        from .section_type import SectionType
        from .teamwork_section_item import TeamworkSectionItem

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayIcon": lambda n : setattr(self, 'display_icon', n.get_object_value(SectionDisplayIcon)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isExpanded": lambda n : setattr(self, 'is_expanded', n.get_bool_value()),
            "isHierarchicalViewEnabled": lambda n : setattr(self, 'is_hierarchical_view_enabled', n.get_bool_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(TeamworkSectionItem)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "sectionType": lambda n : setattr(self, 'section_type', n.get_enum_value(SectionType)),
            "sortType": lambda n : setattr(self, 'sort_type', n.get_enum_value(SectionSortType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("displayIcon", self.display_icon)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isExpanded", self.is_expanded)
        writer.write_bool_value("isHierarchicalViewEnabled", self.is_hierarchical_view_enabled)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("sectionType", self.section_type)
        writer.write_enum_value("sortType", self.sort_type)
    

