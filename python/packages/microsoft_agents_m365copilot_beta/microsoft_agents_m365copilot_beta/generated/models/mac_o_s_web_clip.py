from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class MacOSWebClip(MobileApp, Parsable):
    """
    Contains properties and inherited properties for macOS web apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSWebClip"
    # The web app URL starting with http:// or https://, such as https://learn.microsoft.com/mem/.
    app_url: Optional[str] = None
    # Whether or not to open the web clip as a full-screen web app. Defaults to false. If TRUE, opens the web clip as a full-screen web app. If FALSE, the web clip opens inside of another app.
    full_screen_enabled: Optional[bool] = None
    # Whether or not the icon for the app is precomosed. Defaults to false. If TRUE, prevents SpringBoard from adding 'shine' to the icon. If FALSE, SpringBoard can add 'shine'.
    pre_composed_icon_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSWebClip:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSWebClip
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSWebClip()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp

        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appUrl": lambda n : setattr(self, 'app_url', n.get_str_value()),
            "fullScreenEnabled": lambda n : setattr(self, 'full_screen_enabled', n.get_bool_value()),
            "preComposedIconEnabled": lambda n : setattr(self, 'pre_composed_icon_enabled', n.get_bool_value()),
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
        writer.write_str_value("appUrl", self.app_url)
        writer.write_bool_value("fullScreenEnabled", self.full_screen_enabled)
        writer.write_bool_value("preComposedIconEnabled", self.pre_composed_icon_enabled)
    

