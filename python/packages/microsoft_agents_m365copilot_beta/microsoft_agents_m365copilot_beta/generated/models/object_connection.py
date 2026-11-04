from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ObjectConnection(AdditionalDataHolder, Parsable):
    """
    Represents a connector data store linkage record for an object in a synchronization job.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Display name of the connected object. Nullable. Read-only.
    display_name: Optional[str] = None
    # Identifier supplied in the request to look up the connection. Can be the source or target identifier for the object in the synchronization job. Key. Not nullable. Read-only.
    object_id: Optional[str] = None
    # Logical object type, such as User or Group. Not nullable. Read-only.
    object_type_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Anchor or join value in the source directory. Not nullable. Read-only.
    source_anchor: Optional[str] = None
    # Anchor or transformed identifier in the target space. Not nullable. Read-only.
    target_anchor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "objectTypeName": lambda n : setattr(self, 'object_type_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceAnchor": lambda n : setattr(self, 'source_anchor', n.get_str_value()),
            "targetAnchor": lambda n : setattr(self, 'target_anchor', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("objectTypeName", self.object_type_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceAnchor", self.source_anchor)
        writer.write_str_value("targetAnchor", self.target_anchor)
        writer.write_additional_data_value(self.additional_data)
    

