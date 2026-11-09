from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comment_action import CommentAction
    from .create_action import CreateAction
    from .delete_action import DeleteAction
    from .edit_action import EditAction
    from .mention_action import MentionAction
    from .move_action import MoveAction
    from .rename_action import RenameAction
    from .restore_action import RestoreAction
    from .share_action import ShareAction
    from .version_action import VersionAction

@dataclass
class ItemActionSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A comment was added to the item.
    comment: Optional[CommentAction] = None
    # An item was created.
    create: Optional[CreateAction] = None
    # An item was deleted.
    delete: Optional[DeleteAction] = None
    # An item was edited.
    edit: Optional[EditAction] = None
    # A user was mentioned in the item.
    mention: Optional[MentionAction] = None
    # An item was moved.
    move: Optional[MoveAction] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # An item was renamed.
    rename: Optional[RenameAction] = None
    # An item was restored.
    restore: Optional[RestoreAction] = None
    # An item was shared.
    share: Optional[ShareAction] = None
    # An item was versioned.
    version: Optional[VersionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemActionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemActionSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemActionSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .comment_action import CommentAction
        from .create_action import CreateAction
        from .delete_action import DeleteAction
        from .edit_action import EditAction
        from .mention_action import MentionAction
        from .move_action import MoveAction
        from .rename_action import RenameAction
        from .restore_action import RestoreAction
        from .share_action import ShareAction
        from .version_action import VersionAction

        from .comment_action import CommentAction
        from .create_action import CreateAction
        from .delete_action import DeleteAction
        from .edit_action import EditAction
        from .mention_action import MentionAction
        from .move_action import MoveAction
        from .rename_action import RenameAction
        from .restore_action import RestoreAction
        from .share_action import ShareAction
        from .version_action import VersionAction

        fields: dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_object_value(CommentAction)),
            "create": lambda n : setattr(self, 'create', n.get_object_value(CreateAction)),
            "delete": lambda n : setattr(self, 'delete', n.get_object_value(DeleteAction)),
            "edit": lambda n : setattr(self, 'edit', n.get_object_value(EditAction)),
            "mention": lambda n : setattr(self, 'mention', n.get_object_value(MentionAction)),
            "move": lambda n : setattr(self, 'move', n.get_object_value(MoveAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rename": lambda n : setattr(self, 'rename', n.get_object_value(RenameAction)),
            "restore": lambda n : setattr(self, 'restore', n.get_object_value(RestoreAction)),
            "share": lambda n : setattr(self, 'share', n.get_object_value(ShareAction)),
            "version": lambda n : setattr(self, 'version', n.get_object_value(VersionAction)),
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
        writer.write_object_value("comment", self.comment)
        writer.write_object_value("create", self.create)
        writer.write_object_value("delete", self.delete)
        writer.write_object_value("edit", self.edit)
        writer.write_object_value("mention", self.mention)
        writer.write_object_value("move", self.move)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("rename", self.rename)
        writer.write_object_value("restore", self.restore)
        writer.write_object_value("share", self.share)
        writer.write_object_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

