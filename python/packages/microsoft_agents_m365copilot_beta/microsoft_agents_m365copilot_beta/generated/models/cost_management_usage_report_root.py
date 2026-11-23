from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_funding_usage_record import CostManagementFundingUsageRecord
    from .cost_management_group_usage_record import CostManagementGroupUsageRecord
    from .cost_management_service_usage_record import CostManagementServiceUsageRecord
    from .cost_management_user_usage_detail import CostManagementUserUsageDetail
    from .cost_management_user_usage_record import CostManagementUserUsageRecord
    from .entity import Entity

from .entity import Entity

@dataclass
class CostManagementUsageReportRoot(Entity, Parsable):
    """
    The Copilot Cost Management usage reporting root.
    """
    # Reported consumption per funding class for a calendar month.
    funding_usage_records: Optional[list[CostManagementFundingUsageRecord]] = None
    # Reported consumption per security group for one completed UTC day.
    group_usage_records: Optional[list[CostManagementGroupUsageRecord]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Reported consumption per governed service for one completed UTC day.
    service_usage_records: Optional[list[CostManagementServiceUsageRecord]] = None
    # Raw per-user usage detail, read one user at a time.
    user_usage_details: Optional[list[CostManagementUserUsageDetail]] = None
    # Reported consumption per user for one completed UTC day, ranked by consumption.
    user_usage_records: Optional[list[CostManagementUserUsageRecord]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUsageReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUsageReportRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUsageReportRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_funding_usage_record import CostManagementFundingUsageRecord
        from .cost_management_group_usage_record import CostManagementGroupUsageRecord
        from .cost_management_service_usage_record import CostManagementServiceUsageRecord
        from .cost_management_user_usage_detail import CostManagementUserUsageDetail
        from .cost_management_user_usage_record import CostManagementUserUsageRecord
        from .entity import Entity

        from .cost_management_funding_usage_record import CostManagementFundingUsageRecord
        from .cost_management_group_usage_record import CostManagementGroupUsageRecord
        from .cost_management_service_usage_record import CostManagementServiceUsageRecord
        from .cost_management_user_usage_detail import CostManagementUserUsageDetail
        from .cost_management_user_usage_record import CostManagementUserUsageRecord
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "fundingUsageRecords": lambda n : setattr(self, 'funding_usage_records', n.get_collection_of_object_values(CostManagementFundingUsageRecord)),
            "groupUsageRecords": lambda n : setattr(self, 'group_usage_records', n.get_collection_of_object_values(CostManagementGroupUsageRecord)),
            "serviceUsageRecords": lambda n : setattr(self, 'service_usage_records', n.get_collection_of_object_values(CostManagementServiceUsageRecord)),
            "userUsageDetails": lambda n : setattr(self, 'user_usage_details', n.get_collection_of_object_values(CostManagementUserUsageDetail)),
            "userUsageRecords": lambda n : setattr(self, 'user_usage_records', n.get_collection_of_object_values(CostManagementUserUsageRecord)),
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
        writer.write_collection_of_object_values("fundingUsageRecords", self.funding_usage_records)
        writer.write_collection_of_object_values("groupUsageRecords", self.group_usage_records)
        writer.write_collection_of_object_values("serviceUsageRecords", self.service_usage_records)
        writer.write_collection_of_object_values("userUsageDetails", self.user_usage_details)
        writer.write_collection_of_object_values("userUsageRecords", self.user_usage_records)
    

