from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize
    from .windows_kiosk_app_type import WindowsKioskAppType
    from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
    from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
    from .windows_kiosk_win32_app import WindowsKioskWin32App

@dataclass
class WindowsKioskAppBase(AdditionalDataHolder, Parsable):
    """
    The base class for a type of apps
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The type of Windows kiosk app.
    app_type: Optional[WindowsKioskAppType] = None
    # Allow the app to be auto-launched in multi-app kiosk mode
    auto_launch: Optional[bool] = None
    # Represents the friendly name of an app
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tile size of Windows app in the start layout.
    start_layout_tile_size: Optional[WindowsAppStartLayoutTileSize] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskAppBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskAppBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskDesktopApp".casefold():
            from .windows_kiosk_desktop_app import WindowsKioskDesktopApp

            return WindowsKioskDesktopApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskUWPApp".casefold():
            from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp

            return WindowsKioskUWPApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsKioskWin32App".casefold():
            from .windows_kiosk_win32_app import WindowsKioskWin32App

            return WindowsKioskWin32App()
        return WindowsKioskAppBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize
        from .windows_kiosk_app_type import WindowsKioskAppType
        from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
        from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
        from .windows_kiosk_win32_app import WindowsKioskWin32App

        from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize
        from .windows_kiosk_app_type import WindowsKioskAppType
        from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
        from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
        from .windows_kiosk_win32_app import WindowsKioskWin32App

        fields: dict[str, Callable[[Any], None]] = {
            "appType": lambda n : setattr(self, 'app_type', n.get_enum_value(WindowsKioskAppType)),
            "autoLaunch": lambda n : setattr(self, 'auto_launch', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startLayoutTileSize": lambda n : setattr(self, 'start_layout_tile_size', n.get_enum_value(WindowsAppStartLayoutTileSize)),
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
        writer.write_enum_value("appType", self.app_type)
        writer.write_bool_value("autoLaunch", self.auto_launch)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("startLayoutTileSize", self.start_layout_tile_size)
        writer.write_additional_data_value(self.additional_data)
    

