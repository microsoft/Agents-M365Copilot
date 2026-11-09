from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_filter_payload_type import AssignmentFilterPayloadType
    from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

@dataclass
class PayloadCompatibleAssignmentFilter(DeviceAndAppManagementAssignmentFilter, Parsable):
    """
    A class containing the properties used for Payload Compatible Assignment Filter.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.payloadCompatibleAssignmentFilter"
    # Represents the payload type AssignmentFilter is being assigned to.
    payload_type: Optional[AssignmentFilterPayloadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PayloadCompatibleAssignmentFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PayloadCompatibleAssignmentFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PayloadCompatibleAssignmentFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_filter_payload_type import AssignmentFilterPayloadType
        from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

        from .assignment_filter_payload_type import AssignmentFilterPayloadType
        from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

        fields: dict[str, Callable[[Any], None]] = {
            "payloadType": lambda n : setattr(self, 'payload_type', n.get_enum_value(AssignmentFilterPayloadType)),
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
        writer.write_enum_value("payloadType", self.payload_type)
    

