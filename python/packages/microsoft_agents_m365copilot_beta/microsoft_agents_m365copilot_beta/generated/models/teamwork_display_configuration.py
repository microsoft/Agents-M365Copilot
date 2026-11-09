from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_configured_peripheral import TeamworkConfiguredPeripheral
    from .teamwork_display_screen_configuration import TeamworkDisplayScreenConfiguration

@dataclass
class TeamworkDisplayConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The list of configured displays. Applicable only for Microsoft Teams Rooms devices.
    configured_displays: Optional[list[TeamworkConfiguredPeripheral]] = None
    # Total number of connected displays, including the inbuilt display. Applicable only for Teams Rooms devices.
    display_count: Optional[int] = None
    # Configuration for the inbuilt display. Not applicable for Teams Rooms devices.
    in_built_display_screen_configuration: Optional[TeamworkDisplayScreenConfiguration] = None
    # True if content duplication is allowed. Applicable only for Teams Rooms devices.
    is_content_duplication_allowed: Optional[bool] = None
    # True if dual display mode is enabled. If isDualDisplayModeEnabled is true, then the content will be displayed on both front of room screens instead of just the one screen, when it is shared via the HDMI ingest module on the Microsoft Teams Rooms device. Applicable only for Teams Rooms devices.
    is_dual_display_mode_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkDisplayConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDisplayConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDisplayConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_configured_peripheral import TeamworkConfiguredPeripheral
        from .teamwork_display_screen_configuration import TeamworkDisplayScreenConfiguration

        from .teamwork_configured_peripheral import TeamworkConfiguredPeripheral
        from .teamwork_display_screen_configuration import TeamworkDisplayScreenConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "configuredDisplays": lambda n : setattr(self, 'configured_displays', n.get_collection_of_object_values(TeamworkConfiguredPeripheral)),
            "displayCount": lambda n : setattr(self, 'display_count', n.get_int_value()),
            "inBuiltDisplayScreenConfiguration": lambda n : setattr(self, 'in_built_display_screen_configuration', n.get_object_value(TeamworkDisplayScreenConfiguration)),
            "isContentDuplicationAllowed": lambda n : setattr(self, 'is_content_duplication_allowed', n.get_bool_value()),
            "isDualDisplayModeEnabled": lambda n : setattr(self, 'is_dual_display_mode_enabled', n.get_bool_value()),
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
        writer.write_collection_of_object_values("configuredDisplays", self.configured_displays)
        writer.write_int_value("displayCount", self.display_count)
        writer.write_object_value("inBuiltDisplayScreenConfiguration", self.in_built_display_screen_configuration)
        writer.write_bool_value("isContentDuplicationAllowed", self.is_content_duplication_allowed)
        writer.write_bool_value("isDualDisplayModeEnabled", self.is_dual_display_mode_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

