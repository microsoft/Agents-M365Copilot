from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_management_alert_threshold import CostManagementAlertThreshold
    from .entity import Entity
    from .user import User

from .entity import Entity

@dataclass
class CostManagementAlertSetting(Entity, Parsable):
    """
    Notify-only alert configuration for a spending policy. Each policy has at most one,retrieved from its own URL beneath the policy.
    """
    # Whether alerting is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The directory users notified when a threshold is crossed. The address is resolved at sendtime, so a recipient survives a mailbox change. Managed with $ref add and remove. Areference that does not resolve to a user in the tenant is rejected withalertRecipientNotFound.
    recipients: Optional[list[User]] = None
    # The configured thresholds.
    thresholds: Optional[list[CostManagementAlertThreshold]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostManagementAlertSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostManagementAlertSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostManagementAlertSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_management_alert_threshold import CostManagementAlertThreshold
        from .entity import Entity
        from .user import User

        from .cost_management_alert_threshold import CostManagementAlertThreshold
        from .entity import Entity
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(User)),
            "thresholds": lambda n : setattr(self, 'thresholds', n.get_collection_of_object_values(CostManagementAlertThreshold)),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_collection_of_object_values("thresholds", self.thresholds)
    

