from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
    from .microsoft_tunnel_server import MicrosoftTunnelServer

from .entity import Entity

@dataclass
class MicrosoftTunnelSite(Entity, Parsable):
    """
    Entity that represents a Microsoft Tunnel site
    """
    # The site's description (optional)
    description: Optional[str] = None
    # The display name for the site. This property is required when a site is created.
    display_name: Optional[str] = None
    # The site's Internal Network Access Probe URL
    internal_network_probe_url: Optional[str] = None
    # The MicrosoftTunnelConfiguration that has been applied to this MicrosoftTunnelSite
    microsoft_tunnel_configuration: Optional[MicrosoftTunnelConfiguration] = None
    # A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
    microsoft_tunnel_servers: Optional[list[MicrosoftTunnelServer]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The site's public domain name or IP address
    public_address: Optional[str] = None
    # List of Scope Tags for this Entity instance
    role_scope_tag_ids: Optional[list[str]] = None
    # The site's automatic upgrade setting. True for automatic upgrades, false for manual control
    upgrade_automatically: Optional[bool] = None
    # The site provides the state of when an upgrade is available
    upgrade_available: Optional[bool] = None
    # The site's upgrade window end time of day
    upgrade_window_end_time: Optional[datetime.time] = None
    # The site's upgrade window start time of day
    upgrade_window_start_time: Optional[datetime.time] = None
    # The site's timezone represented as a minute offset from UTC
    upgrade_window_utc_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelSite:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelSite
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelSite()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from .microsoft_tunnel_server import MicrosoftTunnelServer

        from .entity import Entity
        from .microsoft_tunnel_configuration import MicrosoftTunnelConfiguration
        from .microsoft_tunnel_server import MicrosoftTunnelServer

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "internalNetworkProbeUrl": lambda n : setattr(self, 'internal_network_probe_url', n.get_str_value()),
            "microsoftTunnelConfiguration": lambda n : setattr(self, 'microsoft_tunnel_configuration', n.get_object_value(MicrosoftTunnelConfiguration)),
            "microsoftTunnelServers": lambda n : setattr(self, 'microsoft_tunnel_servers', n.get_collection_of_object_values(MicrosoftTunnelServer)),
            "publicAddress": lambda n : setattr(self, 'public_address', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "upgradeAutomatically": lambda n : setattr(self, 'upgrade_automatically', n.get_bool_value()),
            "upgradeAvailable": lambda n : setattr(self, 'upgrade_available', n.get_bool_value()),
            "upgradeWindowEndTime": lambda n : setattr(self, 'upgrade_window_end_time', n.get_time_value()),
            "upgradeWindowStartTime": lambda n : setattr(self, 'upgrade_window_start_time', n.get_time_value()),
            "upgradeWindowUtcOffsetInMinutes": lambda n : setattr(self, 'upgrade_window_utc_offset_in_minutes', n.get_int_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("internalNetworkProbeUrl", self.internal_network_probe_url)
        writer.write_object_value("microsoftTunnelConfiguration", self.microsoft_tunnel_configuration)
        writer.write_collection_of_object_values("microsoftTunnelServers", self.microsoft_tunnel_servers)
        writer.write_str_value("publicAddress", self.public_address)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_bool_value("upgradeAutomatically", self.upgrade_automatically)
        writer.write_bool_value("upgradeAvailable", self.upgrade_available)
        writer.write_time_value("upgradeWindowEndTime", self.upgrade_window_end_time)
        writer.write_time_value("upgradeWindowStartTime", self.upgrade_window_start_time)
        writer.write_int_value("upgradeWindowUtcOffsetInMinutes", self.upgrade_window_utc_offset_in_minutes)
    

