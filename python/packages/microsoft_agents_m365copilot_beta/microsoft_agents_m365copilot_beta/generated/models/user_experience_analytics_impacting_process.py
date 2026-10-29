from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsImpactingProcess(Entity, Parsable):
    """
    The user experience analytics top impacting process entity.
    """
    # The category of impacting process.
    category: Optional[str] = None
    # The description of process.
    description: Optional[str] = None
    # The unique identifier of the impacted device.
    device_id: Optional[str] = None
    # The impact value of the process. Valid values 0 to 1.79769313486232E+308
    impact_value: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The process name.
    process_name: Optional[str] = None
    # The publisher of the process.
    publisher: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsImpactingProcess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsImpactingProcess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsImpactingProcess()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "impactValue": lambda n : setattr(self, 'impact_value', n.get_float_value()),
            "processName": lambda n : setattr(self, 'process_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_float_value("impactValue", self.impact_value)
        writer.write_str_value("processName", self.process_name)
        writer.write_str_value("publisher", self.publisher)
    

