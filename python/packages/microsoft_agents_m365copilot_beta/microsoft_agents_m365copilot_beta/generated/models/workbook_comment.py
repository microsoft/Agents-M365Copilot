from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_comment_mention import WorkbookCommentMention
    from .workbook_comment_reply import WorkbookCommentReply
    from .workbook_document_task import WorkbookDocumentTask

from .entity import Entity

@dataclass
class WorkbookComment(Entity, Parsable):
    # The cell where the comment is located. The address value is in A1-style, which contains the sheet reference (for example, Sheet1!A1). Read-only.
    cell_address: Optional[str] = None
    # The content of the comment that is the String displayed to end-users.
    content: Optional[str] = None
    # The content type of the comment. Supported values are: plain, mention.
    content_type: Optional[str] = None
    # A collection that contains all the people mentioned within the comment. When contentType is plain, this property is an empty array. Read-only.
    mentions: Optional[list[WorkbookCommentMention]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of replies to the comment. Read-only. Nullable.
    replies: Optional[list[WorkbookCommentReply]] = None
    # The rich content of the comment (for example, comment content with mentions, where the first mentioned entity has an ID attribute of 0 and the second has an ID attribute of 1). When contentType is plain, this property is empty. Read-only.
    rich_content: Optional[str] = None
    # The task associated with the comment. Read-only. Nullable.
    task: Optional[WorkbookDocumentTask] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookComment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookComment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_comment_mention import WorkbookCommentMention
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_document_task import WorkbookDocumentTask

        from .entity import Entity
        from .workbook_comment_mention import WorkbookCommentMention
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_document_task import WorkbookDocumentTask

        fields: dict[str, Callable[[Any], None]] = {
            "cellAddress": lambda n : setattr(self, 'cell_address', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "mentions": lambda n : setattr(self, 'mentions', n.get_collection_of_object_values(WorkbookCommentMention)),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(WorkbookCommentReply)),
            "richContent": lambda n : setattr(self, 'rich_content', n.get_str_value()),
            "task": lambda n : setattr(self, 'task', n.get_object_value(WorkbookDocumentTask)),
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
        writer.write_str_value("cellAddress", self.cell_address)
        writer.write_str_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
        writer.write_collection_of_object_values("mentions", self.mentions)
        writer.write_collection_of_object_values("replies", self.replies)
        writer.write_str_value("richContent", self.rich_content)
        writer.write_object_value("task", self.task)
    

