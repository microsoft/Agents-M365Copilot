from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_device_windows_operating_system_edition_type import ManagedDeviceWindowsOperatingSystemEditionType

@dataclass
class ManagedDeviceWindowsOperatingSystemEdition(AdditionalDataHolder, Parsable):
    """
    Different Windows' versions have Edition specific support timelines. This complex type defines the date until which a particular edition is supported in a Windows' version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Windows Operating System is available in different editions, which have a specific set of features available. This enum type defines the corresponding edition.
    edition_type: Optional[ManagedDeviceWindowsOperatingSystemEditionType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the Date until which this Operating System edition type is officially supported. The Timestamp type represents date and time information using ISO 8601 format and is always in Pacific Time Zone (PT). For example, 2014-01-01 would mean '2014-01-01T07:00:00Z' in UTC time. Returned by default. Read-only.
    support_end_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceWindowsOperatingSystemEdition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceWindowsOperatingSystemEdition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceWindowsOperatingSystemEdition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_device_windows_operating_system_edition_type import ManagedDeviceWindowsOperatingSystemEditionType

        from .managed_device_windows_operating_system_edition_type import ManagedDeviceWindowsOperatingSystemEditionType

        fields: dict[str, Callable[[Any], None]] = {
            "editionType": lambda n : setattr(self, 'edition_type', n.get_enum_value(ManagedDeviceWindowsOperatingSystemEditionType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportEndDate": lambda n : setattr(self, 'support_end_date', n.get_date_value()),
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
        writer.write_enum_value("editionType", self.edition_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_date_value("supportEndDate", self.support_end_date)
        writer.write_additional_data_value(self.additional_data)
    

