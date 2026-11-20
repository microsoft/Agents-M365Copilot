from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provisioning_status_error_category import ProvisioningStatusErrorCategory
    from .status_base import StatusBase

from .status_base import StatusBase

@dataclass
class StatusDetails(StatusBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.statusDetails"
    # Additional details if there is an error.
    additional_details: Optional[str] = None
    # Categorizes the error code. Possible values are Failure, NonServiceFailure, Success.
    error_category: Optional[ProvisioningStatusErrorCategory] = None
    # Unique error code if any occurred. Learn more
    error_code: Optional[str] = None
    # Summarizes the status and describes why the status happened.
    reason: Optional[str] = None
    # Provides the resolution for the corresponding error.
    recommended_action: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatusDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatusDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provisioning_status_error_category import ProvisioningStatusErrorCategory
        from .status_base import StatusBase

        from .provisioning_status_error_category import ProvisioningStatusErrorCategory
        from .status_base import StatusBase

        fields: dict[str, Callable[[Any], None]] = {
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "errorCategory": lambda n : setattr(self, 'error_category', n.get_enum_value(ProvisioningStatusErrorCategory)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recommendedAction": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
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
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_enum_value("errorCategory", self.error_category)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recommendedAction", self.recommended_action)
    

