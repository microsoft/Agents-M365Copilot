from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_base import WindowsKioskAppBase

from .windows_kiosk_app_base import WindowsKioskAppBase

@dataclass
class WindowsKioskDesktopApp(WindowsKioskAppBase, Parsable):
    """
    The base class for a type of apps
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskDesktopApp"
    # Define the DesktopApplicationID of the app
    desktop_application_id: Optional[str] = None
    # Define the DesktopApplicationLinkPath of the app
    desktop_application_link_path: Optional[str] = None
    # Define the path of a desktop app
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskDesktopApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskDesktopApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskDesktopApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_app_base import WindowsKioskAppBase

        from .windows_kiosk_app_base import WindowsKioskAppBase

        fields: dict[str, Callable[[Any], None]] = {
            "desktopApplicationId": lambda n : setattr(self, 'desktop_application_id', n.get_str_value()),
            "desktopApplicationLinkPath": lambda n : setattr(self, 'desktop_application_link_path', n.get_str_value()),
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
        writer.write_str_value("desktopApplicationId", self.desktop_application_id)
        writer.write_str_value("desktopApplicationLinkPath", self.desktop_application_link_path)
        writer.write_str_value("path", self.path)
    

