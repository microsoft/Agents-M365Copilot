from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcBulkActionSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of Cloud PCs where the action failed.
    failed_count: Optional[int] = None
    # The number of Cloud PCs where the action is in progress.
    in_progress_count: Optional[int] = None
    # The number of Cloud PCs where the action isn't supported.
    not_supported_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of Cloud PCs where the action is pending.
    pending_count: Optional[int] = None
    # The number of Cloud PCs where the action is successful.
    successful_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcBulkActionSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcBulkActionSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcBulkActionSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "inProgressCount": lambda n : setattr(self, 'in_progress_count', n.get_int_value()),
            "notSupportedCount": lambda n : setattr(self, 'not_supported_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingCount": lambda n : setattr(self, 'pending_count', n.get_int_value()),
            "successfulCount": lambda n : setattr(self, 'successful_count', n.get_int_value()),
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
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_int_value("inProgressCount", self.in_progress_count)
        writer.write_int_value("notSupportedCount", self.not_supported_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingCount", self.pending_count)
        writer.write_int_value("successfulCount", self.successful_count)
        writer.write_additional_data_value(self.additional_data)
    

