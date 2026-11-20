from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_resource import GovernanceResource
    from .governance_role_assignment_request_status import GovernanceRoleAssignmentRequestStatus
    from .governance_role_definition import GovernanceRoleDefinition
    from .governance_schedule import GovernanceSchedule
    from .governance_subject import GovernanceSubject

from .entity import Entity

@dataclass
class GovernanceRoleAssignmentRequest(Entity, Parsable):
    # Required. The state of the assignment. The possible values are: Eligible (for eligible assignment),  Active (if it is directly assigned), Active (by administrators, or activated on an eligible assignment by the users).
    assignment_state: Optional[str] = None
    # If this is a request for role activation, it represents the id of the eligible assignment being referred; Otherwise, the value is null.
    linked_eligible_role_assignment_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A message provided by users and administrators when create the request about why it is needed.
    reason: Optional[str] = None
    # Read-only. The request create time. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    requested_date_time: Optional[datetime.datetime] = None
    # Read-only. The resource that the request aims to.
    resource: Optional[GovernanceResource] = None
    # Required. The unique identifier of the Azure resource that is associated with the role assignment request. Azure resources can include subscriptions, resource groups, virtual machines, and SQL databases.
    resource_id: Optional[str] = None
    # Read-only. The role definition that the request aims to.
    role_definition: Optional[GovernanceRoleDefinition] = None
    # Required. The identifier of the Azure role definition that the role assignment request is associated with.
    role_definition_id: Optional[str] = None
    # The schedule object of the role assignment request.
    schedule: Optional[GovernanceSchedule] = None
    # The status of the role assignment request.
    status: Optional[GovernanceRoleAssignmentRequestStatus] = None
    # Read-only. The user/group principal.
    subject: Optional[GovernanceSubject] = None
    # Required. The unique identifier of the principal or subject that the role assignment request is associated with. Principals can be users, groups, or service principals.
    subject_id: Optional[str] = None
    # Required. Representing the type of the operation on the role assignment. The possible values are: AdminAdd , UserAdd , AdminUpdate , AdminRemove , UserRemove , UserExtend , AdminExtend , UserRenew , AdminRenew.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceRoleAssignmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleAssignmentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRoleAssignmentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_assignment_request_status import GovernanceRoleAssignmentRequestStatus
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_schedule import GovernanceSchedule
        from .governance_subject import GovernanceSubject

        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_assignment_request_status import GovernanceRoleAssignmentRequestStatus
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_schedule import GovernanceSchedule
        from .governance_subject import GovernanceSubject

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "linkedEligibleRoleAssignmentId": lambda n : setattr(self, 'linked_eligible_role_assignment_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "requestedDateTime": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(GovernanceResource)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(GovernanceRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(GovernanceSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(GovernanceRoleAssignmentRequestStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(GovernanceSubject)),
            "subjectId": lambda n : setattr(self, 'subject_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("linkedEligibleRoleAssignmentId", self.linked_eligible_role_assignment_id)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("requestedDateTime", self.requested_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("status", self.status)
        writer.write_object_value("subject", self.subject)
        writer.write_str_value("subjectId", self.subject_id)
        writer.write_str_value("type", self.type)
    

