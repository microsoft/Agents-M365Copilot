from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_entity_identifier import FileEntityIdentifier
    from .response_action import ResponseAction

from .response_action import ResponseAction

@dataclass
class AllowFileResponseAction(ResponseAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.allowFileResponseAction"
    # Device groups to which the actions set in the custom detection rule are applied. More information
    device_group_names: Optional[list[str]] = None
    # The identifier property
    identifier: Optional[FileEntityIdentifier] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AllowFileResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AllowFileResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AllowFileResponseAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_entity_identifier import FileEntityIdentifier
        from .response_action import ResponseAction

        from .file_entity_identifier import FileEntityIdentifier
        from .response_action import ResponseAction

        fields: dict[str, Callable[[Any], None]] = {
            "deviceGroupNames": lambda n : setattr(self, 'device_group_names', n.get_collection_of_primitive_values(str)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_collection_of_enum_values(FileEntityIdentifier)),
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
        writer.write_collection_of_primitive_values("deviceGroupNames", self.device_group_names)
        writer.write_enum_value("identifier", self.identifier)
    

