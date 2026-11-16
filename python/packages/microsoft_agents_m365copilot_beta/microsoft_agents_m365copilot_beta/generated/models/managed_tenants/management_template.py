from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..action_url import ActionUrl
    from ..entity import Entity
    from .management_category import ManagementCategory
    from .management_provider import ManagementProvider
    from .management_template_collection import ManagementTemplateCollection
    from .management_template_step import ManagementTemplateStep
    from .template_parameter import TemplateParameter
    from .workload_action import WorkloadAction

from ..entity import Entity

@dataclass
class ManagementTemplate(Entity, Parsable):
    # The management category for the management template. The possible values are: custom, devices, identity, unknownFutureValue. Required. Read-only.
    category: Optional[ManagementCategory] = None
    # The createdByUserId property
    created_by_user_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description for the management template. Optional. Read-only.
    description: Optional[str] = None
    # The display name for the management template. Required. Read-only.
    display_name: Optional[str] = None
    # The informationLinks property
    information_links: Optional[list[ActionUrl]] = None
    # The lastActionByUserId property
    last_action_by_user_id: Optional[str] = None
    # The lastActionDateTime property
    last_action_date_time: Optional[datetime.datetime] = None
    # The managementTemplateCollections property
    management_template_collections: Optional[list[ManagementTemplateCollection]] = None
    # The managementTemplateSteps property
    management_template_steps: Optional[list[ManagementTemplateStep]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of parameters used by the management template. Optional. Read-only.
    parameters: Optional[list[TemplateParameter]] = None
    # The priority property
    priority: Optional[int] = None
    # The provider property
    provider: Optional[ManagementProvider] = None
    # The userImpact property
    user_impact: Optional[str] = None
    # The version property
    version: Optional[int] = None
    # The collection of workload actions associated with the management template. Optional. Read-only.
    workload_actions: Optional[list[WorkloadAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..action_url import ActionUrl
        from ..entity import Entity
        from .management_category import ManagementCategory
        from .management_provider import ManagementProvider
        from .management_template_collection import ManagementTemplateCollection
        from .management_template_step import ManagementTemplateStep
        from .template_parameter import TemplateParameter
        from .workload_action import WorkloadAction

        from ..action_url import ActionUrl
        from ..entity import Entity
        from .management_category import ManagementCategory
        from .management_provider import ManagementProvider
        from .management_template_collection import ManagementTemplateCollection
        from .management_template_step import ManagementTemplateStep
        from .template_parameter import TemplateParameter
        from .workload_action import WorkloadAction

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(ManagementCategory)),
            "createdByUserId": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "informationLinks": lambda n : setattr(self, 'information_links', n.get_collection_of_object_values(ActionUrl)),
            "lastActionByUserId": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "managementTemplateCollections": lambda n : setattr(self, 'management_template_collections', n.get_collection_of_object_values(ManagementTemplateCollection)),
            "managementTemplateSteps": lambda n : setattr(self, 'management_template_steps', n.get_collection_of_object_values(ManagementTemplateStep)),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(TemplateParameter)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_enum_value(ManagementProvider)),
            "userImpact": lambda n : setattr(self, 'user_impact', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "workloadActions": lambda n : setattr(self, 'workload_actions', n.get_collection_of_object_values(WorkloadAction)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("informationLinks", self.information_links)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_collection_of_object_values("managementTemplateCollections", self.management_template_collections)
        writer.write_collection_of_object_values("managementTemplateSteps", self.management_template_steps)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("provider", self.provider)
        writer.write_str_value("userImpact", self.user_impact)
        writer.write_int_value("version", self.version)
        writer.write_collection_of_object_values("workloadActions", self.workload_actions)
    

