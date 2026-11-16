from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_agent_pool_billing_type import CloudPcAgentPoolBillingType

@dataclass
class CloudPcAgentPoolBillingConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identifier of the billing plan.
    billing_plan_id: Optional[str] = None
    # The billingType property
    billing_type: Optional[CloudPcAgentPoolBillingType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAgentPoolBillingConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAgentPoolBillingConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAgentPoolBillingConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_agent_pool_billing_type import CloudPcAgentPoolBillingType

        from .cloud_pc_agent_pool_billing_type import CloudPcAgentPoolBillingType

        fields: dict[str, Callable[[Any], None]] = {
            "billingPlanId": lambda n : setattr(self, 'billing_plan_id', n.get_str_value()),
            "billingType": lambda n : setattr(self, 'billing_type', n.get_enum_value(CloudPcAgentPoolBillingType)),
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
        writer.write_str_value("billingPlanId", self.billing_plan_id)
        writer.write_enum_value("billingType", self.billing_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

