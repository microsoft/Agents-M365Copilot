from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_user_balance import CostManagementUserBalance
    from .entity import Entity
    from .spending_policy import SpendingPolicy

from .entity import Entity

@dataclass
class CostManagementRoot(Entity, Parsable):
    """
    The Copilot Cost Management administration root.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The spending policies that govern Copilot Credits consumption.
    spending_policies: Optional[list[SpendingPolicy]] = None
    # Per-user consumption balances, addressed by the user's identifier.
    user_balances: Optional[list[CostManagementUserBalance]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_user_balance import CostManagementUserBalance
        from .entity import Entity
        from .spending_policy import SpendingPolicy

        from .cost_management_user_balance import CostManagementUserBalance
        from .entity import Entity
        from .spending_policy import SpendingPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "spendingPolicies": lambda n : setattr(self, 'spending_policies', n.get_collection_of_object_values(SpendingPolicy)),
            "userBalances": lambda n : setattr(self, 'user_balances', n.get_collection_of_object_values(CostManagementUserBalance)),
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
        writer.write_collection_of_object_values("spendingPolicies", self.spending_policies)
        writer.write_collection_of_object_values("userBalances", self.user_balances)
    

