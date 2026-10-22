from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_action_type import MobileAppActionType
    from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem
    from .run_state import RunState

from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem

@dataclass
class MobileAppTroubleshootingAppStateHistory(MobileAppTroubleshootingHistoryItem, Parsable):
    """
    History Item contained in the Mobile App Troubleshooting Event.
    """
    # Defines the Action Types for an Intune Application.
    action_type: Optional[MobileAppActionType] = None
    # Error code for the failure, empty if no failure.
    error_code: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution status of the device management script.
    run_state: Optional[RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppTroubleshootingAppStateHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingAppStateHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppTroubleshootingAppStateHistory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_action_type import MobileAppActionType
        from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem
        from .run_state import RunState

        from .mobile_app_action_type import MobileAppActionType
        from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem
        from .run_state import RunState

        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(MobileAppActionType)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "runState": lambda n : setattr(self, 'run_state', n.get_enum_value(RunState)),
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
        writer.write_enum_value("actionType", self.action_type)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("runState", self.run_state)
    

