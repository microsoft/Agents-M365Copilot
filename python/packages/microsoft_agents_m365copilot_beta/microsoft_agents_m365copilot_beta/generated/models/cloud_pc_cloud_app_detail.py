from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_automatic_discovered_app_detail import CloudPcAutomaticDiscoveredAppDetail
    from .cloud_pc_file_path_app_detail import CloudPcFilePathAppDetail

@dataclass
class CloudPcCloudAppDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the command-line arguments for the cloud app. These parameters are passed to the cloud app when it's launched. The maximum allowed length for this property is 2,048 characters. For example, -fullscreen -loop.
    command_line_arguments: Optional[str] = None
    # Specifies the path to the executable file for the application within the OS of the hosting Cloud PC. The value should be an absolute path to a Windows or Universal app. For example, C:/app.exe or shell:AppsFolder/appname!App.
    file_path: Optional[str] = None
    # Specifies the index of the icon within the file specified by the iconPath property. For example, if iconPath is set to C:/Program Files/MyApp/myapp.ico and iconIndex is set to 0, the system uses the first icon in the myapp.ico file. The default value is 0.
    icon_index: Optional[int] = None
    # Specifies the path to the icon file for the application within the OS of the hosting Cloud PC. When an admin updates the path of a cloud app, the value should be a rooted absolute path. For example, C:/Windows/system32/WindowsPowerShell/v1.0/powershell_ise.exe. If this property isn't defined, a default icon is used.
    icon_path: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcCloudAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcCloudAppDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcAutomaticDiscoveredAppDetail".casefold():
            from .cloud_pc_automatic_discovered_app_detail import CloudPcAutomaticDiscoveredAppDetail

            return CloudPcAutomaticDiscoveredAppDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcFilePathAppDetail".casefold():
            from .cloud_pc_file_path_app_detail import CloudPcFilePathAppDetail

            return CloudPcFilePathAppDetail()
        return CloudPcCloudAppDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_automatic_discovered_app_detail import CloudPcAutomaticDiscoveredAppDetail
        from .cloud_pc_file_path_app_detail import CloudPcFilePathAppDetail

        from .cloud_pc_automatic_discovered_app_detail import CloudPcAutomaticDiscoveredAppDetail
        from .cloud_pc_file_path_app_detail import CloudPcFilePathAppDetail

        fields: dict[str, Callable[[Any], None]] = {
            "commandLineArguments": lambda n : setattr(self, 'command_line_arguments', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "iconIndex": lambda n : setattr(self, 'icon_index', n.get_int_value()),
            "iconPath": lambda n : setattr(self, 'icon_path', n.get_str_value()),
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
        writer.write_str_value("commandLineArguments", self.command_line_arguments)
        writer.write_str_value("filePath", self.file_path)
        writer.write_int_value("iconIndex", self.icon_index)
        writer.write_str_value("iconPath", self.icon_path)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

