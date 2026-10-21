from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .driver_update_filter import DriverUpdateFilter
    from .quality_update_filter import QualityUpdateFilter
    from .remediation_update_filter import RemediationUpdateFilter
    from .software_update_filter import SoftwareUpdateFilter
    from .windows_update_filter import WindowsUpdateFilter

@dataclass
class ContentFilter(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.driverUpdateFilter".casefold():
            from .driver_update_filter import DriverUpdateFilter

            return DriverUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.qualityUpdateFilter".casefold():
            from .quality_update_filter import QualityUpdateFilter

            return QualityUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.remediationUpdateFilter".casefold():
            from .remediation_update_filter import RemediationUpdateFilter

            return RemediationUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.softwareUpdateFilter".casefold():
            from .software_update_filter import SoftwareUpdateFilter

            return SoftwareUpdateFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdates.windowsUpdateFilter".casefold():
            from .windows_update_filter import WindowsUpdateFilter

            return WindowsUpdateFilter()
        return ContentFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .driver_update_filter import DriverUpdateFilter
        from .quality_update_filter import QualityUpdateFilter
        from .remediation_update_filter import RemediationUpdateFilter
        from .software_update_filter import SoftwareUpdateFilter
        from .windows_update_filter import WindowsUpdateFilter

        from .driver_update_filter import DriverUpdateFilter
        from .quality_update_filter import QualityUpdateFilter
        from .remediation_update_filter import RemediationUpdateFilter
        from .software_update_filter import SoftwareUpdateFilter
        from .windows_update_filter import WindowsUpdateFilter

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

