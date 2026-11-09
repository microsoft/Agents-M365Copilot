from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .application_snapshot import ApplicationSnapshot
    from .connection_status import ConnectionStatus
    from .cross_tenant_access_type import CrossTenantAccessType
    from .device_category import DeviceCategory
    from .device_join_type import DeviceJoinType
    from .networking_protocol import NetworkingProtocol
    from .private_access_details import PrivateAccessDetails
    from .traffic_type import TrafficType

from ..entity import Entity

@dataclass
class Connection(Entity, Parsable):
    # The version of the client that initiated the connection.
    agent_version: Optional[str] = None
    # appId (or client ID) of the destination Microsoft Entra application.
    application_snapshot: Optional[ApplicationSnapshot] = None
    # The time the connection was created.
    created_date_time: Optional[datetime.datetime] = None
    # Cross tenant access details, for B2B scenarios. The possible values are: none, b2bCollaboration, unknownFutureValue.
    cross_tenant_access_type: Optional[CrossTenantAccessType] = None
    # The destination FQDN of the connection.
    destination_fqdn: Optional[str] = None
    # The destination IP of the connection.
    destination_ip: Optional[str] = None
    # The destination port of the connection.
    destination_port: Optional[int] = None
    # The category of the device. The possible values are: client, branch, unknownFutureValue, remoteNetwork. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: remoteNetwork.
    device_category: Optional[DeviceCategory] = None
    # The DeviceID.
    device_id: Optional[str] = None
    # Device registration type, for BYOD scenarios. The possible values are: none, microsoftEntraJoined, microsoftEntraRegistered, unknownFutureValue.
    device_join_type: Optional[DeviceJoinType] = None
    # The device operating system type.
    device_operating_system: Optional[str] = None
    # The device operating system version.
    device_operating_system_version: Optional[str] = None
    # The time the connection was terminated.
    end_date_time: Optional[datetime.datetime] = None
    # The identifier of the home tenant, for Entra B2B scenarios.
    home_tenant_id: Optional[str] = None
    # The process initiating the traffic connection.
    initiating_process_name: Optional[str] = None
    # When the connection was last updated.
    last_update_date_time: Optional[datetime.datetime] = None
    # The network protocol of the connection. The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue.
    network_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Point-of-Presence processing region of the traffic.
    pop_processing_region: Optional[str] = None
    # Private access details.
    private_access_details: Optional[PrivateAccessDetails] = None
    # Accumulative bytes received.
    received_bytes: Optional[int] = None
    # Accumulative bytes sent.
    sent_bytes: Optional[int] = None
    # The source IP of the connection.
    source_ip: Optional[str] = None
    # The source port of the connection.
    source_port: Optional[int] = None
    # Status of the connection. The possible values are: open, active, closed, unknownFutureValue.
    status: Optional[ConnectionStatus] = None
    # The ID of the tenant where the connection was initiated.
    tenant_id: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # The number of blocked transactions belonging to the connection.
    transaction_block_count: Optional[int] = None
    # The number of transactions belonging to the connection.
    transaction_count: Optional[int] = None
    # The transport protocol of the connection. The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue.
    transport_protocol: Optional[NetworkingProtocol] = None
    # The user ID.
    user_id: Optional[str] = None
    # The principal name of the user.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Connection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Connection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Connection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .application_snapshot import ApplicationSnapshot
        from .connection_status import ConnectionStatus
        from .cross_tenant_access_type import CrossTenantAccessType
        from .device_category import DeviceCategory
        from .device_join_type import DeviceJoinType
        from .networking_protocol import NetworkingProtocol
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType

        from ..entity import Entity
        from .application_snapshot import ApplicationSnapshot
        from .connection_status import ConnectionStatus
        from .cross_tenant_access_type import CrossTenantAccessType
        from .device_category import DeviceCategory
        from .device_join_type import DeviceJoinType
        from .networking_protocol import NetworkingProtocol
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType

        fields: dict[str, Callable[[Any], None]] = {
            "agentVersion": lambda n : setattr(self, 'agent_version', n.get_str_value()),
            "applicationSnapshot": lambda n : setattr(self, 'application_snapshot', n.get_object_value(ApplicationSnapshot)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "crossTenantAccessType": lambda n : setattr(self, 'cross_tenant_access_type', n.get_enum_value(CrossTenantAccessType)),
            "destinationFqdn": lambda n : setattr(self, 'destination_fqdn', n.get_str_value()),
            "destinationIp": lambda n : setattr(self, 'destination_ip', n.get_str_value()),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_int_value()),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_enum_value(DeviceCategory)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceJoinType": lambda n : setattr(self, 'device_join_type', n.get_enum_value(DeviceJoinType)),
            "deviceOperatingSystem": lambda n : setattr(self, 'device_operating_system', n.get_str_value()),
            "deviceOperatingSystemVersion": lambda n : setattr(self, 'device_operating_system_version', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "homeTenantId": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "initiatingProcessName": lambda n : setattr(self, 'initiating_process_name', n.get_str_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_enum_value(NetworkingProtocol)),
            "popProcessingRegion": lambda n : setattr(self, 'pop_processing_region', n.get_str_value()),
            "privateAccessDetails": lambda n : setattr(self, 'private_access_details', n.get_object_value(PrivateAccessDetails)),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "sentBytes": lambda n : setattr(self, 'sent_bytes', n.get_int_value()),
            "sourceIp": lambda n : setattr(self, 'source_ip', n.get_str_value()),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectionStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionBlockCount": lambda n : setattr(self, 'transaction_block_count', n.get_int_value()),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "transportProtocol": lambda n : setattr(self, 'transport_protocol', n.get_enum_value(NetworkingProtocol)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_str_value("agentVersion", self.agent_version)
        writer.write_object_value("applicationSnapshot", self.application_snapshot)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("crossTenantAccessType", self.cross_tenant_access_type)
        writer.write_str_value("destinationFqdn", self.destination_fqdn)
        writer.write_str_value("destinationIp", self.destination_ip)
        writer.write_int_value("destinationPort", self.destination_port)
        writer.write_enum_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_enum_value("deviceJoinType", self.device_join_type)
        writer.write_str_value("deviceOperatingSystem", self.device_operating_system)
        writer.write_str_value("deviceOperatingSystemVersion", self.device_operating_system_version)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("initiatingProcessName", self.initiating_process_name)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_enum_value("networkProtocol", self.network_protocol)
        writer.write_str_value("popProcessingRegion", self.pop_processing_region)
        writer.write_object_value("privateAccessDetails", self.private_access_details)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_int_value("sentBytes", self.sent_bytes)
        writer.write_str_value("sourceIp", self.source_ip)
        writer.write_int_value("sourcePort", self.source_port)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_int_value("transactionBlockCount", self.transaction_block_count)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_enum_value("transportProtocol", self.transport_protocol)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

