from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_schedule_settings import AccessReviewScheduleSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class DirectoryRoleAccessReviewPolicy(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[AccessReviewScheduleSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryRoleAccessReviewPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryRoleAccessReviewPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectoryRoleAccessReviewPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_schedule_settings import AccessReviewScheduleSettings
        from .entity import Entity

        from .access_review_schedule_settings import AccessReviewScheduleSettings
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AccessReviewScheduleSettings)),
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
        writer.write_object_value("settings", self.settings)
    

