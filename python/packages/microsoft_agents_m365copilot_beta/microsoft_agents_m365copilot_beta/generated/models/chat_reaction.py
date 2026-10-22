from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .creation_timestamp import CreationTimestamp

@dataclass
class ChatReaction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the reaction (for example, an emoji key).
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Users who applied the reaction, and when.
    users: Optional[list[CreationTimestamp]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatReaction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatReaction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .creation_timestamp import CreationTimestamp

        from .creation_timestamp import CreationTimestamp

        fields: dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(CreationTimestamp)),
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
        writer.write_str_value("key", self.key)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_additional_data_value(self.additional_data)
    

