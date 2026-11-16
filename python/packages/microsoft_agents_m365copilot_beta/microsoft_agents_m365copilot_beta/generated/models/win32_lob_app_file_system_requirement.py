from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType
    from .win32_lob_app_requirement import Win32LobAppRequirement

from .win32_lob_app_requirement import Win32LobAppRequirement

@dataclass
class Win32LobAppFileSystemRequirement(Win32LobAppRequirement, Parsable):
    """
    Contains file or folder path to detect a Win32 App
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppFileSystemRequirement"
    # A value indicating whether this file or folder is for checking 32-bit app on 64-bit system
    check32_bit_on64_system: Optional[bool] = None
    # Contains all supported file system detection type.
    detection_type: Optional[Win32LobAppFileSystemDetectionType] = None
    # The file or folder name to detect Win32 Line of Business (LoB) app
    file_or_folder_name: Optional[str] = None
    # The file or folder path to detect Win32 Line of Business (LoB) app
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppFileSystemRequirement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppFileSystemRequirement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppFileSystemRequirement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType
        from .win32_lob_app_requirement import Win32LobAppRequirement

        from .win32_lob_app_file_system_detection_type import Win32LobAppFileSystemDetectionType
        from .win32_lob_app_requirement import Win32LobAppRequirement

        fields: dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "detectionType": lambda n : setattr(self, 'detection_type', n.get_enum_value(Win32LobAppFileSystemDetectionType)),
            "fileOrFolderName": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_enum_value("detectionType", self.detection_type)
        writer.write_str_value("fileOrFolderName", self.file_or_folder_name)
        writer.write_str_value("path", self.path)
    

