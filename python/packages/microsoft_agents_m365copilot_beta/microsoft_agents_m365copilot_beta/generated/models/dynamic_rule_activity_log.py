from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_log_base import ActivityLogBase
    from .protection_unit_details import ProtectionUnitDetails

from .activity_log_base import ActivityLogBase

@dataclass
class DynamicRuleActivityLog(ActivityLogBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.dynamicRuleActivityLog"
    # The unique identifier of the protection policy associated with the activity log.
    policy_id: Optional[str] = None
    # Name of the protection policy.
    policy_name: Optional[str] = None
    # Contains Protection unit counts information.
    protection_unit_details: Optional[ProtectionUnitDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamicRuleActivityLog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamicRuleActivityLog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamicRuleActivityLog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_log_base import ActivityLogBase
        from .protection_unit_details import ProtectionUnitDetails

        from .activity_log_base import ActivityLogBase
        from .protection_unit_details import ProtectionUnitDetails

        fields: dict[str, Callable[[Any], None]] = {
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "protectionUnitDetails": lambda n : setattr(self, 'protection_unit_details', n.get_object_value(ProtectionUnitDetails)),
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
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_object_value("protectionUnitDetails", self.protection_unit_details)
    

