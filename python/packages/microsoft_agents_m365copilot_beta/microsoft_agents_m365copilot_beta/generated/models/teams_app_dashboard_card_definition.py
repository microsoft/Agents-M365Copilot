from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teams_app_dashboard_card_content_source import TeamsAppDashboardCardContentSource
    from .teams_app_dashboard_card_icon import TeamsAppDashboardCardIcon
    from .teams_app_dashboard_card_size import TeamsAppDashboardCardSize

from .entity import Entity

@dataclass
class TeamsAppDashboardCardDefinition(Entity, Parsable):
    # The configuration for the source of the card content. Required.
    content_source: Optional[TeamsAppDashboardCardContentSource] = None
    # The size of the card. The possible values are: medium, large, unknownFutureValue. Required.
    default_size: Optional[TeamsAppDashboardCardSize] = None
    # The description for the card. Required.
    description: Optional[str] = None
    # The name of the card. Required.
    display_name: Optional[str] = None
    # Configuration for the display of the icon in the card picker. If neither this nor any of its properties (iconUrl and officeUIFabricIconName) are specified, the color icon of the app is used. Optional.
    icon: Optional[TeamsAppDashboardCardIcon] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID for the group in the card picker. Required.
    picker_group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDashboardCardDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDashboardCardDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDashboardCardDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teams_app_dashboard_card_content_source import TeamsAppDashboardCardContentSource
        from .teams_app_dashboard_card_icon import TeamsAppDashboardCardIcon
        from .teams_app_dashboard_card_size import TeamsAppDashboardCardSize

        from .entity import Entity
        from .teams_app_dashboard_card_content_source import TeamsAppDashboardCardContentSource
        from .teams_app_dashboard_card_icon import TeamsAppDashboardCardIcon
        from .teams_app_dashboard_card_size import TeamsAppDashboardCardSize

        fields: dict[str, Callable[[Any], None]] = {
            "contentSource": lambda n : setattr(self, 'content_source', n.get_object_value(TeamsAppDashboardCardContentSource)),
            "defaultSize": lambda n : setattr(self, 'default_size', n.get_enum_value(TeamsAppDashboardCardSize)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_object_value(TeamsAppDashboardCardIcon)),
            "pickerGroupId": lambda n : setattr(self, 'picker_group_id', n.get_str_value()),
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
        writer.write_object_value("contentSource", self.content_source)
        writer.write_enum_value("defaultSize", self.default_size)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("icon", self.icon)
        writer.write_str_value("pickerGroupId", self.picker_group_id)
    

