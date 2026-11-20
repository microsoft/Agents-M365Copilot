from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_policy_setting_agent_sharing_limit import CopilotPolicySettingAgentSharingLimit
    from .copilot_policy_setting_user_assignment import CopilotPolicySettingUserAssignment
    from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

@dataclass
class CopilotPolicySettingAgentSharingValueObject(CopilotPolicySettingValueObject, Parsable):
    """
    The value of an agent sharing policy setting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.copilotPolicySettingAgentSharingValueObject"
    # The supported range and default value for an agent sharing limit.
    agent_sharing_limit: Optional[CopilotPolicySettingAgentSharingLimit] = None
    # Indicates whether sharing agents with groups is enabled.
    is_sharing_with_groups_enabled: Optional[bool] = None
    # Indicates whether the per-user agent sharing limit is enabled.
    is_user_sharing_limit_enabled: Optional[bool] = None
    # The users and groups selected by a Copilot policy setting.
    organization_wide_sharing_assignment: Optional[CopilotPolicySettingUserAssignment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingAgentSharingValueObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingAgentSharingValueObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPolicySettingAgentSharingValueObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_policy_setting_agent_sharing_limit import CopilotPolicySettingAgentSharingLimit
        from .copilot_policy_setting_user_assignment import CopilotPolicySettingUserAssignment
        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        from .copilot_policy_setting_agent_sharing_limit import CopilotPolicySettingAgentSharingLimit
        from .copilot_policy_setting_user_assignment import CopilotPolicySettingUserAssignment
        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        fields: dict[str, Callable[[Any], None]] = {
            "agentSharingLimit": lambda n : setattr(self, 'agent_sharing_limit', n.get_object_value(CopilotPolicySettingAgentSharingLimit)),
            "isSharingWithGroupsEnabled": lambda n : setattr(self, 'is_sharing_with_groups_enabled', n.get_bool_value()),
            "isUserSharingLimitEnabled": lambda n : setattr(self, 'is_user_sharing_limit_enabled', n.get_bool_value()),
            "organizationWideSharingAssignment": lambda n : setattr(self, 'organization_wide_sharing_assignment', n.get_object_value(CopilotPolicySettingUserAssignment)),
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
        writer.write_object_value("agentSharingLimit", self.agent_sharing_limit)
        writer.write_bool_value("isSharingWithGroupsEnabled", self.is_sharing_with_groups_enabled)
        writer.write_bool_value("isUserSharingLimitEnabled", self.is_user_sharing_limit_enabled)
        writer.write_object_value("organizationWideSharingAssignment", self.organization_wide_sharing_assignment)
    

