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
    from .governance_rule_setting import GovernanceRuleSetting

from .entity import Entity

@dataclass
class GovernanceRoleSetting(Entity, Parsable):
    # The rule settings that are evaluated when an administrator tries to add an eligible role assignment.
    admin_eligible_settings: Optional[list[GovernanceRuleSetting]] = None
    # The rule settings that are evaluated when an administrator tries to add a direct member role assignment.
    admin_member_settings: Optional[list[GovernanceRuleSetting]] = None
    # Read-only. Indicate if the roleSetting is a default roleSetting
    is_default: Optional[bool] = None
    # Read-only. The display name of the administrator who last updated the roleSetting.
    last_updated_by: Optional[str] = None
    # Read-only. The time when the role setting was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. The associated resource for this role setting.
    resource: Optional[GovernanceResource] = None
    # Required. The id of the resource that the role setting is associated with.
    resource_id: Optional[str] = None
    # Read-only. The role definition that is enforced with this role setting.
    role_definition: Optional[GovernanceRoleDefinition] = None
    # Required. The id of the role definition that the role setting is associated with.
    role_definition_id: Optional[str] = None
    # The rule settings that are evaluated when a user tries to add an eligible role assignment. The setting is not supported for now.
    user_eligible_settings: Optional[list[GovernanceRuleSetting]] = None
    # The rule settings that are evaluated when a user tries to activate his role assignment.
    user_member_settings: Optional[list[GovernanceRuleSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceRoleSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceRoleSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceRoleSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_rule_setting import GovernanceRuleSetting

        from .entity import Entity
        from .governance_resource import GovernanceResource
        from .governance_role_definition import GovernanceRoleDefinition
        from .governance_rule_setting import GovernanceRuleSetting

        fields: dict[str, Callable[[Any], None]] = {
            "adminEligibleSettings": lambda n : setattr(self, 'admin_eligible_settings', n.get_collection_of_object_values(GovernanceRuleSetting)),
            "adminMemberSettings": lambda n : setattr(self, 'admin_member_settings', n.get_collection_of_object_values(GovernanceRuleSetting)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "lastUpdatedBy": lambda n : setattr(self, 'last_updated_by', n.get_str_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(GovernanceResource)),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(GovernanceRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "userEligibleSettings": lambda n : setattr(self, 'user_eligible_settings', n.get_collection_of_object_values(GovernanceRuleSetting)),
            "userMemberSettings": lambda n : setattr(self, 'user_member_settings', n.get_collection_of_object_values(GovernanceRuleSetting)),
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
        writer.write_collection_of_object_values("adminEligibleSettings", self.admin_eligible_settings)
        writer.write_collection_of_object_values("adminMemberSettings", self.admin_member_settings)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("lastUpdatedBy", self.last_updated_by)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_collection_of_object_values("userEligibleSettings", self.user_eligible_settings)
        writer.write_collection_of_object_values("userMemberSettings", self.user_member_settings)
    

