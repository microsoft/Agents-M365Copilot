from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .balance_evaluation_failure_reason import BalanceEvaluationFailureReason

@dataclass
class CostManagementUnevaluatedService(AdditionalDataHolder, Parsable):
    """
    A service whose balance could not be evaluated for the user, reported instead of anunreliable costManagementUserServiceBalance row.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The reason a service's balance could not be evaluated for the user.
    reason: Optional[BalanceEvaluationFailureReason] = None
    # The service identifier whose balance could not be evaluated.
    service_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUnevaluatedService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUnevaluatedService
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUnevaluatedService()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .balance_evaluation_failure_reason import BalanceEvaluationFailureReason

        from .balance_evaluation_failure_reason import BalanceEvaluationFailureReason

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(BalanceEvaluationFailureReason)),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
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
        writer.write_enum_value("reason", self.reason)
        writer.write_str_value("serviceId", self.service_id)
        writer.write_additional_data_value(self.additional_data)
    

