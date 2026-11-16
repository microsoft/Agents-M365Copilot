from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_lob_app import MobileLobApp
    from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

from .mobile_lob_app import MobileLobApp

@dataclass
class WindowsPhoneXAP(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Windows Phone XAP Line Of Business apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhoneXAP"
    # The identity version.
    identity_version: Optional[str] = None
    # The minimum operating system required for a Windows mobile app.
    minimum_supported_operating_system: Optional[WindowsMinimumOperatingSystem] = None
    # The Product Identifier.
    product_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhoneXAP:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhoneXAP
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhoneXAP()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_lob_app import MobileLobApp
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        from .mobile_lob_app import MobileLobApp
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem

        fields: dict[str, Callable[[Any], None]] = {
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(WindowsMinimumOperatingSystem)),
            "productIdentifier": lambda n : setattr(self, 'product_identifier', n.get_str_value()),
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
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("productIdentifier", self.product_identifier)
    

