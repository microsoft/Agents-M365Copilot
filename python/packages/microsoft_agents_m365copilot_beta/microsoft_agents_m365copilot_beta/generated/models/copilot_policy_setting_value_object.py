from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_policy_setting_agent_sharing_value_object import CopilotPolicySettingAgentSharingValueObject
    from .copilot_policy_setting_agent_user_access_value_object import CopilotPolicySettingAgentUserAccessValueObject
    from .copilot_policy_setting_allowed_agent_types_value_object import CopilotPolicySettingAllowedAgentTypesValueObject
    from .copilot_policy_setting_teams_meeting_value_object import CopilotPolicySettingTeamsMeetingValueObject

@dataclass
class CopilotPolicySettingValueObject(AdditionalDataHolder, Parsable):
    """
    The native JSON value of a Copilot policy setting.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingValueObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingValueObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return CopilotPolicySettingValueObject()
        if mapping_value.casefold() == "#microsoft.graph.copilotPolicySettingAgentSharingValueObject".casefold():
            from .copilot_policy_setting_agent_sharing_value_object import CopilotPolicySettingAgentSharingValueObject

            return CopilotPolicySettingAgentSharingValueObject()
        if mapping_value.casefold() == "#microsoft.graph.copilotPolicySettingAgentUserAccessValueObject".casefold():
            from .copilot_policy_setting_agent_user_access_value_object import CopilotPolicySettingAgentUserAccessValueObject

            return CopilotPolicySettingAgentUserAccessValueObject()
        if mapping_value.casefold() == "#microsoft.graph.copilotPolicySettingAllowedAgentTypesValueObject".casefold():
            from .copilot_policy_setting_allowed_agent_types_value_object import CopilotPolicySettingAllowedAgentTypesValueObject

            return CopilotPolicySettingAllowedAgentTypesValueObject()
        if mapping_value.casefold() == "#microsoft.graph.copilotPolicySettingTeamsMeetingValueObject".casefold():
            from .copilot_policy_setting_teams_meeting_value_object import CopilotPolicySettingTeamsMeetingValueObject

            return CopilotPolicySettingTeamsMeetingValueObject()
        return CopilotPolicySettingValueObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_policy_setting_agent_sharing_value_object import CopilotPolicySettingAgentSharingValueObject
        from .copilot_policy_setting_agent_user_access_value_object import CopilotPolicySettingAgentUserAccessValueObject
        from .copilot_policy_setting_allowed_agent_types_value_object import CopilotPolicySettingAllowedAgentTypesValueObject
        from .copilot_policy_setting_teams_meeting_value_object import CopilotPolicySettingTeamsMeetingValueObject

        from .copilot_policy_setting_agent_sharing_value_object import CopilotPolicySettingAgentSharingValueObject
        from .copilot_policy_setting_agent_user_access_value_object import CopilotPolicySettingAgentUserAccessValueObject
        from .copilot_policy_setting_allowed_agent_types_value_object import CopilotPolicySettingAllowedAgentTypesValueObject
        from .copilot_policy_setting_teams_meeting_value_object import CopilotPolicySettingTeamsMeetingValueObject

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

