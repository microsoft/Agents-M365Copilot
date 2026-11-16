from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval import Approval
    from .directory_role_management_deleted_item_container import DirectoryRoleManagementDeletedItemContainer
    from .entity import Entity
    from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
    from .unified_role_assignment import UnifiedRoleAssignment
    from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
    from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
    from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

from .entity import Entity

@dataclass
class RbacApplication(Entity, Parsable):
    # Container for soft-deleted directory role management resources.
    deleted_items: Optional[DirectoryRoleManagementDeletedItemContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceNamespaces property
    resource_namespaces: Optional[list[UnifiedRbacResourceNamespace]] = None
    # The roleAssignmentApprovals property
    role_assignment_approvals: Optional[list[Approval]] = None
    # The roleAssignmentScheduleInstances property
    role_assignment_schedule_instances: Optional[list[UnifiedRoleAssignmentScheduleInstance]] = None
    # The roleAssignmentScheduleRequests property
    role_assignment_schedule_requests: Optional[list[UnifiedRoleAssignmentScheduleRequest]] = None
    # The roleAssignmentSchedules property
    role_assignment_schedules: Optional[list[UnifiedRoleAssignmentSchedule]] = None
    # The roleAssignments property
    role_assignments: Optional[list[UnifiedRoleAssignment]] = None
    # The roleDefinitions property
    role_definitions: Optional[list[UnifiedRoleDefinition]] = None
    # The roleEligibilityScheduleInstances property
    role_eligibility_schedule_instances: Optional[list[UnifiedRoleEligibilityScheduleInstance]] = None
    # The roleEligibilityScheduleRequests property
    role_eligibility_schedule_requests: Optional[list[UnifiedRoleEligibilityScheduleRequest]] = None
    # The roleEligibilitySchedules property
    role_eligibility_schedules: Optional[list[UnifiedRoleEligibilitySchedule]] = None
    # The transitiveRoleAssignments property
    transitive_role_assignments: Optional[list[UnifiedRoleAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RbacApplication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval import Approval
        from .directory_role_management_deleted_item_container import DirectoryRoleManagementDeletedItemContainer
        from .entity import Entity
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

        from .approval import Approval
        from .directory_role_management_deleted_item_container import DirectoryRoleManagementDeletedItemContainer
        from .entity import Entity
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

        fields: dict[str, Callable[[Any], None]] = {
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_object_value(DirectoryRoleManagementDeletedItemContainer)),
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(UnifiedRbacResourceNamespace)),
            "roleAssignmentApprovals": lambda n : setattr(self, 'role_assignment_approvals', n.get_collection_of_object_values(Approval)),
            "roleAssignmentScheduleInstances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(UnifiedRoleAssignmentScheduleInstance)),
            "roleAssignmentScheduleRequests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(UnifiedRoleAssignmentScheduleRequest)),
            "roleAssignmentSchedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(UnifiedRoleAssignmentSchedule)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(UnifiedRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(UnifiedRoleDefinition)),
            "roleEligibilityScheduleInstances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(UnifiedRoleEligibilityScheduleInstance)),
            "roleEligibilityScheduleRequests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(UnifiedRoleEligibilityScheduleRequest)),
            "roleEligibilitySchedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(UnifiedRoleEligibilitySchedule)),
            "transitiveRoleAssignments": lambda n : setattr(self, 'transitive_role_assignments', n.get_collection_of_object_values(UnifiedRoleAssignment)),
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
        writer.write_object_value("deletedItems", self.deleted_items)
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignmentApprovals", self.role_assignment_approvals)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
        writer.write_collection_of_object_values("transitiveRoleAssignments", self.transitive_role_assignments)
    

