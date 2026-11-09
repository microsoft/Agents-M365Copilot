from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_item import DriveItem
    from .entity import Entity
    from .identity_set import IdentitySet
    from .item_action_set import ItemActionSet
    from .item_activity_time_set import ItemActivityTimeSet
    from .list_item import ListItem

from .entity import Entity

@dataclass
class ItemActivityOLD(Entity, Parsable):
    # The action property
    action: Optional[ItemActionSet] = None
    # The actor property
    actor: Optional[IdentitySet] = None
    # The driveItem property
    drive_item: Optional[DriveItem] = None
    # The listItem property
    list_item: Optional[ListItem] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The times property
    times: Optional[ItemActivityTimeSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemActivityOLD:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityOLD
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemActivityOLD()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_action_set import ItemActionSet
        from .item_activity_time_set import ItemActivityTimeSet
        from .list_item import ListItem

        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_action_set import ItemActionSet
        from .item_activity_time_set import ItemActivityTimeSet
        from .list_item import ListItem

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(ItemActionSet)),
            "actor": lambda n : setattr(self, 'actor', n.get_object_value(IdentitySet)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(DriveItem)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(ListItem)),
            "times": lambda n : setattr(self, 'times', n.get_object_value(ItemActivityTimeSet)),
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
        writer.write_object_value("action", self.action)
        writer.write_object_value("actor", self.actor)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("times", self.times)
    

