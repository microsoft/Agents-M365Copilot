from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_policy_enforcement_action_state import LifecyclePolicyEnforcementActionState
    from .lifecycle_policy_enforcement_status import LifecyclePolicyEnforcementStatus
    from .lifecycle_policy_next_enforcement_action import LifecyclePolicyNextEnforcementAction

@dataclass
class LifecyclePolicySubjectEnforcement(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether enforcement is locked.
    is_locked: Optional[bool] = None
    # Indicates whether enforcement reached a terminal state.
    is_terminal: Optional[bool] = None
    # The lastAction property
    last_action: Optional[LifecyclePolicyEnforcementActionState] = None
    # The date and time when the last enforcement action completed.
    last_action_date_time: Optional[datetime.datetime] = None
    # The next enforcement action. The possible values are: nonComplianceNotification, firstNotification, secondNotification, finalNotification, disable, disableNotification, delete, unknownFutureValue.
    next_action: Optional[LifecyclePolicyNextEnforcementAction] = None
    # The date and time when the next enforcement action is scheduled.
    next_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[LifecyclePolicyEnforcementStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicySubjectEnforcement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicySubjectEnforcement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicySubjectEnforcement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_policy_enforcement_action_state import LifecyclePolicyEnforcementActionState
        from .lifecycle_policy_enforcement_status import LifecyclePolicyEnforcementStatus
        from .lifecycle_policy_next_enforcement_action import LifecyclePolicyNextEnforcementAction

        from .lifecycle_policy_enforcement_action_state import LifecyclePolicyEnforcementActionState
        from .lifecycle_policy_enforcement_status import LifecyclePolicyEnforcementStatus
        from .lifecycle_policy_next_enforcement_action import LifecyclePolicyNextEnforcementAction

        fields: dict[str, Callable[[Any], None]] = {
            "isLocked": lambda n : setattr(self, 'is_locked', n.get_bool_value()),
            "isTerminal": lambda n : setattr(self, 'is_terminal', n.get_bool_value()),
            "lastAction": lambda n : setattr(self, 'last_action', n.get_enum_value(LifecyclePolicyEnforcementActionState)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "nextAction": lambda n : setattr(self, 'next_action', n.get_enum_value(LifecyclePolicyNextEnforcementAction)),
            "nextActionDateTime": lambda n : setattr(self, 'next_action_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LifecyclePolicyEnforcementStatus)),
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
        writer.write_bool_value("isLocked", self.is_locked)
        writer.write_bool_value("isTerminal", self.is_terminal)
        writer.write_enum_value("lastAction", self.last_action)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("nextAction", self.next_action)
        writer.write_datetime_value("nextActionDateTime", self.next_action_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

