from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_delta import PlannerDelta
    from .planner_plan_context_type import PlannerPlanContextType

from .planner_delta import PlannerDelta

@dataclass
class PlanContextLink(PlannerDelta, Parsable):
    # Describes how the plan is associated with the surface.
    association_type: Optional[str] = None
    # Date and time the context link was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Custom text used to render the link, if provided.
    custom_link_text: Optional[str] = None
    # How the context link should be displayed. The possible values are: teamsTab, sharePointPage, meetingNotes, other, unknownFutureValue, loopPage, project. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: loopPage , project.
    display_as: Optional[PlannerPlanContextType] = None
    # Display name segments used to render where the plan is surfaced.
    display_name_segments: Optional[list[str]] = None
    # Indicates whether the context link is currently active.
    is_active: Optional[bool] = None
    # Indicates whether this context link represents the original creation surface for the plan.
    is_creation: Optional[bool] = None
    # Identifier for the context the plan is surfaced in.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Application ID of the app that owns the surface the plan is linked from.
    owner_app_id: Optional[str] = None
    # URL of the surface where the plan is displayed.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlanContextLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlanContextLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlanContextLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_delta import PlannerDelta
        from .planner_plan_context_type import PlannerPlanContextType

        from .planner_delta import PlannerDelta
        from .planner_plan_context_type import PlannerPlanContextType

        fields: dict[str, Callable[[Any], None]] = {
            "associationType": lambda n : setattr(self, 'association_type', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customLinkText": lambda n : setattr(self, 'custom_link_text', n.get_str_value()),
            "displayAs": lambda n : setattr(self, 'display_as', n.get_enum_value(PlannerPlanContextType)),
            "displayNameSegments": lambda n : setattr(self, 'display_name_segments', n.get_collection_of_primitive_values(str)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "isCreation": lambda n : setattr(self, 'is_creation', n.get_bool_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "ownerAppId": lambda n : setattr(self, 'owner_app_id', n.get_str_value()),
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
        writer.write_str_value("associationType", self.association_type)
        writer.write_str_value("customLinkText", self.custom_link_text)
        writer.write_enum_value("displayAs", self.display_as)
        writer.write_collection_of_primitive_values("displayNameSegments", self.display_name_segments)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isCreation", self.is_creation)
        writer.write_str_value("key", self.key)
        writer.write_str_value("ownerAppId", self.owner_app_id)
        writer.write_str_value("webUrl", self.web_url)
    

