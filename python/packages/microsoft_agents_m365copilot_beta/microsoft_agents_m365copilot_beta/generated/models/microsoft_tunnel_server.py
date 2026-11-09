from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .microsoft_tunnel_deployment_mode import MicrosoftTunnelDeploymentMode
    from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

from .entity import Entity

@dataclass
class MicrosoftTunnelServer(Entity, Parsable):
    """
    Entity that represents a single Microsoft Tunnel server
    """
    # The digest of the current agent image running on this server. Supports: $filter, $select, $top, $skip, $orderby. $search is not supported. Read-only.
    agent_image_digest: Optional[str] = None
    # Microsoft Tunnel server deployment mode. The value is set when the server is registered. Possible values are standaloneRootful, standaloneRootless, podRootful, podRootless. Default value: standaloneRootful. Supports: $filter, $select, $top, $skip, $orderby. $search is not supported. Read-only. Possible values are: standaloneRootful, standaloneRootless, podRootful, podRootless, unknownFutureValue.
    deployment_mode: Optional[MicrosoftTunnelDeploymentMode] = None
    # The display name of the server. It is the same as the host name during registration and can be changed later. Supports: $filter, $select, $top, $skip, $orderby. $search is not supported. Max allowed length is 200 chars.
    display_name: Optional[str] = None
    # Indicates when the server last checked in. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Supports: $filter, $select, $top, $skip, $orderby. $search is not supported Read-only.
    last_checkin_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The digest of the current server image running on this server. Supports: $filter, $select, $top, $skip, $orderby. $search is not supported. Read-only.
    server_image_digest: Optional[str] = None
    # Enum of possible MicrosoftTunnelServer health status types
    tunnel_server_health_status: Optional[MicrosoftTunnelServerHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftTunnelServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftTunnelServer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftTunnelServer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .microsoft_tunnel_deployment_mode import MicrosoftTunnelDeploymentMode
        from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

        from .entity import Entity
        from .microsoft_tunnel_deployment_mode import MicrosoftTunnelDeploymentMode
        from .microsoft_tunnel_server_health_status import MicrosoftTunnelServerHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "agentImageDigest": lambda n : setattr(self, 'agent_image_digest', n.get_str_value()),
            "deploymentMode": lambda n : setattr(self, 'deployment_mode', n.get_enum_value(MicrosoftTunnelDeploymentMode)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastCheckinDateTime": lambda n : setattr(self, 'last_checkin_date_time', n.get_datetime_value()),
            "serverImageDigest": lambda n : setattr(self, 'server_image_digest', n.get_str_value()),
            "tunnelServerHealthStatus": lambda n : setattr(self, 'tunnel_server_health_status', n.get_enum_value(MicrosoftTunnelServerHealthStatus)),
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
        writer.write_str_value("agentImageDigest", self.agent_image_digest)
        writer.write_enum_value("deploymentMode", self.deployment_mode)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastCheckinDateTime", self.last_checkin_date_time)
        writer.write_str_value("serverImageDigest", self.server_image_digest)
        writer.write_enum_value("tunnelServerHealthStatus", self.tunnel_server_health_status)
    

