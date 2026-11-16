from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
    from .windows_kiosk_win32_app import WindowsKioskWin32App

from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration

@dataclass
class WindowsKioskSingleWin32App(WindowsKioskAppConfiguration, Parsable):
    """
    The class used to identify the single app configuration for the kiosk win32 configuration
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskSingleWin32App"
    # The win32App property
    win32_app: Optional[WindowsKioskWin32App] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskSingleWin32App:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskSingleWin32App
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskSingleWin32App()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_win32_app import WindowsKioskWin32App

        from .windows_kiosk_app_configuration import WindowsKioskAppConfiguration
        from .windows_kiosk_win32_app import WindowsKioskWin32App

        fields: dict[str, Callable[[Any], None]] = {
            "win32App": lambda n : setattr(self, 'win32_app', n.get_object_value(WindowsKioskWin32App)),
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
        writer.write_object_value("win32App", self.win32_app)
    

