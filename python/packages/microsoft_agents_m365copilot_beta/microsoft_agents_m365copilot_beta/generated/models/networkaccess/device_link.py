from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .bandwidth_capacity_in_mbps import BandwidthCapacityInMbps
    from .bgp_configuration import BgpConfiguration
    from .device_vendor import DeviceVendor
    from .redundancy_configuration import RedundancyConfiguration
    from .tunnel_configuration import TunnelConfiguration

from ..entity import Entity

@dataclass
class DeviceLink(Entity, Parsable):
    # Determines the maximum allowed Mbps (megabits per second) bandwidth from a device link. The possible values are:250,500,750,1000.
    bandwidth_capacity_in_mbps: Optional[BandwidthCapacityInMbps] = None
    # The bgpConfiguration property
    bgp_configuration: Optional[BgpConfiguration] = None
    # The deviceVendor property
    device_vendor: Optional[DeviceVendor] = None
    # The public IP address of your CPE (customer premise equipment) device.
    ip_address: Optional[str] = None
    # last modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The redundancyConfiguration property
    redundancy_configuration: Optional[RedundancyConfiguration] = None
    # The tunnelConfiguration property
    tunnel_configuration: Optional[TunnelConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .bandwidth_capacity_in_mbps import BandwidthCapacityInMbps
        from .bgp_configuration import BgpConfiguration
        from .device_vendor import DeviceVendor
        from .redundancy_configuration import RedundancyConfiguration
        from .tunnel_configuration import TunnelConfiguration

        from ..entity import Entity
        from .bandwidth_capacity_in_mbps import BandwidthCapacityInMbps
        from .bgp_configuration import BgpConfiguration
        from .device_vendor import DeviceVendor
        from .redundancy_configuration import RedundancyConfiguration
        from .tunnel_configuration import TunnelConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "bandwidthCapacityInMbps": lambda n : setattr(self, 'bandwidth_capacity_in_mbps', n.get_enum_value(BandwidthCapacityInMbps)),
            "bgpConfiguration": lambda n : setattr(self, 'bgp_configuration', n.get_object_value(BgpConfiguration)),
            "deviceVendor": lambda n : setattr(self, 'device_vendor', n.get_enum_value(DeviceVendor)),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "redundancyConfiguration": lambda n : setattr(self, 'redundancy_configuration', n.get_object_value(RedundancyConfiguration)),
            "tunnelConfiguration": lambda n : setattr(self, 'tunnel_configuration', n.get_object_value(TunnelConfiguration)),
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
        writer.write_enum_value("bandwidthCapacityInMbps", self.bandwidth_capacity_in_mbps)
        writer.write_object_value("bgpConfiguration", self.bgp_configuration)
        writer.write_enum_value("deviceVendor", self.device_vendor)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("redundancyConfiguration", self.redundancy_configuration)
        writer.write_object_value("tunnelConfiguration", self.tunnel_configuration)
    

