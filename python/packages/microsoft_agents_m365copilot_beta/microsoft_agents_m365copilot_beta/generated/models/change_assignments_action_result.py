from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult
    from .device_assignment_item import DeviceAssignmentItem

from .device_action_result import DeviceActionResult

@dataclass
class ChangeAssignmentsActionResult(DeviceActionResult, Parsable):
    """
    ChangeAssignmentsActionResult represents the result of executing the changeAssignments action on tracking the live reporting data for applications or configuration regarding their removal or restoration process
    """
    # Indicates the list of applications or configuration to report live results during their changeAssignments action execution process. The result for each individual application or configuration can contain whether it's being removed or restored, what's the current status with potential message or error code, and when any changes happen on it. Read-Only. This collection can contain a maximum of 30 elements.
    device_assignment_items: Optional[list[DeviceAssignmentItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeAssignmentsActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeAssignmentsActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeAssignmentsActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult
        from .device_assignment_item import DeviceAssignmentItem

        from .device_action_result import DeviceActionResult
        from .device_assignment_item import DeviceAssignmentItem

        fields: dict[str, Callable[[Any], None]] = {
            "deviceAssignmentItems": lambda n : setattr(self, 'device_assignment_items', n.get_collection_of_object_values(DeviceAssignmentItem)),
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
        writer.write_collection_of_object_values("deviceAssignmentItems", self.device_assignment_items)
    

