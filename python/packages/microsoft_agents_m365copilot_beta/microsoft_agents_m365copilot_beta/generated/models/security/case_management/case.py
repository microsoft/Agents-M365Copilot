from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity import Activity
    from .attachment import Attachment
    from .case_management_entity import CaseManagementEntity
    from .case_sla_policy_entry import CaseSlaPolicyEntry
    from .custom_field_values import CustomFieldValues
    from .exposure_case import ExposureCase
    from .generic_case import GenericCase
    from .incident_case import IncidentCase
    from .relation import Relation
    from .task import Task

from .case_management_entity import CaseManagementEntity

@dataclass
class Case(CaseManagementEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.case"
    # The timeline of comments and audit events associated with the case. Supports $expand.
    activities: Optional[list[Activity]] = None
    # Evidence files and metadata associated with the case. Supports $expand.
    attachments: Optional[list[Attachment]] = None
    # Tenant-defined custom field values keyed by the exact displayName of each custom field definition. The property and its dynamic fields don't support $filter.
    custom_fields: Optional[CustomFieldValues] = None
    # The display name of the case. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Links from the case to related security resources. Supports $expand.
    relations: Optional[list[Relation]] = None
    # A denormalized, read-only collection of SLA (service level agreement) policy status entries for the case. Each entry represents one SLA policy applied to the case, including its current status and breach target time. Computed by the service; any value supplied in a create or update request is silently ignored. Supports $filter using the any() lambda operator only, for example, $filter=slaPolicies/any(p: p/status eq 'breached'). The all() lambda operator and other collection functions aren't supported. Doesn't support $orderby.
    sla_policies: Optional[list[CaseSlaPolicyEntry]] = None
    # The tenant-defined lifecycle status of the case. Use a displayName value returned in the status tree by List statuses from /security/caseManagement/caseTypeConfigurations/genericCase/statuses or /security/caseManagement/caseTypeConfigurations/incidentCase/statuses, depending on the case type. Supports $filter (eq).
    status: Optional[str] = None
    # Tasks used to track work required to resolve the case. Supports $expand.
    tasks: Optional[list[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Case:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Case
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.exposureCase".casefold():
            from .exposure_case import ExposureCase

            return ExposureCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.genericCase".casefold():
            from .generic_case import GenericCase

            return GenericCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseManagement.incidentCase".casefold():
            from .incident_case import IncidentCase

            return IncidentCase()
        return Case()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity import Activity
        from .attachment import Attachment
        from .case_management_entity import CaseManagementEntity
        from .case_sla_policy_entry import CaseSlaPolicyEntry
        from .custom_field_values import CustomFieldValues
        from .exposure_case import ExposureCase
        from .generic_case import GenericCase
        from .incident_case import IncidentCase
        from .relation import Relation
        from .task import Task

        from .activity import Activity
        from .attachment import Attachment
        from .case_management_entity import CaseManagementEntity
        from .case_sla_policy_entry import CaseSlaPolicyEntry
        from .custom_field_values import CustomFieldValues
        from .exposure_case import ExposureCase
        from .generic_case import GenericCase
        from .incident_case import IncidentCase
        from .relation import Relation
        from .task import Task

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(Activity)),
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "customFields": lambda n : setattr(self, 'custom_fields', n.get_object_value(CustomFieldValues)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(Relation)),
            "slaPolicies": lambda n : setattr(self, 'sla_policies', n.get_collection_of_object_values(CaseSlaPolicyEntry)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(Task)),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("customFields", self.custom_fields)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_str_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

