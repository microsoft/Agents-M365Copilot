from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .team import Team
    from .team_template_audience import TeamTemplateAudience

from .entity import Entity

@dataclass
class TeamTemplateDefinition(Entity, Parsable):
    # Describes the audience the team template is available to. The possible values are: organization, user, public, unknownFutureValue.
    audience: Optional[TeamTemplateAudience] = None
    # The assigned categories for the team template.
    categories: Optional[list[str]] = None
    # A brief description of the team template as it will appear to the users in Microsoft Teams.
    description: Optional[str] = None
    # The user defined name of the team template.
    display_name: Optional[str] = None
    # The icon url for the team template.
    icon_url: Optional[str] = None
    # Language the template is available in.
    language_tag: Optional[str] = None
    # The identity of the user who last modified the team template.
    last_modified_by: Optional[IdentitySet] = None
    # The date time of when the team template was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The templateId for the team template
    parent_template_id: Optional[str] = None
    # The organization which published the team template.
    publisher_name: Optional[str] = None
    # A short-description of the team template as it will appear to the users in Microsoft Teams.
    short_description: Optional[str] = None
    # Collection of channel objects. A channel represents a topic, and therefore a logical isolation of discussion, within a team.
    team_definition: Optional[Team] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamTemplateDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamTemplateDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamTemplateDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .team import Team
        from .team_template_audience import TeamTemplateAudience

        from .entity import Entity
        from .identity_set import IdentitySet
        from .team import Team
        from .team_template_audience import TeamTemplateAudience

        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(TeamTemplateAudience)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "parentTemplateId": lambda n : setattr(self, 'parent_template_id', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "shortDescription": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "teamDefinition": lambda n : setattr(self, 'team_definition', n.get_object_value(Team)),
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
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("parentTemplateId", self.parent_template_id)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_object_value("teamDefinition", self.team_definition)
    

