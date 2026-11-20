from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .outlook_task_folder import OutlookTaskFolder

from .entity import Entity

@dataclass
class OutlookTaskGroup(Entity, Parsable):
    # The version of the task group.
    change_key: Optional[str] = None
    # The unique GUID identifier for the task group.
    group_key: Optional[UUID] = None
    # True if the task group is the default task group.
    is_default_group: Optional[bool] = None
    # The name of the task group.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of task folders in the task group. Read-only. Nullable.
    task_folders: Optional[list[OutlookTaskFolder]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutlookTaskGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookTaskGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutlookTaskGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .outlook_task_folder import OutlookTaskFolder

        from .entity import Entity
        from .outlook_task_folder import OutlookTaskFolder

        fields: dict[str, Callable[[Any], None]] = {
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "groupKey": lambda n : setattr(self, 'group_key', n.get_uuid_value()),
            "isDefaultGroup": lambda n : setattr(self, 'is_default_group', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "taskFolders": lambda n : setattr(self, 'task_folders', n.get_collection_of_object_values(OutlookTaskFolder)),
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
        writer.write_str_value("changeKey", self.change_key)
        writer.write_uuid_value("groupKey", self.group_key)
        writer.write_bool_value("isDefaultGroup", self.is_default_group)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("taskFolders", self.task_folders)
    

