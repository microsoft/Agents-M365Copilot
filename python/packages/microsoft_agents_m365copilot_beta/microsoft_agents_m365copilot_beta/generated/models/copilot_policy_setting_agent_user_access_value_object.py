from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_policy_setting_assignment_member import CopilotPolicySettingAssignmentMember
    from .copilot_policy_setting_user_assignment_category import CopilotPolicySettingUserAssignmentCategory
    from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

@dataclass
class CopilotPolicySettingAgentUserAccessValueObject(CopilotPolicySettingValueObject, Parsable):
    """
    The value of an agent user access policy setting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.copilotPolicySettingAgentUserAccessValueObject"
    # Users and groups explicitly granted access.
    members: Optional[list[CopilotPolicySettingAssignmentMember]] = None
    # The category that determines which users are assigned by a Copilot policy setting.
    user_assignment_category: Optional[CopilotPolicySettingUserAssignmentCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPolicySettingAgentUserAccessValueObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPolicySettingAgentUserAccessValueObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPolicySettingAgentUserAccessValueObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_policy_setting_assignment_member import CopilotPolicySettingAssignmentMember
        from .copilot_policy_setting_user_assignment_category import CopilotPolicySettingUserAssignmentCategory
        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        from .copilot_policy_setting_assignment_member import CopilotPolicySettingAssignmentMember
        from .copilot_policy_setting_user_assignment_category import CopilotPolicySettingUserAssignmentCategory
        from .copilot_policy_setting_value_object import CopilotPolicySettingValueObject

        fields: dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(CopilotPolicySettingAssignmentMember)),
            "userAssignmentCategory": lambda n : setattr(self, 'user_assignment_category', n.get_enum_value(CopilotPolicySettingUserAssignmentCategory)),
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
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("userAssignmentCategory", self.user_assignment_category)
    

