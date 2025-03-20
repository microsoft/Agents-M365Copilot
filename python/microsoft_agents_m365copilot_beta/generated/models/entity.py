from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction import AiInteraction
    from .ai_interaction_history import AiInteractionHistory
    from .ai_user import AiUser
    from .copilot_admin import CopilotAdmin
    from .copilot_admin_limited_mode import CopilotAdminLimitedMode
    from .copilot_admin_setting import CopilotAdminSetting

@dataclass
class Entity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteraction".casefold():
            from .ai_interaction import AiInteraction

            return AiInteraction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteractionHistory".casefold():
            from .ai_interaction_history import AiInteractionHistory

            return AiInteractionHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiUser".casefold():
            from .ai_user import AiUser

            return AiUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdmin".casefold():
            from .copilot_admin import CopilotAdmin

            return CopilotAdmin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminLimitedMode".casefold():
            from .copilot_admin_limited_mode import CopilotAdminLimitedMode

            return CopilotAdminLimitedMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminSetting".casefold():
            from .copilot_admin_setting import CopilotAdminSetting

            return CopilotAdminSetting()
        return Entity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_user import AiUser
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting

        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_user import AiUser
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

