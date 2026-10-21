from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_kiosk_app_base import WindowsKioskAppBase

from .windows_kiosk_app_base import WindowsKioskAppBase

@dataclass
class WindowsKioskUWPApp(WindowsKioskAppBase, Parsable):
    """
    The base class for a type of apps
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsKioskUWPApp"
    # This references an Intune App that will be target to the same assignments as Kiosk configuration
    app_id: Optional[str] = None
    # This is the only Application User Model ID (AUMID) that will be available to launch use while in Kiosk Mode
    app_user_model_id: Optional[str] = None
    # This references an contained App from an Intune App
    contained_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsKioskUWPApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsKioskUWPApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsKioskUWPApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_kiosk_app_base import WindowsKioskAppBase

        from .windows_kiosk_app_base import WindowsKioskAppBase

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "appUserModelId": lambda n : setattr(self, 'app_user_model_id', n.get_str_value()),
            "containedAppId": lambda n : setattr(self, 'contained_app_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("appUserModelId", self.app_user_model_id)
        writer.write_str_value("containedAppId", self.contained_app_id)
    

