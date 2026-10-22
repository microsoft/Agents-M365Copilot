from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_action_info import DlpActionInfo
    from .notify_user_action import NotifyUserAction

from .dlp_action_info import DlpActionInfo

@dataclass
class PolicyTipAction(DlpActionInfo, Parsable):
    # A URL that points users to additional compliance guidance or remediation details for the policy tip.
    compliance_url: Optional[str] = None
    # A user-friendly summary of the matched DLP conditions that triggered the policy tip.
    matched_conditions_description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The text of the policy tip that explains what triggered the DLP policy. Developers can display this information to users in the app.
    policy_tip: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyTipAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyTipAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notifyUserAction".casefold():
            from .notify_user_action import NotifyUserAction

            return NotifyUserAction()
        return PolicyTipAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_action_info import DlpActionInfo
        from .notify_user_action import NotifyUserAction

        from .dlp_action_info import DlpActionInfo
        from .notify_user_action import NotifyUserAction

        fields: dict[str, Callable[[Any], None]] = {
            "complianceUrl": lambda n : setattr(self, 'compliance_url', n.get_str_value()),
            "matchedConditionsDescription": lambda n : setattr(self, 'matched_conditions_description', n.get_str_value()),
            "policyTip": lambda n : setattr(self, 'policy_tip', n.get_str_value()),
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
        writer.write_str_value("complianceUrl", self.compliance_url)
        writer.write_str_value("matchedConditionsDescription", self.matched_conditions_description)
        writer.write_str_value("policyTip", self.policy_tip)
    

