from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SessionMetadataInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The appHost property
    app_host: Optional[str] = None
    # The appHostCategories property
    app_host_categories: Optional[list[str]] = None
    # The appHostFqdn property
    app_host_fqdn: Optional[str] = None
    # The browser property
    browser: Optional[str] = None
    # The browserVersion property
    browser_version: Optional[str] = None
    # The deviceManagementType property
    device_management_type: Optional[str] = None
    # The deviceType property
    device_type: Optional[str] = None
    # The enforcementPlane property
    enforcement_plane: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The osPlatform property
    os_platform: Optional[str] = None
    # The osVersion property
    os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SessionMetadataInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SessionMetadataInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SessionMetadataInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "appHost": lambda n : setattr(self, 'app_host', n.get_str_value()),
            "appHostCategories": lambda n : setattr(self, 'app_host_categories', n.get_collection_of_primitive_values(str)),
            "appHostFqdn": lambda n : setattr(self, 'app_host_fqdn', n.get_str_value()),
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "browserVersion": lambda n : setattr(self, 'browser_version', n.get_str_value()),
            "deviceManagementType": lambda n : setattr(self, 'device_management_type', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "enforcementPlane": lambda n : setattr(self, 'enforcement_plane', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osPlatform": lambda n : setattr(self, 'os_platform', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
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
        writer.write_str_value("appHost", self.app_host)
        writer.write_collection_of_primitive_values("appHostCategories", self.app_host_categories)
        writer.write_str_value("appHostFqdn", self.app_host_fqdn)
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("browserVersion", self.browser_version)
        writer.write_str_value("deviceManagementType", self.device_management_type)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_str_value("enforcementPlane", self.enforcement_plane)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osPlatform", self.os_platform)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_additional_data_value(self.additional_data)
    

