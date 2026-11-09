from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_task_creation import PlannerTaskCreation

from .planner_task_creation import PlannerTaskCreation

@dataclass
class PlannerTeamsPublicationInfo(PlannerTaskCreation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.plannerTeamsPublicationInfo"
    # The date and time when this task was last modified by the publication process. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The identifier of the publication. Read-only.
    publication_id: Optional[str] = None
    # The name of the published task list. Read-only.
    publication_name: Optional[str] = None
    # The identifier of the plannerPlan this task was originally placed in. Read-only.
    published_to_plan_id: Optional[str] = None
    # The identifier of the team that initiated the publication process. Read-only.
    publishing_team_id: Optional[str] = None
    # The display name of the team that initiated the publication process. This display name is for reference only, and might not represent the most up-to-date name of the team. Read-only.
    publishing_team_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTeamsPublicationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTeamsPublicationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTeamsPublicationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_task_creation import PlannerTaskCreation

        from .planner_task_creation import PlannerTaskCreation

        fields: dict[str, Callable[[Any], None]] = {
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publicationId": lambda n : setattr(self, 'publication_id', n.get_str_value()),
            "publicationName": lambda n : setattr(self, 'publication_name', n.get_str_value()),
            "publishedToPlanId": lambda n : setattr(self, 'published_to_plan_id', n.get_str_value()),
            "publishingTeamId": lambda n : setattr(self, 'publishing_team_id', n.get_str_value()),
            "publishingTeamName": lambda n : setattr(self, 'publishing_team_name', n.get_str_value()),
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
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("publicationId", self.publication_id)
        writer.write_str_value("publicationName", self.publication_name)
        writer.write_str_value("publishedToPlanId", self.published_to_plan_id)
        writer.write_str_value("publishingTeamId", self.publishing_team_id)
        writer.write_str_value("publishingTeamName", self.publishing_team_name)
    

