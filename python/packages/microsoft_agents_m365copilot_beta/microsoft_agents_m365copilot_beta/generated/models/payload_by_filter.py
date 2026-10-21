from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .associated_assignment_payload_type import AssociatedAssignmentPayloadType
    from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

@dataclass
class PayloadByFilter(AdditionalDataHolder, Parsable):
    """
    This entity represents a single payload with requested assignment filter Id
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents type of the assignment filter.
    assignment_filter_type: Optional[DeviceAndAppManagementAssignmentFilterType] = None
    # The Azure AD security group ID
    group_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy identifier
    payload_id: Optional[str] = None
    # This enum represents associated assignment payload type
    payload_type: Optional[AssociatedAssignmentPayloadType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PayloadByFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PayloadByFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PayloadByFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .associated_assignment_payload_type import AssociatedAssignmentPayloadType
        from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

        from .associated_assignment_payload_type import AssociatedAssignmentPayloadType
        from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentFilterType": lambda n : setattr(self, 'assignment_filter_type', n.get_enum_value(DeviceAndAppManagementAssignmentFilterType)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "payloadType": lambda n : setattr(self, 'payload_type', n.get_enum_value(AssociatedAssignmentPayloadType)),
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
        writer.write_enum_value("assignmentFilterType", self.assignment_filter_type)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("payloadType", self.payload_type)
        writer.write_additional_data_value(self.additional_data)
    

