from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .content_approval import ContentApproval
    from .update_policy import UpdatePolicy

from ..entity import Entity

@dataclass
class ComplianceChange(Entity, Parsable):
    # The date and time when a compliance change was created.
    created_date_time: Optional[datetime.datetime] = None
    # True indicates that a compliance change is revoked, preventing further application. Revoking a compliance change is a final action.
    is_revoked: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the compliance change was revoked.
    revoked_date_time: Optional[datetime.datetime] = None
    # The policy this compliance change is a member of.
    update_policy: Optional[UpdatePolicy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceChange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceChange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.contentApproval".casefold():
            from .content_approval import ContentApproval

            return ContentApproval()
        return ComplianceChange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .content_approval import ContentApproval
        from .update_policy import UpdatePolicy

        from ..entity import Entity
        from .content_approval import ContentApproval
        from .update_policy import UpdatePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isRevoked": lambda n : setattr(self, 'is_revoked', n.get_bool_value()),
            "revokedDateTime": lambda n : setattr(self, 'revoked_date_time', n.get_datetime_value()),
            "updatePolicy": lambda n : setattr(self, 'update_policy', n.get_object_value(UpdatePolicy)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isRevoked", self.is_revoked)
        writer.write_datetime_value("revokedDateTime", self.revoked_date_time)
        writer.write_object_value("updatePolicy", self.update_policy)
    

