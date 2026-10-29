from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_policy_rule import LifecyclePolicyRule

from .lifecycle_policy_rule import LifecyclePolicyRule

@dataclass
class InvitationRedemptionRule(LifecyclePolicyRule, Parsable):
    """
    Requires a pending guest invitation to be redeemed within a threshold period. Guest lifecycle policies only; adding this rule to a non-guest lifecycle policy returns HTTP 400.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.invitationRedemptionRule"
    # The number of days in which the guest user must redeem their invitation.
    invitation_redemption_threshold_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvitationRedemptionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitationRedemptionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvitationRedemptionRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_policy_rule import LifecyclePolicyRule

        from .lifecycle_policy_rule import LifecyclePolicyRule

        fields: dict[str, Callable[[Any], None]] = {
            "invitationRedemptionThresholdInDays": lambda n : setattr(self, 'invitation_redemption_threshold_in_days', n.get_int_value()),
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
        writer.write_int_value("invitationRedemptionThresholdInDays", self.invitation_redemption_threshold_in_days)
    

