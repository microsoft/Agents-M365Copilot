from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_detection import Win32LobAppDetection
    from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

from .win32_lob_app_detection import Win32LobAppDetection

@dataclass
class Win32LobAppProductCodeDetection(Win32LobAppDetection, Parsable):
    """
    Contains product code and version properties to detect a Win32 App
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppProductCodeDetection"
    # The product code of Win32 Line of Business (LoB) app.
    product_code: Optional[str] = None
    # The product version of Win32 Line of Business (LoB) app.
    product_version: Optional[str] = None
    # Contains properties for detection operator.
    product_version_operator: Optional[Win32LobAppDetectionOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppProductCodeDetection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppProductCodeDetection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppProductCodeDetection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_detection import Win32LobAppDetection
        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

        from .win32_lob_app_detection import Win32LobAppDetection
        from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

        fields: dict[str, Callable[[Any], None]] = {
            "productCode": lambda n : setattr(self, 'product_code', n.get_str_value()),
            "productVersion": lambda n : setattr(self, 'product_version', n.get_str_value()),
            "productVersionOperator": lambda n : setattr(self, 'product_version_operator', n.get_collection_of_enum_values(Win32LobAppDetectionOperator)),
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
        writer.write_str_value("productCode", self.product_code)
        writer.write_str_value("productVersion", self.product_version)
        writer.write_enum_value("productVersionOperator", self.product_version_operator)
    

