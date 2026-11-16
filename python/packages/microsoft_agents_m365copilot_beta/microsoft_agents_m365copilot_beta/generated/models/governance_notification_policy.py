from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .governance_notification_template import GovernanceNotificationTemplate

@dataclass
class GovernanceNotificationPolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The enabledTemplateTypes property
    enabled_template_types: Optional[list[str]] = None
    # The notificationTemplates property
    notification_templates: Optional[list[GovernanceNotificationTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GovernanceNotificationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GovernanceNotificationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GovernanceNotificationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .governance_notification_template import GovernanceNotificationTemplate

        from .governance_notification_template import GovernanceNotificationTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "enabledTemplateTypes": lambda n : setattr(self, 'enabled_template_types', n.get_collection_of_primitive_values(str)),
            "notificationTemplates": lambda n : setattr(self, 'notification_templates', n.get_collection_of_object_values(GovernanceNotificationTemplate)),
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
        writer.write_collection_of_primitive_values("enabledTemplateTypes", self.enabled_template_types)
        writer.write_collection_of_object_values("notificationTemplates", self.notification_templates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

