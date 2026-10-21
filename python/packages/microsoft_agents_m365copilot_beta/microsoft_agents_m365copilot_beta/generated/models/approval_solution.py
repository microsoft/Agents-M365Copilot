from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_item import ApprovalItem
    from .approval_operation import ApprovalOperation
    from .entity import Entity
    from .provision_state import ProvisionState

from .entity import Entity

@dataclass
class ApprovalSolution(Entity, Parsable):
    # A collection of approval items.
    approval_items: Optional[list[ApprovalItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[list[ApprovalOperation]] = None
    # The approval provisioning status for a tenant on an environment. The possible values are: notProvisioned, provisioningInProgress, provisioningFailed, provisioningCompleted, unknownFutureValue.
    provisioning_status: Optional[ProvisionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalSolution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalSolution
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalSolution()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_item import ApprovalItem
        from .approval_operation import ApprovalOperation
        from .entity import Entity
        from .provision_state import ProvisionState

        from .approval_item import ApprovalItem
        from .approval_operation import ApprovalOperation
        from .entity import Entity
        from .provision_state import ProvisionState

        fields: dict[str, Callable[[Any], None]] = {
            "approvalItems": lambda n : setattr(self, 'approval_items', n.get_collection_of_object_values(ApprovalItem)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(ApprovalOperation)),
            "provisioningStatus": lambda n : setattr(self, 'provisioning_status', n.get_enum_value(ProvisionState)),
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
        writer.write_collection_of_object_values("approvalItems", self.approval_items)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_enum_value("provisioningStatus", self.provisioning_status)
    

