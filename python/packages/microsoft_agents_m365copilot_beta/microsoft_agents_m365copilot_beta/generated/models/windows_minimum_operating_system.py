from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class WindowsMinimumOperatingSystem(AdditionalDataHolder, Parsable):
    """
    The minimum operating system required for a Windows mobile app.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Windows version 10.0 or later.
    v10_0: Optional[bool] = None
    # Windows 10 1607 or later.
    v10_1607: Optional[bool] = None
    # Windows 10 1703 or later.
    v10_1703: Optional[bool] = None
    # Windows 10 1709 or later.
    v10_1709: Optional[bool] = None
    # Windows 10 1803 or later.
    v10_1803: Optional[bool] = None
    # Windows 10 1809 or later.
    v10_1809: Optional[bool] = None
    # Windows 10 1903 or later.
    v10_1903: Optional[bool] = None
    # Windows 10 1909 or later.
    v10_1909: Optional[bool] = None
    # Windows 10 2H20 or later.
    v10_2_h20: Optional[bool] = None
    # Windows 10 2004 or later.
    v10_2004: Optional[bool] = None
    # Windows 10 21H1 or later.
    v10_21_h1: Optional[bool] = None
    # Windows version 8.0 or later.
    v8_0: Optional[bool] = None
    # Windows version 8.1 or later.
    v8_1: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsMinimumOperatingSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsMinimumOperatingSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsMinimumOperatingSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "v10_0": lambda n : setattr(self, 'v10_0', n.get_bool_value()),
            "v10_1607": lambda n : setattr(self, 'v10_1607', n.get_bool_value()),
            "v10_1703": lambda n : setattr(self, 'v10_1703', n.get_bool_value()),
            "v10_1709": lambda n : setattr(self, 'v10_1709', n.get_bool_value()),
            "v10_1803": lambda n : setattr(self, 'v10_1803', n.get_bool_value()),
            "v10_1809": lambda n : setattr(self, 'v10_1809', n.get_bool_value()),
            "v10_1903": lambda n : setattr(self, 'v10_1903', n.get_bool_value()),
            "v10_1909": lambda n : setattr(self, 'v10_1909', n.get_bool_value()),
            "v10_2H20": lambda n : setattr(self, 'v10_2_h20', n.get_bool_value()),
            "v10_2004": lambda n : setattr(self, 'v10_2004', n.get_bool_value()),
            "v10_21H1": lambda n : setattr(self, 'v10_21_h1', n.get_bool_value()),
            "v8_0": lambda n : setattr(self, 'v8_0', n.get_bool_value()),
            "v8_1": lambda n : setattr(self, 'v8_1', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("v10_0", self.v10_0)
        writer.write_bool_value("v10_1607", self.v10_1607)
        writer.write_bool_value("v10_1703", self.v10_1703)
        writer.write_bool_value("v10_1709", self.v10_1709)
        writer.write_bool_value("v10_1803", self.v10_1803)
        writer.write_bool_value("v10_1809", self.v10_1809)
        writer.write_bool_value("v10_1903", self.v10_1903)
        writer.write_bool_value("v10_1909", self.v10_1909)
        writer.write_bool_value("v10_2H20", self.v10_2_h20)
        writer.write_bool_value("v10_2004", self.v10_2004)
        writer.write_bool_value("v10_21H1", self.v10_21_h1)
        writer.write_bool_value("v8_0", self.v8_0)
        writer.write_bool_value("v8_1", self.v8_1)
        writer.write_additional_data_value(self.additional_data)
    

