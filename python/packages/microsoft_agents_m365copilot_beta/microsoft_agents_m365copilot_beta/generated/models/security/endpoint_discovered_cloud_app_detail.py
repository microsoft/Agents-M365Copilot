from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .discovered_cloud_app_detail import DiscoveredCloudAppDetail
    from .discovered_cloud_app_device import DiscoveredCloudAppDevice

from .discovered_cloud_app_detail import DiscoveredCloudAppDetail

@dataclass
class EndpointDiscoveredCloudAppDetail(DiscoveredCloudAppDetail, Parsable):
    # The number of devices that accessed the discovered app.
    device_count: Optional[int] = None
    # Represents the devices that access the discovered apps.
    devices: Optional[list[DiscoveredCloudAppDevice]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndpointDiscoveredCloudAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndpointDiscoveredCloudAppDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EndpointDiscoveredCloudAppDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .discovered_cloud_app_detail import DiscoveredCloudAppDetail
        from .discovered_cloud_app_device import DiscoveredCloudAppDevice

        from .discovered_cloud_app_detail import DiscoveredCloudAppDetail
        from .discovered_cloud_app_device import DiscoveredCloudAppDevice

        fields: dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "devices": lambda n : setattr(self, 'devices', n.get_collection_of_object_values(DiscoveredCloudAppDevice)),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_collection_of_object_values("devices", self.devices)
    

