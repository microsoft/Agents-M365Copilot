from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_package_information import WindowsPackageInformation
    from .windows_phone81_app_x import WindowsPhone81AppX

from .windows_phone81_app_x import WindowsPhone81AppX

@dataclass
class WindowsPhone81AppXBundle(WindowsPhone81AppX, Parsable):
    """
    Contains properties and inherited properties for Windows Phone 8.1 AppX Bundle Line Of Business apps. Inherits from graph.windowsPhone81AppX (which is also to be deprecated at the same time). Will be deprecated in February 2023.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81AppXBundle"
    # The list of AppX Package Information.
    app_x_package_information_list: Optional[list[WindowsPackageInformation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhone81AppXBundle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81AppXBundle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81AppXBundle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_package_information import WindowsPackageInformation
        from .windows_phone81_app_x import WindowsPhone81AppX

        from .windows_package_information import WindowsPackageInformation
        from .windows_phone81_app_x import WindowsPhone81AppX

        fields: dict[str, Callable[[Any], None]] = {
            "appXPackageInformationList": lambda n : setattr(self, 'app_x_package_information_list', n.get_collection_of_object_values(WindowsPackageInformation)),
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
        writer.write_collection_of_object_values("appXPackageInformationList", self.app_x_package_information_list)
    

