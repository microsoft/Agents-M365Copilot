from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet

@dataclass
class CommentAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If true, this activity was a reply to an existing comment thread.
    is_reply: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity of the user who started the comment thread.
    parent_author: Optional[IdentitySet] = None
    # The identities of the users participating in this comment thread.
    participants: Optional[list[IdentitySet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommentAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommentAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommentAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet

        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "isReply": lambda n : setattr(self, 'is_reply', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentAuthor": lambda n : setattr(self, 'parent_author', n.get_object_value(IdentitySet)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(IdentitySet)),
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
        writer.write_bool_value("isReply", self.is_reply)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parentAuthor", self.parent_author)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_additional_data_value(self.additional_data)
    

