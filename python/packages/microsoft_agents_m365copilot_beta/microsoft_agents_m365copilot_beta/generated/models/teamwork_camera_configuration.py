from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_content_camera_configuration import TeamworkContentCameraConfiguration
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkCameraConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cameras property
    cameras: Optional[list[TeamworkPeripheral]] = None
    # The configuration for the content camera.
    content_camera_configuration: Optional[TeamworkContentCameraConfiguration] = None
    # The defaultContentCamera property
    default_content_camera: Optional[TeamworkPeripheral] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkCameraConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkCameraConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkCameraConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_content_camera_configuration import TeamworkContentCameraConfiguration
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_content_camera_configuration import TeamworkContentCameraConfiguration
        from .teamwork_peripheral import TeamworkPeripheral

        fields: dict[str, Callable[[Any], None]] = {
            "cameras": lambda n : setattr(self, 'cameras', n.get_collection_of_object_values(TeamworkPeripheral)),
            "contentCameraConfiguration": lambda n : setattr(self, 'content_camera_configuration', n.get_object_value(TeamworkContentCameraConfiguration)),
            "defaultContentCamera": lambda n : setattr(self, 'default_content_camera', n.get_object_value(TeamworkPeripheral)),
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
        writer.write_collection_of_object_values("cameras", self.cameras)
        writer.write_object_value("contentCameraConfiguration", self.content_camera_configuration)
        writer.write_object_value("defaultContentCamera", self.default_content_camera)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

