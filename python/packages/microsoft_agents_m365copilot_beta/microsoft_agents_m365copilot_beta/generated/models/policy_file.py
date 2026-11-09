from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .policy_file_status import PolicyFileStatus
    from .policy_file_type import PolicyFileType

from .entity import Entity

@dataclass
class PolicyFile(Entity, Parsable):
    # The content property
    content: Optional[bytes] = None
    # The fileType property
    file_type: Optional[PolicyFileType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[PolicyFileStatus] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .policy_file_status import PolicyFileStatus
        from .policy_file_type import PolicyFileType

        from .entity import Entity
        from .policy_file_status import PolicyFileStatus
        from .policy_file_type import PolicyFileType

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_enum_value(PolicyFileType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PolicyFileStatus)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_bytes_value("content", self.content)
        writer.write_enum_value("fileType", self.file_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("version", self.version)
    

