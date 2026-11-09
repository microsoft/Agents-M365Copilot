from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_requirement import SecurityRequirement

from .security_requirement import SecurityRequirement

@dataclass
class CustomersSpendingBudgetSecurityRequirement(SecurityRequirement, Parsable):
    # The number of customers with a spending budget set.
    customers_with_spend_budget_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of customers associated with the partner.
    total_customers_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomersSpendingBudgetSecurityRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomersSpendingBudgetSecurityRequirement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomersSpendingBudgetSecurityRequirement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .security_requirement import SecurityRequirement

        from .security_requirement import SecurityRequirement

        fields: dict[str, Callable[[Any], None]] = {
            "customersWithSpendBudgetCount": lambda n : setattr(self, 'customers_with_spend_budget_count', n.get_int_value()),
            "totalCustomersCount": lambda n : setattr(self, 'total_customers_count', n.get_int_value()),
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
        writer.write_int_value("customersWithSpendBudgetCount", self.customers_with_spend_budget_count)
        writer.write_int_value("totalCustomersCount", self.total_customers_count)
    

