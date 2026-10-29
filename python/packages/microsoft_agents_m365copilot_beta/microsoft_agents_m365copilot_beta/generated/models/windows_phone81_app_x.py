from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_lob_app import MobileLobApp
    from .windows_architecture import WindowsArchitecture
    from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
    from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

from .mobile_lob_app import MobileLobApp

@dataclass
class WindowsPhone81AppX(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Windows Phone 8.1 AppX Line Of Business apps. Inherits from graph.mobileLobApp. Will be deprecated in February 2023.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81AppX"
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[WindowsArchitecture] = None
    # The Identity Name.
    identity_name: Optional[str] = None
    # The Identity Publisher Hash.
    identity_publisher_hash: Optional[str] = None
    # The Identity Resource Identifier.
    identity_resource_identifier: Optional[str] = None
    # The identity version.
    identity_version: Optional[str] = None
    # The minimum operating system required for a Windows mobile app.
    minimum_supported_operating_system: Optional[WindowsMinimumOperatingSystem] = None
    # The Phone Product Identifier.
    phone_product_identifier: Optional[str] = None
    # The Phone Publisher Id.
    phone_publisher_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhone81AppX:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81AppX
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81AppXBundle".casefold():
            from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

            return WindowsPhone81AppXBundle()
        return WindowsPhone81AppX()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_lob_app import MobileLobApp
        from .windows_architecture import WindowsArchitecture
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

        from .mobile_lob_app import MobileLobApp
        from .windows_architecture import WindowsArchitecture
        from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
        from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle

        fields: dict[str, Callable[[Any], None]] = {
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_collection_of_enum_values(WindowsArchitecture)),
            "identityName": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identityPublisherHash": lambda n : setattr(self, 'identity_publisher_hash', n.get_str_value()),
            "identityResourceIdentifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(WindowsMinimumOperatingSystem)),
            "phoneProductIdentifier": lambda n : setattr(self, 'phone_product_identifier', n.get_str_value()),
            "phonePublisherId": lambda n : setattr(self, 'phone_publisher_id', n.get_str_value()),
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
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisherHash", self.identity_publisher_hash)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("phoneProductIdentifier", self.phone_product_identifier)
        writer.write_str_value("phonePublisherId", self.phone_publisher_id)
    

