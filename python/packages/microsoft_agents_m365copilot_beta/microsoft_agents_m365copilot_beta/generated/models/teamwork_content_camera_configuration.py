from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamworkContentCameraConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # True if the content camera is inverted.
    is_content_camera_inverted: Optional[bool] = None
    # True if the content camera is optional.
    is_content_camera_optional: Optional[bool] = None
    # True if the content enhancement is enabled.
    is_content_enhancement_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkContentCameraConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkContentCameraConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkContentCameraConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isContentCameraInverted": lambda n : setattr(self, 'is_content_camera_inverted', n.get_bool_value()),
            "isContentCameraOptional": lambda n : setattr(self, 'is_content_camera_optional', n.get_bool_value()),
            "isContentEnhancementEnabled": lambda n : setattr(self, 'is_content_enhancement_enabled', n.get_bool_value()),
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
        writer.write_bool_value("isContentCameraInverted", self.is_content_camera_inverted)
        writer.write_bool_value("isContentCameraOptional", self.is_content_camera_optional)
        writer.write_bool_value("isContentEnhancementEnabled", self.is_content_enhancement_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

