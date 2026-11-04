from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_decision_reason import AccessDecisionReason
    from .cost_management_data_status import CostManagementDataStatus
    from .cost_management_quantity import CostManagementQuantity
    from .cost_management_unit import CostManagementUnit

@dataclass
class CostManagementUserServiceBalance(AdditionalDataHolder, Parsable):
    """
    Per-service balance and enforcement-selection diagnosis for a user.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The reason for a user's access decision for a service.
    access_decision_reason: Optional[AccessDecisionReason] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    configured_per_user_limit: Optional[CostManagementQuantity] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    configured_period_limit: Optional[CostManagementQuantity] = None
    # Measured consumption for the selected service context, counted from the start of thecurrent period: month-to-date in UTC.
    consumed_quantity: Optional[float] = None
    # Last modification time for the source data represented by a result.
    data_status: Optional[CostManagementDataStatus] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    effective_capacity_quantity: Optional[CostManagementQuantity] = None
    # Whether the user can currently consume the service. False covers both an entitlement gateand an exhausted limit; accessDecisionReason states which one applies.
    is_consumption_allowed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A unit-bearing quantity that is either limited to a value or unlimited. Every quantity isone of its derived types, identified by @odata.type on create.
    remaining_quantity: Optional[CostManagementQuantity] = None
    # The service identifier. A user holds at most one balance per service. Read-only.
    service_id: Optional[str] = None
    # The identifier of the spending policy selected for this service. Always present: aservice with no selected policy is reported incostManagementUserBalance.unevaluatedServices instead of as a balance row. Read-only.
    spending_policy_id: Optional[str] = None
    # Unit in which consumption quantities are expressed. Values are consumption units, not currency.
    unit: Optional[CostManagementUnit] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUserServiceBalance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUserServiceBalance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUserServiceBalance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_decision_reason import AccessDecisionReason
        from .cost_management_data_status import CostManagementDataStatus
        from .cost_management_quantity import CostManagementQuantity
        from .cost_management_unit import CostManagementUnit

        from .access_decision_reason import AccessDecisionReason
        from .cost_management_data_status import CostManagementDataStatus
        from .cost_management_quantity import CostManagementQuantity
        from .cost_management_unit import CostManagementUnit

        fields: dict[str, Callable[[Any], None]] = {
            "accessDecisionReason": lambda n : setattr(self, 'access_decision_reason', n.get_enum_value(AccessDecisionReason)),
            "configuredPerUserLimit": lambda n : setattr(self, 'configured_per_user_limit', n.get_object_value(CostManagementQuantity)),
            "configuredPeriodLimit": lambda n : setattr(self, 'configured_period_limit', n.get_object_value(CostManagementQuantity)),
            "consumedQuantity": lambda n : setattr(self, 'consumed_quantity', n.get_float_value()),
            "dataStatus": lambda n : setattr(self, 'data_status', n.get_object_value(CostManagementDataStatus)),
            "effectiveCapacityQuantity": lambda n : setattr(self, 'effective_capacity_quantity', n.get_object_value(CostManagementQuantity)),
            "isConsumptionAllowed": lambda n : setattr(self, 'is_consumption_allowed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remainingQuantity": lambda n : setattr(self, 'remaining_quantity', n.get_object_value(CostManagementQuantity)),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "spendingPolicyId": lambda n : setattr(self, 'spending_policy_id', n.get_str_value()),
            "unit": lambda n : setattr(self, 'unit', n.get_enum_value(CostManagementUnit)),
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
        writer.write_enum_value("accessDecisionReason", self.access_decision_reason)
        writer.write_object_value("configuredPerUserLimit", self.configured_per_user_limit)
        writer.write_object_value("configuredPeriodLimit", self.configured_period_limit)
        writer.write_float_value("consumedQuantity", self.consumed_quantity)
        writer.write_object_value("dataStatus", self.data_status)
        writer.write_object_value("effectiveCapacityQuantity", self.effective_capacity_quantity)
        writer.write_bool_value("isConsumptionAllowed", self.is_consumption_allowed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("remainingQuantity", self.remaining_quantity)
        writer.write_enum_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

