from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamsAppDashboardCardIcon(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The icon for the card, displayed in the toolbox and card bar, is represented as a URL. The preferred size for raster images is 28x28 pixels. If this property has a value, the officeFabricIconFontName property is ignored.
    icon_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The friendly name of the Office UI Fabric/Fluent UI icon for the card that is used when the iconUrl property isn't specified. For example, 'officeUIFabricIconName': 'Search'.
    office_u_i_fabric_icon_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDashboardCardIcon:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDashboardCardIcon
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDashboardCardIcon()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "officeUIFabricIconName": lambda n : setattr(self, 'office_u_i_fabric_icon_name', n.get_str_value()),
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
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("officeUIFabricIconName", self.office_u_i_fabric_icon_name)
        writer.write_additional_data_value(self.additional_data)
    

