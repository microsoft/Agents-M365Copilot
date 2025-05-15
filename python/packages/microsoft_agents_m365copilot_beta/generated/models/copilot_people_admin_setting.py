from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enhanced_personalization_setting import EnhancedPersonalizationSetting
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotPeopleAdminSetting(Entity, Parsable):
    # The enhancedPersonalization property
    enhanced_personalization: Optional[EnhancedPersonalizationSetting] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPeopleAdminSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPeopleAdminSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPeopleAdminSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enhanced_personalization_setting import EnhancedPersonalizationSetting
        from .entity import Entity

        from .enhanced_personalization_setting import EnhancedPersonalizationSetting
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "enhancedPersonalization": lambda n : setattr(self, 'enhanced_personalization', n.get_object_value(EnhancedPersonalizationSetting)),
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
        writer.write_object_value("enhancedPersonalization", self.enhanced_personalization)
    

