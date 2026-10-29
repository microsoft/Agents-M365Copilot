from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ManagedDeviceWindowsOperatingSystemUpdate(AdditionalDataHolder, Parsable):
    """
    Updates for different Windows' versions are usually released on the Patch Tuesday or B-week  of each month. This complex type defines the Build-version and the release-date for a particular B-week update of the Windows' version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the build version for associated windows update. Windows Operating System updates are usually released on the Patch Tuesday or B-week of each month. Read-only.
    build_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the Month in which this B-week update was released. Read-only.
    release_month: Optional[int] = None
    # Indicates the Year in which this B-week update was released. Read-only.
    release_year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceWindowsOperatingSystemUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceWindowsOperatingSystemUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceWindowsOperatingSystemUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "buildVersion": lambda n : setattr(self, 'build_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "releaseMonth": lambda n : setattr(self, 'release_month', n.get_int_value()),
            "releaseYear": lambda n : setattr(self, 'release_year', n.get_int_value()),
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
        writer.write_str_value("buildVersion", self.build_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("releaseMonth", self.release_month)
        writer.write_int_value("releaseYear", self.release_year)
        writer.write_additional_data_value(self.additional_data)
    

