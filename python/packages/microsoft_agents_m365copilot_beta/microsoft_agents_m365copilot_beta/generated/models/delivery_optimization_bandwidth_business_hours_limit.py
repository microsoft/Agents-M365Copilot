from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeliveryOptimizationBandwidthBusinessHoursLimit(AdditionalDataHolder, Parsable):
    """
    Bandwidth business hours and percentages type
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the beginning of business hours using a 24-hour clock (0-23). Valid values 0 to 23
    bandwidth_begin_business_hours: Optional[int] = None
    # Specifies the end of business hours using a 24-hour clock (0-23). Valid values 0 to 23
    bandwidth_end_business_hours: Optional[int] = None
    # Specifies the percentage of bandwidth to limit during business hours (0-100). Valid values 0 to 100
    bandwidth_percentage_during_business_hours: Optional[int] = None
    # Specifies the percentage of bandwidth to limit outsidse business hours (0-100). Valid values 0 to 100
    bandwidth_percentage_outside_business_hours: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeliveryOptimizationBandwidthBusinessHoursLimit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeliveryOptimizationBandwidthBusinessHoursLimit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeliveryOptimizationBandwidthBusinessHoursLimit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bandwidthBeginBusinessHours": lambda n : setattr(self, 'bandwidth_begin_business_hours', n.get_int_value()),
            "bandwidthEndBusinessHours": lambda n : setattr(self, 'bandwidth_end_business_hours', n.get_int_value()),
            "bandwidthPercentageDuringBusinessHours": lambda n : setattr(self, 'bandwidth_percentage_during_business_hours', n.get_int_value()),
            "bandwidthPercentageOutsideBusinessHours": lambda n : setattr(self, 'bandwidth_percentage_outside_business_hours', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_int_value("bandwidthBeginBusinessHours", self.bandwidth_begin_business_hours)
        writer.write_int_value("bandwidthEndBusinessHours", self.bandwidth_end_business_hours)
        writer.write_int_value("bandwidthPercentageDuringBusinessHours", self.bandwidth_percentage_during_business_hours)
        writer.write_int_value("bandwidthPercentageOutsideBusinessHours", self.bandwidth_percentage_outside_business_hours)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

