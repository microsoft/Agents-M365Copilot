from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DriveItemAccessOperationsViewpoint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the user can comment on this item.
    can_comment: Optional[bool] = None
    # Indicates whether the user can create files within this object. Returned only on folders.
    can_create_file: Optional[bool] = None
    # Indicates whether the user can create folders within this object. Returned only on folders.
    can_create_folder: Optional[bool] = None
    # Indicates whether the user can delete this item.
    can_delete: Optional[bool] = None
    # Indicates whether the user can download this item.
    can_download: Optional[bool] = None
    # Indicates whether the user can read this item.
    can_read: Optional[bool] = None
    # Indicates whether the user can update this item.
    can_update: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveItemAccessOperationsViewpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemAccessOperationsViewpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveItemAccessOperationsViewpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "canComment": lambda n : setattr(self, 'can_comment', n.get_bool_value()),
            "canCreateFile": lambda n : setattr(self, 'can_create_file', n.get_bool_value()),
            "canCreateFolder": lambda n : setattr(self, 'can_create_folder', n.get_bool_value()),
            "canDelete": lambda n : setattr(self, 'can_delete', n.get_bool_value()),
            "canDownload": lambda n : setattr(self, 'can_download', n.get_bool_value()),
            "canRead": lambda n : setattr(self, 'can_read', n.get_bool_value()),
            "canUpdate": lambda n : setattr(self, 'can_update', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("canComment", self.can_comment)
        writer.write_bool_value("canCreateFile", self.can_create_file)
        writer.write_bool_value("canCreateFolder", self.can_create_folder)
        writer.write_bool_value("canDelete", self.can_delete)
        writer.write_bool_value("canDownload", self.can_download)
        writer.write_bool_value("canRead", self.can_read)
        writer.write_bool_value("canUpdate", self.can_update)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

