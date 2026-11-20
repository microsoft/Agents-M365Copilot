from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_base import WindowsKioskAppBase
    from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

@dataclass
class WindowsKioskMultipleApps(WindowsKioskAppConfiguration, Parsable):
    """
    The class used to identify the MultiMode app configuration for the kiosk configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskMultipleApps"
    # This setting allows access to Downloads folder in file explorer.
    allow_access_to_downloads_folder: Optional[bool] = None
    # These are the only Windows Store Apps that will be available to launch from the Start menu. This collection can contain a maximum of 128 elements.
    apps: Optional[list[WindowsKioskAppBase]] = None
    # This setting indicates that desktop apps are allowed. Default to true.
    disallow_desktop_apps: Optional[bool] = None
    # This setting allows the admin to specify whether the Task Bar is shown or not.
    show_task_bar: Optional[bool] = None
    # Allows admins to override the default Start layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in Binary format.
    start_menu_layout_xml: Optional[bytes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskMultipleApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskMultipleApps
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskMultipleApps()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_app_base import WindowsKioskAppBase
        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

        from .windows_kiosk_app_base import WindowsKioskAppBase
        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "allowAccessToDownloadsFolder": lambda n : setattr(self, 'allow_access_to_downloads_folder', n.get_bool_value()),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(WindowsKioskAppBase)),
            "disallowDesktopApps": lambda n : setattr(self, 'disallow_desktop_apps', n.get_bool_value()),
            "showTaskBar": lambda n : setattr(self, 'show_task_bar', n.get_bool_value()),
            "startMenuLayoutXml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
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
        writer.write_bool_value("allowAccessToDownloadsFolder", self.allow_access_to_downloads_folder)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_bool_value("disallowDesktopApps", self.disallow_desktop_apps)
        writer.write_bool_value("showTaskBar", self.show_task_bar)
        writer.write_bytes_value("startMenuLayoutXml", self.start_menu_layout_xml)
    

