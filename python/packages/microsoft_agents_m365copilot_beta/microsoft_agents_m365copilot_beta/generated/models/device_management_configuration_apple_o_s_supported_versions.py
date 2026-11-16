from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceManagementConfigurationAppleOSSupportedVersions(AdditionalDataHolder, Parsable):
    """
    Indicates the version range for an apple setting.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the maximum version is included in the supported version range.
    includes_max_version: Optional[bool] = None
    # Indicates whether the minimum version is included in the supported version range.
    includes_min_version: Optional[bool] = None
    # Gets the maximum supported version for an Apple setting.
    max_version: Optional[str] = None
    # Gets the minimum supported version for an Apple setting.
    min_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementConfigurationAppleOSSupportedVersions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementConfigurationAppleOSSupportedVersions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementConfigurationAppleOSSupportedVersions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "includesMaxVersion": lambda n : setattr(self, 'includes_max_version', n.get_bool_value()),
            "includesMinVersion": lambda n : setattr(self, 'includes_min_version', n.get_bool_value()),
            "maxVersion": lambda n : setattr(self, 'max_version', n.get_str_value()),
            "minVersion": lambda n : setattr(self, 'min_version', n.get_str_value()),
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
        writer.write_bool_value("includesMaxVersion", self.includes_max_version)
        writer.write_bool_value("includesMinVersion", self.includes_min_version)
        writer.write_str_value("maxVersion", self.max_version)
        writer.write_str_value("minVersion", self.min_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

