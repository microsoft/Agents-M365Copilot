from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_edge_kiosk_type import WindowsEdgeKioskType
    from .windows_kiosk_app_base import WindowsKioskAppBase

from .windows_kiosk_app_base import WindowsKioskAppBase

@dataclass
class WindowsKioskWin32App(WindowsKioskAppBase, Parsable):
    """
    KioskModeApp v4 for Win32 app support
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskWin32App"
    # This is the classicapppath to be used by v4 Win32 app while in Kiosk Mode
    classic_app_path: Optional[str] = None
    # Edge kiosk (url) for Edge kiosk mode
    edge_kiosk: Optional[str] = None
    # Edge kiosk idle timeout in minutes for Edge kiosk mode. Valid values 0 to 1440
    edge_kiosk_idle_timeout_minutes: Optional[int] = None
    # Edge kiosk type
    edge_kiosk_type: Optional[WindowsEdgeKioskType] = None
    # Edge first run flag for Edge kiosk mode
    edge_no_first_run: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskWin32App:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskWin32App
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskWin32App()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_edge_kiosk_type import WindowsEdgeKioskType
        from .windows_kiosk_app_base import WindowsKioskAppBase

        from .windows_edge_kiosk_type import WindowsEdgeKioskType
        from .windows_kiosk_app_base import WindowsKioskAppBase

        fields: dict[str, Callable[[Any], None]] = {
            "classicAppPath": lambda n : setattr(self, 'classic_app_path', n.get_str_value()),
            "edgeKiosk": lambda n : setattr(self, 'edge_kiosk', n.get_str_value()),
            "edgeKioskIdleTimeoutMinutes": lambda n : setattr(self, 'edge_kiosk_idle_timeout_minutes', n.get_int_value()),
            "edgeKioskType": lambda n : setattr(self, 'edge_kiosk_type', n.get_enum_value(WindowsEdgeKioskType)),
            "edgeNoFirstRun": lambda n : setattr(self, 'edge_no_first_run', n.get_bool_value()),
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
        writer.write_str_value("classicAppPath", self.classic_app_path)
        writer.write_str_value("edgeKiosk", self.edge_kiosk)
        writer.write_int_value("edgeKioskIdleTimeoutMinutes", self.edge_kiosk_idle_timeout_minutes)
        writer.write_enum_value("edgeKioskType", self.edge_kiosk_type)
        writer.write_bool_value("edgeNoFirstRun", self.edge_no_first_run)
    

