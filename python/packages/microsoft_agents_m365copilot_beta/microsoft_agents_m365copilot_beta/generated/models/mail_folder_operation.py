from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mail_folder_operation_status import MailFolderOperationStatus
    from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation

from .entity import Entity

@dataclass
class MailFolderOperation(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The location of the long-running operation.
    resource_location: Optional[str] = None
    # The status of the long-running operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
    status: Optional[MailFolderOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailFolderOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailFolderOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateAllMessagesReadStateOperation".casefold():
            from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation

            return UpdateAllMessagesReadStateOperation()
        return MailFolderOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mail_folder_operation_status import MailFolderOperationStatus
        from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation

        from .entity import Entity
        from .mail_folder_operation_status import MailFolderOperationStatus
        from .update_all_messages_read_state_operation import UpdateAllMessagesReadStateOperation

        fields: dict[str, Callable[[Any], None]] = {
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MailFolderOperationStatus)),
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
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
    

