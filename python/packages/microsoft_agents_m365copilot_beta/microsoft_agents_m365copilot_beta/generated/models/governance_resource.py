from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_role_assignment import GovernanceRoleAssignment
    from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
    from .governance_role_definition import GovernanceRoleDefinition
    from .governance_role_setting import GovernanceRoleSetting

from .entity import Entity

@dataclass
class GovernanceResource(Entity, Parsable):
    # The display name of the resource.
    display_name: Optional[str] = None
    # The external id of the resource, representing its original id in the external system. For example, a subscription resource's external id can be '/subscriptions/c14ae696-5e0c-4e5d-88cc-bef6637737ac'.
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. The parent resource. for pimforazurerbac scenario, it can represent the subscription the resource belongs to.
    parent: Optional[GovernanceResource] = None
    # Represents the date time when the resource is registered in PIM.
    registered_date_time: Optional[datetime.datetime] = None
    # The externalId of the resource's root scope that is registered in PIM. The root scope can be the parent, grandparent, or higher ancestor resources.
    registered_root: Optional[str] = None
    # The collection of role assignment requests for the resource.
    role_assignment_requests: Optional[list[GovernanceRoleAssignmentRequest]] = None
    # The collection of role assignments for the resource.
    role_assignments: Optional[list[GovernanceRoleAssignment]] = None
    # The collection of role definitions for the resource.
    role_definitions: Optional[list[GovernanceRoleDefinition]] = None
    # The collection of role settings for the resource.
    role_settings: Optional[list[GovernanceRoleSetting]] = None
    # The status of a given resource. For example, it could represent whether the resource is locked or not (values: Active/Locked). Note: This property may be extended in the future to support more scenarios.
    status: Optional[str] = None
    # Required. Resource type. For example, for Azure resources, the type could be 'Subscription', 'ResourceGroup', 'Microsoft.Sql/server', etc.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting

        from .entity import Entity
        from .governance_role_assignment import GovernanceRoleAssignment
        from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_role_setting import GovernanceRoleSetting

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(GovernanceResource)),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
            "registeredRoot": lambda n : setattr(self, 'registered_root', n.get_str_value()),
            "roleAssignmentRequests": lambda n : setattr(self, 'role_assignment_requests', n.get_collection_of_object_values(GovernanceRoleAssignmentRequest)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(GovernanceRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(GovernanceRoleDefinition)),
            "roleSettings": lambda n : setattr(self, 'role_settings', n.get_collection_of_object_values(GovernanceRoleSetting)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("parent", self.parent)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
        writer.write_str_value("registeredRoot", self.registered_root)
        writer.write_collection_of_object_values("roleAssignmentRequests", self.role_assignment_requests)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleSettings", self.role_settings)
        writer.write_str_value("status", self.status)
        writer.write_str_value("type", self.type)
    

