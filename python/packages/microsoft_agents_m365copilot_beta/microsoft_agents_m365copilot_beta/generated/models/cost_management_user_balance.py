from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_unevaluated_service import CostManagementUnevaluatedService
    from .cost_management_user_service_balance import CostManagementUserServiceBalance
    from .entity import Entity
    from .selection_data_status import SelectionDataStatus

from .entity import Entity

@dataclass
class CostManagementUserBalance(Entity, Parsable):
    """
    A user's computed per-service consumption balance. Addressed by the user's identifier; onebalance resource exists per user.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Freshness of each source that contributed to a computed balance or selection.
    selection_data_status: Optional[SelectionDataStatus] = None
    # Per-service balance rows for the user. Services listed in unevaluatedServices areomitted. Expand to inline them.
    service_balances: Optional[list[CostManagementUserServiceBalance]] = None
    # Services whose balance could not be evaluated. Empty on a fully successful read; anon-empty collection means the result is partial. When no service could be evaluated, therequest fails with 503 sourceUnavailable. Read-only.
    unevaluated_services: Optional[list[CostManagementUnevaluatedService]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementUserBalance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementUserBalance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementUserBalance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_unevaluated_service import CostManagementUnevaluatedService
        from .cost_management_user_service_balance import CostManagementUserServiceBalance
        from .entity import Entity
        from .selection_data_status import SelectionDataStatus

        from .cost_management_unevaluated_service import CostManagementUnevaluatedService
        from .cost_management_user_service_balance import CostManagementUserServiceBalance
        from .entity import Entity
        from .selection_data_status import SelectionDataStatus

        fields: dict[str, Callable[[Any], None]] = {
            "selectionDataStatus": lambda n : setattr(self, 'selection_data_status', n.get_object_value(SelectionDataStatus)),
            "serviceBalances": lambda n : setattr(self, 'service_balances', n.get_collection_of_object_values(CostManagementUserServiceBalance)),
            "unevaluatedServices": lambda n : setattr(self, 'unevaluated_services', n.get_collection_of_object_values(CostManagementUnevaluatedService)),
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
        writer.write_object_value("selectionDataStatus", self.selection_data_status)
        writer.write_collection_of_object_values("serviceBalances", self.service_balances)
    

