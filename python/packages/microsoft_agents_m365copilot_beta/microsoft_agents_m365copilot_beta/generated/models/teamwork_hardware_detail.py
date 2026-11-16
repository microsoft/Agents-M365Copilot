from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkHardwareDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # MAC address.
    mac_addresses: Optional[list[str]] = None
    # Device manufacturer.
    manufacturer: Optional[str] = None
    # Devie model.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device serial number.
    serial_number: Optional[str] = None
    # The unique identifier for the device.
    unique_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkHardwareDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkHardwareDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "macAddresses": lambda n : setattr(self, 'mac_addresses', n.get_collection_of_primitive_values(str)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "uniqueId": lambda n : setattr(self, 'unique_id', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("macAddresses", self.mac_addresses)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_additional_data_value(self.additional_data)
    

