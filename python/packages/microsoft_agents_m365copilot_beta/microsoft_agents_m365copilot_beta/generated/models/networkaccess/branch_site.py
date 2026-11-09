from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .branch_connectivity_configuration import BranchConnectivityConfiguration
    from .connectivity_state import ConnectivityState
    from .device_link import DeviceLink
    from .forwarding_profile import ForwardingProfile
    from .region import Region

from ..entity import Entity

@dataclass
class BranchSite(Entity, Parsable):
    # Determines the maximum allowed Mbps (megabits per second) bandwidth from a branch site. The possible values are:250,500,750,1000.
    bandwidth_capacity: Optional[int] = None
    # Specifies the connectivity details of all device links associated with a branch.
    connectivity_configuration: Optional[BranchConnectivityConfiguration] = None
    # Determines the branch site status. The possible values are: pending, connected, inactive, error.
    connectivity_state: Optional[ConnectivityState] = None
    # The branch site is created in the specified country. DO NOT USE.
    country: Optional[str] = None
    # Each unique CPE device associated with a branch is specified. Supports $expand.
    device_links: Optional[list[DeviceLink]] = None
    # Each forwarding profile associated with a branch site is specified. Supports $expand.
    forwarding_profiles: Optional[list[ForwardingProfile]] = None
    # last modified time.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The region property
    region: Optional[Region] = None
    # The branch version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BranchSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BranchSite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BranchSite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .branch_connectivity_configuration import BranchConnectivityConfiguration
        from .connectivity_state import ConnectivityState
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region

        from ..entity import Entity
        from .branch_connectivity_configuration import BranchConnectivityConfiguration
        from .connectivity_state import ConnectivityState
        from .device_link import DeviceLink
        from .forwarding_profile import ForwardingProfile
        from .region import Region

        fields: dict[str, Callable[[Any], None]] = {
            "bandwidthCapacity": lambda n : setattr(self, 'bandwidth_capacity', n.get_int_value()),
            "connectivityConfiguration": lambda n : setattr(self, 'connectivity_configuration', n.get_object_value(BranchConnectivityConfiguration)),
            "connectivityState": lambda n : setattr(self, 'connectivity_state', n.get_enum_value(ConnectivityState)),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "deviceLinks": lambda n : setattr(self, 'device_links', n.get_collection_of_object_values(DeviceLink)),
            "forwardingProfiles": lambda n : setattr(self, 'forwarding_profiles', n.get_collection_of_object_values(ForwardingProfile)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(Region)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_int_value("bandwidthCapacity", self.bandwidth_capacity)
        writer.write_object_value("connectivityConfiguration", self.connectivity_configuration)
        writer.write_enum_value("connectivityState", self.connectivity_state)
        writer.write_str_value("country", self.country)
        writer.write_collection_of_object_values("deviceLinks", self.device_links)
        writer.write_collection_of_object_values("forwardingProfiles", self.forwarding_profiles)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
        writer.write_str_value("version", self.version)
    

