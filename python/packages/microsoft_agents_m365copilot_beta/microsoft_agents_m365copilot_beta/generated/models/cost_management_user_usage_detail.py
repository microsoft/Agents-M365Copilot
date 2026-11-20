from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unit import CostManagementUnit
    from .cost_management_usage_data_status import CostManagementUsageDataStatus
    from .cost_management_user_usage_service_detail import CostManagementUserUsageServiceDetail
    from .cost_management_user_usage_session_detail import CostManagementUserUsageSessionDetail

@dataclass
class CostManagementUserUsageDetail(AdditionalDataHolder, Parsable):
    """
    One user's raw usage detail, distinct from the processed report at userUsageRecords.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Raw, billable-flagged consumption attributed to this user over the requested window, boundedto the latest processed watermark rather than reprocessed. Read-only.
    consumed_quantity: Optional[float] = None
    # Freshness of the source activity data this detail was computed from, when the native sourcereports an as-of timestamp for the window. Null rather than fabricated when the source hasnone to report. Read-only.
    data_status: Optional[CostManagementUsageDataStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This user's raw consumption, split by governed service. The same native grouped result isalso addressable directly at the services navigation collection.
    services: Optional[list[CostManagementUserUsageServiceDetail]] = None
    # Count of billable-flagged activity sessions, bounded to the latest processed watermark, thatcontributed to consumedQuantity. Excludes non-billable activity; the timestamp window and rawsource distinguish this count from the processed completed-day report. Read-only.
    session_count: Optional[int] = None
    # This user's raw usage grouped by session identifiers represented by the native source.Activity without a session identifier may be omitted even when included in the parent total;child quantities need not sum to the parent's consumedQuantity. Also available as a direct collection.
    sessions: Optional[list[CostManagementUserUsageSessionDetail]] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    # The identifier of the user this detail covers. Read-only.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUserUsageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUserUsageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUserUsageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_unit import CostManagementUnit
        from .cost_management_usage_data_status import CostManagementUsageDataStatus
        from .cost_management_user_usage_service_detail import CostManagementUserUsageServiceDetail
        from .cost_management_user_usage_session_detail import CostManagementUserUsageSessionDetail

        from .cost_management_unit import CostManagementUnit
        from .cost_management_usage_data_status import CostManagementUsageDataStatus
        from .cost_management_user_usage_service_detail import CostManagementUserUsageServiceDetail
        from .cost_management_user_usage_session_detail import CostManagementUserUsageSessionDetail

        fields: dict[str, Callable[[Any], None]] = {
            "consumedQuantity": lambda n : setattr(self, 'consumed_quantity', n.get_float_value()),
            "dataStatus": lambda n : setattr(self, 'data_status', n.get_object_value(CostManagementUsageDataStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(CostManagementUserUsageServiceDetail)),
            "sessionCount": lambda n : setattr(self, 'session_count', n.get_int_value()),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(CostManagementUserUsageSessionDetail)),
            "unit": lambda n : setattr(self, 'unit', n.get_enum_value(CostManagementUnit)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_enum_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

