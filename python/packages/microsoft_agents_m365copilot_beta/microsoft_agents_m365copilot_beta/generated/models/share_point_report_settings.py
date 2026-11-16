from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_usage_report_enablement_status import ApiUsageReportEnablementStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class SharePointReportSettings(Entity, Parsable):
    # The collection of API usage report metrics and the status of their enablement.
    api_usage_report_metrics: Optional[list[ApiUsageReportEnablementStatus]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointReportSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointReportSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointReportSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_usage_report_enablement_status import ApiUsageReportEnablementStatus
        from .entity import Entity

        from .api_usage_report_enablement_status import ApiUsageReportEnablementStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "apiUsageReportMetrics": lambda n : setattr(self, 'api_usage_report_metrics', n.get_collection_of_object_values(ApiUsageReportEnablementStatus)),
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
        writer.write_collection_of_object_values("apiUsageReportMetrics", self.api_usage_report_metrics)
    

