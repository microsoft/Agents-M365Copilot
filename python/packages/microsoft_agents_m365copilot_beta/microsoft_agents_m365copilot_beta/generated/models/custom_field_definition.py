from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_choice_option import CustomChoiceOption
    from .custom_field_rollup_type import CustomFieldRollupType
    from .custom_field_value_type import CustomFieldValueType
    from .identity_set import IdentitySet
    from .planner_archival_info import PlannerArchivalInfo
    from .planner_delta import PlannerDelta

from .planner_delta import PlannerDelta

@dataclass
class CustomFieldDefinition(PlannerDelta, Parsable):
    # Information about whether the entity is archived, and when it was archived.
    archival_info: Optional[PlannerArchivalInfo] = None
    # The collection of selectable choice options for a single-choice or multiple-choice custom field. Read-only. Nullable.
    choice_options: Optional[list[CustomChoiceOption]] = None
    # Identity of the user (or application) who created the entity. Read-only.
    created_by: Optional[IdentitySet] = None
    # Date and time the entity was created. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Identity of the user who deleted the custom field definition, if it was deleted.
    deleted_by: Optional[IdentitySet] = None
    # Date and time the custom field definition was deleted, if applicable.
    deleted_date_time: Optional[datetime.datetime] = None
    # Name of the custom field.
    display_name: Optional[str] = None
    # Identity of the user (or application) who last modified the entity. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Date and time the entity was last modified. The value is represented in ISO 8601 format and is always in UTC time. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the plan the custom field is defined on. Required, and immutable after creation.
    plan_id: Optional[str] = None
    # How values of this custom field are rolled up across tasks. The possible values are: noRollup, max, min, sum, average, unknownFutureValue.
    rollup_type: Optional[CustomFieldRollupType] = None
    # Data type of the custom field's values.. The possible values are: text, date, utcDateTime, number, decimal, flag, singleChoiceText, multipleChoiceText, unknownFutureValue.
    value_type: Optional[CustomFieldValueType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomFieldDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomFieldDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomFieldDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_choice_option import CustomChoiceOption
        from .custom_field_rollup_type import CustomFieldRollupType
        from .custom_field_value_type import CustomFieldValueType
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta

        from .custom_choice_option import CustomChoiceOption
        from .custom_field_rollup_type import CustomFieldRollupType
        from .custom_field_value_type import CustomFieldValueType
        from .identity_set import IdentitySet
        from .planner_archival_info import PlannerArchivalInfo
        from .planner_delta import PlannerDelta

        fields: dict[str, Callable[[Any], None]] = {
            "archivalInfo": lambda n : setattr(self, 'archival_info', n.get_object_value(PlannerArchivalInfo)),
            "choiceOptions": lambda n : setattr(self, 'choice_options', n.get_collection_of_object_values(CustomChoiceOption)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deletedBy": lambda n : setattr(self, 'deleted_by', n.get_object_value(IdentitySet)),
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "rollupType": lambda n : setattr(self, 'rollup_type', n.get_enum_value(CustomFieldRollupType)),
            "valueType": lambda n : setattr(self, 'value_type', n.get_enum_value(CustomFieldValueType)),
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
        writer.write_object_value("archivalInfo", self.archival_info)
        writer.write_collection_of_object_values("choiceOptions", self.choice_options)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("planId", self.plan_id)
        writer.write_enum_value("rollupType", self.rollup_type)
        writer.write_enum_value("valueType", self.value_type)
    

