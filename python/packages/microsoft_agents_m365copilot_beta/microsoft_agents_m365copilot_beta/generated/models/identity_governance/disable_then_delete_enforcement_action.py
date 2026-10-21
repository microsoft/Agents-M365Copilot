from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction

from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction

@dataclass
class DisableThenDeleteEnforcementAction(LifecyclePolicyEnforcementAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.disableThenDeleteEnforcementAction"
    # The number of days to wait after disabling a non-compliant identity before deleting it.
    deletion_grace_period_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DisableThenDeleteEnforcementAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DisableThenDeleteEnforcementAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DisableThenDeleteEnforcementAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction

        from .lifecycle_policy_enforcement_action import LifecyclePolicyEnforcementAction

        fields: dict[str, Callable[[Any], None]] = {
            "deletionGracePeriodInDays": lambda n : setattr(self, 'deletion_grace_period_in_days', n.get_int_value()),
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
        writer.write_int_value("deletionGracePeriodInDays", self.deletion_grace_period_in_days)
    

