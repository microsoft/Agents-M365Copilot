from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AndroidDeviceOwnerSystemUpdateFreezePeriod(AdditionalDataHolder, Parsable):
    """
    Represents one item in the list of freeze periods for Android Device Owner system updates
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The day of the end date of the freeze period. Valid values 1 to 31
    end_day: Optional[int] = None
    # The month of the end date of the freeze period. Valid values 1 to 12
    end_month: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The day of the start date of the freeze period. Valid values 1 to 31
    start_day: Optional[int] = None
    # The month of the start date of the freeze period. Valid values 1 to 12
    start_month: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidDeviceOwnerSystemUpdateFreezePeriod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceOwnerSystemUpdateFreezePeriod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidDeviceOwnerSystemUpdateFreezePeriod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "endDay": lambda n : setattr(self, 'end_day', n.get_int_value()),
            "endMonth": lambda n : setattr(self, 'end_month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDay": lambda n : setattr(self, 'start_day', n.get_int_value()),
            "startMonth": lambda n : setattr(self, 'start_month', n.get_int_value()),
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
        writer.write_int_value("endDay", self.end_day)
        writer.write_int_value("endMonth", self.end_month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("startDay", self.start_day)
        writer.write_int_value("startMonth", self.start_month)
        writer.write_additional_data_value(self.additional_data)
    

