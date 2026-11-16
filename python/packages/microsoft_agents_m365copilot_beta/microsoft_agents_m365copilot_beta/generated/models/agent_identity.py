from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .agent_communication_configuration import AgentCommunicationConfiguration
    from .app_role_assignment import AppRoleAssignment
    from .directory_object import DirectoryObject
    from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .service_principal import ServicePrincipal

from .service_principal import ServicePrincipal

@dataclass
class AgentIdentity(ServicePrincipal, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.agentIdentity"
    # The appId of the agent identity blueprint that defines the configuration for this agent identity.
    agent_identity_blueprint_id: Optional[str] = None
    # The effective communication configuration for this agent identity. Represents the agent identity-level override that resolves on top of the configuration inherited from the agent identity blueprint.
    communication_configuration: Optional[AgentCommunicationConfiguration] = None
    # The date and time the agent identity was created. Read-only. Inherited from servicePrincipal.
    created_date_time: Optional[datetime.datetime] = None
    # Application role assignments that this agent identity inherits from its parent Agent Identity Blueprint service principal. Read-only. Nullable.
    inherited_app_role_assignments: Optional[list[AppRoleAssignment]] = None
    # Delegated permission grants that this agent identity inherits from its parent Agent Identity Blueprint service principal. Read-only. Nullable.
    inherited_oauth2_permission_grants: Optional[list[OAuth2PermissionGrant]] = None
    # The lifecyclePolicyComplianceState property
    lifecycle_policy_compliance_state: Optional[LifecyclePolicyComplianceState] = None
    # The lifecyclePolicyComplianceStateLastModifiedDateTime property
    lifecycle_policy_compliance_state_last_modified_date_time: Optional[datetime.datetime] = None
    # The lifecyclePolicyComplianceStateReason property
    lifecycle_policy_compliance_state_reason: Optional[str] = None
    # The lifecyclePolicyNonComplianceDisablementDateTime property
    lifecycle_policy_non_compliance_disablement_date_time: Optional[datetime.datetime] = None
    # The collection of application IDs designated as managers of this agent identity's backing agentIdentityBlueprint. Read-only; the value is server-managed and reflects the managerApplications of the backing agentIdentityBlueprint. To change the managers, an owner or administrator must update the managerApplications property on the backing agentIdentityBlueprint in the tenant where it's registered. For multitenant agent identity blueprints, admins in a tenant where the blueprint is only consumed can't make this change — they must ask an owner or administrator in the blueprint's home tenant. Not nullable. Returned only on $select.
    manager_applications: Optional[list[UUID]] = None
    # The sponsors for this agent identity.
    sponsors: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agent_communication_configuration import AgentCommunicationConfiguration
        from .app_role_assignment import AppRoleAssignment
        from .directory_object import DirectoryObject
        from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .service_principal import ServicePrincipal

        from .agent_communication_configuration import AgentCommunicationConfiguration
        from .app_role_assignment import AppRoleAssignment
        from .directory_object import DirectoryObject
        from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .service_principal import ServicePrincipal

        fields: dict[str, Callable[[Any], None]] = {
            "agentIdentityBlueprintId": lambda n : setattr(self, 'agent_identity_blueprint_id', n.get_str_value()),
            "communicationConfiguration": lambda n : setattr(self, 'communication_configuration', n.get_object_value(AgentCommunicationConfiguration)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "inheritedAppRoleAssignments": lambda n : setattr(self, 'inherited_app_role_assignments', n.get_collection_of_object_values(AppRoleAssignment)),
            "inheritedOauth2PermissionGrants": lambda n : setattr(self, 'inherited_oauth2_permission_grants', n.get_collection_of_object_values(OAuth2PermissionGrant)),
            "lifecyclePolicyComplianceState": lambda n : setattr(self, 'lifecycle_policy_compliance_state', n.get_enum_value(LifecyclePolicyComplianceState)),
            "lifecyclePolicyComplianceStateLastModifiedDateTime": lambda n : setattr(self, 'lifecycle_policy_compliance_state_last_modified_date_time', n.get_datetime_value()),
            "lifecyclePolicyComplianceStateReason": lambda n : setattr(self, 'lifecycle_policy_compliance_state_reason', n.get_str_value()),
            "lifecyclePolicyNonComplianceDisablementDateTime": lambda n : setattr(self, 'lifecycle_policy_non_compliance_disablement_date_time', n.get_datetime_value()),
            "managerApplications": lambda n : setattr(self, 'manager_applications', n.get_collection_of_primitive_values(UUID)),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_str_value("agentIdentityBlueprintId", self.agent_identity_blueprint_id)
        writer.write_object_value("communicationConfiguration", self.communication_configuration)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("inheritedAppRoleAssignments", self.inherited_app_role_assignments)
        writer.write_collection_of_object_values("inheritedOauth2PermissionGrants", self.inherited_oauth2_permission_grants)
        writer.write_enum_value("lifecyclePolicyComplianceState", self.lifecycle_policy_compliance_state)
        writer.write_datetime_value("lifecyclePolicyComplianceStateLastModifiedDateTime", self.lifecycle_policy_compliance_state_last_modified_date_time)
        writer.write_str_value("lifecyclePolicyComplianceStateReason", self.lifecycle_policy_compliance_state_reason)
        writer.write_datetime_value("lifecyclePolicyNonComplianceDisablementDateTime", self.lifecycle_policy_non_compliance_disablement_date_time)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
    

