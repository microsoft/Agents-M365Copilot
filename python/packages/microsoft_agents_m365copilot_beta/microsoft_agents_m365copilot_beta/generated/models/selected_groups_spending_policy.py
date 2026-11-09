from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group import Group
    from .spending_policy import SpendingPolicy

from .spending_policy import SpendingPolicy

@dataclass
class SelectedGroupsSpendingPolicy(SpendingPolicy, Parsable):
    """
    A spending policy that governs only the users in its assigned groups. Omitting assignedGroupsor supplying an empty collection creates a disabled policy that is not enforced. The policytakes effect after at least one valid group is assigned and its other requirements are satisfied.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.selectedGroupsSpendingPolicy"
    # The groups the policy is assigned to. On create, omit this property or supply an emptycollection to create a disabled policy. Add the first group later through theassignedGroups/$ref operation to activate the policy when its other requirements are satisfied.
    assigned_groups: Optional[list[Group]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelectedGroupsSpendingPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelectedGroupsSpendingPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelectedGroupsSpendingPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .group import Group
        from .spending_policy import SpendingPolicy

        from .group import Group
        from .spending_policy import SpendingPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "assignedGroups": lambda n : setattr(self, 'assigned_groups', n.get_collection_of_object_values(Group)),
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
        writer.write_collection_of_object_values("assignedGroups", self.assigned_groups)
    

