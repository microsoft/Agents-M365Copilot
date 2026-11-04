from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sla_policy_criteria_block import SlaPolicyCriteriaBlock

@dataclass
class SlaPolicyTimer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The elapsed time in minutes after which the timer is considered breached. Required when supplying a timer.
    breach_threshold_in_minutes: Optional[int] = None
    # The condition that a case must match for this timer to apply. Required when isDefault is false. Omit this property for the default timer.
    filters: Optional[SlaPolicyCriteriaBlock] = None
    # Whether this timer is the fallback when no other timer's filters match. Required when supplying a timer. Exactly one timer per policy must have a value of true.
    is_default: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The evaluation order among the policy's timers, lowest first. Required when supplying a timer.
    order: Optional[int] = None
    # The server-generated identifier for the timer. Computed on creation and immutable thereafter. Read-only. Omit this property from request bodies.
    policy_timer_id: Optional[str] = None
    # The elapsed time in minutes after which an early warning is raised.
    warning_threshold_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlaPolicyTimer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlaPolicyTimer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlaPolicyTimer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sla_policy_criteria_block import SlaPolicyCriteriaBlock

        from .sla_policy_criteria_block import SlaPolicyCriteriaBlock

        fields: dict[str, Callable[[Any], None]] = {
            "breachThresholdInMinutes": lambda n : setattr(self, 'breach_threshold_in_minutes', n.get_int_value()),
            "filters": lambda n : setattr(self, 'filters', n.get_object_value(SlaPolicyCriteriaBlock)),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "policyTimerId": lambda n : setattr(self, 'policy_timer_id', n.get_str_value()),
            "warningThresholdInMinutes": lambda n : setattr(self, 'warning_threshold_in_minutes', n.get_int_value()),
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
        writer.write_int_value("breachThresholdInMinutes", self.breach_threshold_in_minutes)
        writer.write_object_value("filters", self.filters)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("order", self.order)
        writer.write_int_value("warningThresholdInMinutes", self.warning_threshold_in_minutes)
        writer.write_additional_data_value(self.additional_data)
    

