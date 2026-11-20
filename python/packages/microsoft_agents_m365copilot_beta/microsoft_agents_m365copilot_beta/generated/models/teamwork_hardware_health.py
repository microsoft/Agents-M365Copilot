from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral_health import TeamworkPeripheralHealth

@dataclass
class TeamworkHardwareHealth(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The system health details for a teamworkDevice.
    compute_health: Optional[TeamworkPeripheralHealth] = None
    # The health details about the HDMI ingest of a device.
    hdmi_ingest_health: Optional[TeamworkPeripheralHealth] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkHardwareHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkHardwareHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral_health import TeamworkPeripheralHealth

        from .teamwork_peripheral_health import TeamworkPeripheralHealth

        fields: dict[str, Callable[[Any], None]] = {
            "computeHealth": lambda n : setattr(self, 'compute_health', n.get_object_value(TeamworkPeripheralHealth)),
            "hdmiIngestHealth": lambda n : setattr(self, 'hdmi_ingest_health', n.get_object_value(TeamworkPeripheralHealth)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("computeHealth", self.compute_health)
        writer.write_object_value("hdmiIngestHealth", self.hdmi_ingest_health)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

