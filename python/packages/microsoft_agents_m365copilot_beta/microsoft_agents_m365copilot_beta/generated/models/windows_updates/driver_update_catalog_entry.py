from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

@dataclass
class DriverUpdateCatalogEntry(SoftwareUpdateCatalogEntry, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry"
    # The description of the content.
    description: Optional[str] = None
    # The classification of the driver.
    driver_class: Optional[str] = None
    # The manufacturer of the driver.
    manufacturer: Optional[str] = None
    # The provider of the driver.
    provider: Optional[str] = None
    # The setup information file of the driver.
    setup_information_file: Optional[str] = None
    # The unique version of the content.
    version: Optional[str] = None
    # The date and time when a new version of content was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    version_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriverUpdateCatalogEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriverUpdateCatalogEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriverUpdateCatalogEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        from .software_update_catalog_entry import SoftwareUpdateCatalogEntry

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "driverClass": lambda n : setattr(self, 'driver_class', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "setupInformationFile": lambda n : setattr(self, 'setup_information_file', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "versionDateTime": lambda n : setattr(self, 'version_date_time', n.get_datetime_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("driverClass", self.driver_class)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("setupInformationFile", self.setup_information_file)
        writer.write_str_value("version", self.version)
        writer.write_datetime_value("versionDateTime", self.version_date_time)
    

