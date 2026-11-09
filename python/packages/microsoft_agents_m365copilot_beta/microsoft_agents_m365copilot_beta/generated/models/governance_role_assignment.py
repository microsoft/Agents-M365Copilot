from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_resource import GovernanceResource
    from .governance_role_definition import GovernanceRoleDefinition
    from .governance_subject import GovernanceSubject

from .entity import Entity

@dataclass
class GovernanceRoleAssignment(Entity, Parsable):
    # The state of the assignment. The value can be Eligible for eligible assignment or Active if it's directly assigned Active by administrators, or activated on an eligible assignment by the users.
    assignment_state: Optional[str] = None
    # For a non-permanent role assignment, this is the time when the role assignment is expired. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    end_date_time: Optional[datetime.datetime] = None
    # The external ID the resource that is used to identify the role assignment in the provider.
    external_id: Optional[str] = None
    # Read-only. If this is an active assignment and created due to activation on an eligible assignment, it represents the object of that eligible assignment; Otherwise, the value is null.
    linked_eligible_role_assignment: Optional[GovernanceRoleAssignment] = None
    # If this is an active assignment and created due to activation on an eligible assignment, it represents the ID of that eligible assignment; Otherwise, the value is null.
    linked_eligible_role_assignment_id: Optional[str] = None
    # The type of member. The value can be: Inherited (if the role assignment is inherited from a parent resource scope), Group (if the role assignment isn't inherited, but comes from the membership of a group assignment), or User (if the role assignment isn't inherited or from a group assignment).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. The resource associated with the role assignment.
    resource: Optional[GovernanceResource] = None
    # Required. The ID of the resource that the role assignment is associated with.
    resource_id: Optional[str] = None
    # Read-only. The role definition associated with the role assignment.
    role_definition: Optional[GovernanceRoleDefinition] = None
    # Required. The ID of the role definition that the role assignment is associated with.
    role_definition_id: Optional[str] = None
    # The start time of the role assignment. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # Read-only. The subject associated with the role assignment.
    subject: Optional[GovernanceSubject] = None
    # Required. The ID of the subject that the role assignment is associated with.
    subject_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRoleAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_subject import GovernanceSubject

        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_subject import GovernanceSubject

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "linkedEligibleRoleAssignment": lambda n : setattr(self, 'linked_eligible_role_assignment', n.get_object_value(GovernanceRoleAssignment)),
            "linkedEligibleRoleAssignmentId": lambda n : setattr(self, 'linked_eligible_role_assignment_id', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(GovernanceResource)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(GovernanceRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(GovernanceSubject)),
            "subjectId": lambda n : setattr(self, 'subject_id', n.get_str_value()),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("linkedEligibleRoleAssignment", self.linked_eligible_role_assignment)
        writer.write_str_value("linkedEligibleRoleAssignmentId", self.linked_eligible_role_assignment_id)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_object_value("subject", self.subject)
        writer.write_str_value("subjectId", self.subject_id)
    

