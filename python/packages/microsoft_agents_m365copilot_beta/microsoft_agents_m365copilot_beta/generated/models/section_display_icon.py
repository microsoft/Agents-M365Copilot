from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .section_icon_skin_tone import SectionIconSkinTone

@dataclass
class SectionDisplayIcon(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The URL to a custom icon image. Applicable when iconType is custom.
    content_url: Optional[str] = None
    # The human-readable name of the icon.
    display_name: Optional[str] = None
    # The type of icon. Use an emoji character such as 👍 for an emoji icon, or custom for a custom image icon.
    icon_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The skin tone variant applied to the icon. Read-only. The possible values are: light, mediumLight, medium, mediumDark, dark, unknownFutureValue.
    skin_tone: Optional[SectionIconSkinTone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SectionDisplayIcon:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SectionDisplayIcon
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SectionDisplayIcon()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .section_icon_skin_tone import SectionIconSkinTone

        from .section_icon_skin_tone import SectionIconSkinTone

        fields: dict[str, Callable[[Any], None]] = {
            "contentUrl": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "iconType": lambda n : setattr(self, 'icon_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skinTone": lambda n : setattr(self, 'skin_tone', n.get_enum_value(SectionIconSkinTone)),
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
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("iconType", self.icon_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("skinTone", self.skin_tone)
        writer.write_additional_data_value(self.additional_data)
    

