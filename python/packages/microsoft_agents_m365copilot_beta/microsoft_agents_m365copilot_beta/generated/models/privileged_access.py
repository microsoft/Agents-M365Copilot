from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_resource import GovernanceResource
    from .governance_role_assignment import GovernanceRoleAssignment
    from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
    from .governance_role_definition import GovernanceRoleDefinition
    from .governance_role_setting import GovernanceRoleSetting

from .entity import Entity

@dataclass
class PrivilegedAccess(Entity, Parsable):
    # The display name of the provider managed by PIM.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of resources for the provider.
    resources: Optional[list[GovernanceResource]] = None
    # A collection of role assignment requests for the provider.
    role_assignment_requests: Optional[list[GovernanceRoleAssignmentRequest]] = None
    # A collection of role assignments for the provider.
    role_assignments: Optional[list[GovernanceRoleAssignment]] = None
    # A collection of role definitions for the provider.
    role_definitions: Optional[list[GovernanceRoleDefinition]] = None
    # A collection of role settings for the provider.
    role_settings: Optional[list[GovernanceRoleSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccess()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting

        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(GovernanceResource)),
            "roleAssignmentRequests": lambda n : setattr(self, 'role_assignment_requests', n.get_collection_of_object_values(GovernanceRoleAssignmentRequest)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(GovernanceRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(GovernanceRoleDefinition)),
            "roleSettings": lambda n : setattr(self, 'role_settings', n.get_collection_of_object_values(GovernanceRoleSetting)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_collection_of_object_values("roleAssignmentRequests", self.role_assignment_requests)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleSettings", self.role_settings)
    

