from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_state import ActionState
    from .vpp_token_revoke_licenses_action_result import VppTokenRevokeLicensesActionResult

@dataclass
class VppTokenActionResult(AdditionalDataHolder, Parsable):
    """
    The status of the action performed with an Apple Volume Purchase Program token.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Action name
    action_name: Optional[str] = None
    # The actionState property
    action_state: Optional[ActionState] = None
    # Time the action state was last updated
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time the action was initiated
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VppTokenActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VppTokenActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vppTokenRevokeLicensesActionResult".casefold():
            from .vpp_token_revoke_licenses_action_result import VppTokenRevokeLicensesActionResult

            return VppTokenRevokeLicensesActionResult()
        return VppTokenActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_state import ActionState
        from .vpp_token_revoke_licenses_action_result import VppTokenRevokeLicensesActionResult

        from .action_state import ActionState
        from .vpp_token_revoke_licenses_action_result import VppTokenRevokeLicensesActionResult

        fields: dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(ActionState)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

