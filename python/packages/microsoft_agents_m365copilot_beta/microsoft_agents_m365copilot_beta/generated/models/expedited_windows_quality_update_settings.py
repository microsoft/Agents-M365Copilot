from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ExpeditedWindowsQualityUpdateSettings(AdditionalDataHolder, Parsable):
    """
    A complex type to store the expedited quality update settings such as release date and days until forced reboot.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of days after installation that forced reboot will happen.
    days_until_forced_reboot: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the quality update catalog item targeted by the expedite.
    quality_update_catalog_item_id: Optional[str] = None
    # The release date to identify a quality update.
    quality_update_release: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExpeditedWindowsQualityUpdateSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExpeditedWindowsQualityUpdateSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExpeditedWindowsQualityUpdateSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "daysUntilForcedReboot": lambda n : setattr(self, 'days_until_forced_reboot', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qualityUpdateCatalogItemId": lambda n : setattr(self, 'quality_update_catalog_item_id', n.get_str_value()),
            "qualityUpdateRelease": lambda n : setattr(self, 'quality_update_release', n.get_str_value()),
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
        writer.write_int_value("daysUntilForcedReboot", self.days_until_forced_reboot)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityUpdateCatalogItemId", self.quality_update_catalog_item_id)
        writer.write_str_value("qualityUpdateRelease", self.quality_update_release)
        writer.write_additional_data_value(self.additional_data)
    

