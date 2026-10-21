from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .planner_plan_configuration_bucket_definition import PlannerPlanConfigurationBucketDefinition
    from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization

from .entity import Entity

@dataclass
class PlannerPlanConfiguration(Entity, Parsable):
    # List the buckets that should be created in the plan.
    buckets: Optional[list[PlannerPlanConfigurationBucketDefinition]] = None
    # The identity of the creator of the plan configuration.
    created_by: Optional[IdentitySet] = None
    # The date and time when the plan configuration was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The language code for the default language to be used for the names of the objects created for the plan.
    default_language: Optional[str] = None
    # The identity of the user who last modified the plan configuration.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the plan configuration was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Localized names for the plan configuration.
    localizations: Optional[list[PlannerPlanConfigurationLocalization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerPlanConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlanConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_plan_configuration_bucket_definition import PlannerPlanConfigurationBucketDefinition
        from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization

        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_plan_configuration_bucket_definition import PlannerPlanConfigurationBucketDefinition
        from .planner_plan_configuration_localization import PlannerPlanConfigurationLocalization

        fields: dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerPlanConfigurationBucketDefinition)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultLanguage": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(PlannerPlanConfigurationLocalization)),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("localizations", self.localizations)
    

