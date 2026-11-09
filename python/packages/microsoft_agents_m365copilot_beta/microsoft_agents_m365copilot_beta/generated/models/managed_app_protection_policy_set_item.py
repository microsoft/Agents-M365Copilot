from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_set_item import PolicySetItem

from .policy_set_item import PolicySetItem

@dataclass
class ManagedAppProtectionPolicySetItem(PolicySetItem, Parsable):
    """
    A class containing the properties used for managed app protection PolicySetItem.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedAppProtectionPolicySetItem"
    # TargetedAppManagementLevels of the ManagedAppPolicySetItem.
    targeted_app_management_levels: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppProtectionPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppProtectionPolicySetItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppProtectionPolicySetItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_set_item import PolicySetItem

        from .policy_set_item import PolicySetItem

        fields: dict[str, Callable[[Any], None]] = {
            "targetedAppManagementLevels": lambda n : setattr(self, 'targeted_app_management_levels', n.get_str_value()),
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
        writer.write_str_value("targetedAppManagementLevels", self.targeted_app_management_levels)
    

