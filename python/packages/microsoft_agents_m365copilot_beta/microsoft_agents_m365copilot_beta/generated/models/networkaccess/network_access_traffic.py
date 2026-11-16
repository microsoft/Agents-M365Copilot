from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..device import Device
    from ..user import User
    from .application_snapshot import ApplicationSnapshot
    from .cloud_application_metadata import CloudApplicationMetadata
    from .device_category import DeviceCategory
    from .filtering_policy_action import FilteringPolicyAction
    from .headers import Headers
    from .http_method import HttpMethod
    from .networking_protocol import NetworkingProtocol
    from .network_traffic_operation_status import NetworkTrafficOperationStatus
    from .private_access_details import PrivateAccessDetails
    from .traffic_type import TrafficType
    from .web_category import WebCategory

@dataclass
class NetworkAccessTraffic(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates the action taken based on filtering policies. The possible values are: block, allow, unknownFutureValue, bypass, alert. Use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: bypass , alert.
    action: Optional[FilteringPolicyAction] = None
    # Represents the version of the Global Secure Access (GSA) client agent software. Supports $filter (eq) and $orderby.
    agent_version: Optional[str] = None
    # Destination Application ID accessed in Azure AD during the transaction. Supports $filter (eq) and $orderby.
    application_snapshot: Optional[ApplicationSnapshot] = None
    # Contains metadata about the cloud application involved in the network transaction, such as application name, category, and risk level. Supports $filter (eq) and $orderby.
    cloud_application_metadata: Optional[CloudApplicationMetadata] = None
    # Represents a unique identifier assigned to a connection. Supports $filter (eq) and $orderby.
    connection_id: Optional[str] = None
    # Represents the date and time when a network access traffic log entry was created. Supports $filter (eq) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # Informational error message. For example: 'Threat intelligence detected a transaction and triggered an alert.' or 'The Global Secure Access (GSA) policy blocked the destination and triggered an alert.' Supports $filter (eq) and $orderby.
    description: Optional[str] = None
    # Represents the Fully Qualified Domain Name (FQDN) of the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_f_q_d_n: Optional[str] = None
    # Represents the IP address of the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_ip: Optional[str] = None
    # Represents the network port number on the destination host or server in a network communication. Supports $filter (eq) and $orderby.
    destination_port: Optional[int] = None
    # Represents the URL of the destination in a network communication. Supports $filter (eq) and $orderby.
    destination_url: Optional[str] = None
    # The destination FQDN's Web Category (e.g., Gambling). Supports $filter (eq) and $orderby.
    destination_web_category: Optional[WebCategory] = None
    # Represents the device associated with the network traffic, providing details about the hardware or virtual machine involved in the transaction.
    device: Optional[Device] = None
    # Represents the category classification of a device within a network infrastructure. The possible values are: client, branch, unknownFutureValue. Supports $filter (eq) and $orderby.
    device_category: Optional[DeviceCategory] = None
    # Represents a unique identifier assigned to a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_id: Optional[str] = None
    # Represents the operating system installed on a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_operating_system: Optional[str] = None
    # Represents the version or release number of the operating system installed on a device within a network infrastructure. Supports $filter (eq) and $orderby.
    device_operating_system_version: Optional[str] = None
    # The ID of the Filtering Profile associated with the action performed on traffic. Supports $filter (eq) and $orderby.
    filtering_profile_id: Optional[str] = None
    # The name of the Filtering Profile associated with the action performed on traffic. Supports $filter (eq) and $orderby.
    filtering_profile_name: Optional[str] = None
    # Represents the headers included in a network request or response. Supports $filter (eq) and $orderby.
    headers: Optional[Headers] = None
    # The HTTP method inspected in the intercepted HTTP traffic. Supports $filter (eq) and $orderby.
    http_method: Optional[HttpMethod] = None
    # The process initiating the traffic transaction. Supports $filter (eq) and $orderby.
    initiating_process_name: Optional[str] = None
    # Represents the networking protocol used for communication. The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue. Supports $filter (eq) and $orderby.
    network_protocol: Optional[NetworkingProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indication if traffic was successfully processed. The possible values are: success, failure, unknownFutureValue. Supports $filter (eq) and $orderby.
    operation_status: Optional[NetworkTrafficOperationStatus] = None
    # Represents a unique identifier assigned to a policy. Supports $filter (eq) and $orderby.
    policy_id: Optional[str] = None
    # The name of the filtering policy associated with the action performed on traffic. Supports $filter (eq) and $orderby.
    policy_name: Optional[str] = None
    # Represents a unique identifier assigned to a policy rule. Supports $filter (eq) and $orderby.
    policy_rule_id: Optional[str] = None
    # The name of the rule associated with the action performed on traffic. Supports $filter (eq) and $orderby.
    policy_rule_name: Optional[str] = None
    # The Point-of-Presence processing region of the traffic. Supports $filter (eq) and $orderby.
    pop_processing_region: Optional[str] = None
    # Details about private access traffic. Supports $filter (eq) and $orderby.
    private_access_details: Optional[PrivateAccessDetails] = None
    # Represents the total number of bytes received in a network communication or data transfer. Supports $filter (eq) and $orderby.
    received_bytes: Optional[int] = None
    # The ID from which traffic was sent or received, providing visibility into the origin of the traffic. Supports $filter (eq) and $orderby.
    remote_network_id: Optional[str] = None
    # Tenant ID that owns the resource. Supports $filter (eq) and $orderby.
    resource_tenant_id: Optional[str] = None
    # The HTTP response code inspected in the intercepted HTTP traffic. Supports $filter (eq) and $orderby.
    response_code: Optional[int] = None
    # Represents the total number of bytes sent in a network communication or data transfer. Supports $filter (eq) and $orderby.
    sent_bytes: Optional[int] = None
    # Represents a unique identifier assigned to a session or connection within a network infrastructure. Supports $filter (eq) and $orderby.
    session_id: Optional[str] = None
    # Represents the source IP address in a network communication. Supports $filter (eq) and $orderby.
    source_ip: Optional[str] = None
    # Represents the network port number on the source host or device in a network communication. Supports $filter (eq) and $orderby.
    source_port: Optional[int] = None
    # Represents a unique identifier assigned to a tenant within a network infrastructure. Supports $filter (eq) and $orderby.
    tenant_id: Optional[str] = None
    # The type of threat detected in the traffic. Supports $filter (eq) and $orderby.
    threat_type: Optional[str] = None
    # The trafficType property
    traffic_type: Optional[TrafficType] = None
    # Represents a unique identifier assigned to a specific transaction or operation. Key. Supports $filter (eq) and $orderby.
    transaction_id: Optional[str] = None
    # Represents the transport protocol used for communication. The possible values are: ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII, unknownFutureValue. Supports $filter (eq) and $orderby.
    transport_protocol: Optional[NetworkingProtocol] = None
    # Represents the user associated with the network traffic, providing details about the individual or account initiating the transaction.
    user: Optional[User] = None
    # Represents a unique identifier assigned to a user. Supports $filter (eq) and $orderby.
    user_id: Optional[str] = None
    # Represents the user principal name (UPN) associated with a user. Supports $filter (eq) and $orderby.
    user_principal_name: Optional[str] = None
    # The name of the vendors who detected the threat. Supports $filter (eq) and $orderby.
    vendor_names: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkAccessTraffic:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkAccessTraffic
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkAccessTraffic()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..device import Device
        from ..user import User
        from .application_snapshot import ApplicationSnapshot
        from .cloud_application_metadata import CloudApplicationMetadata
        from .device_category import DeviceCategory
        from .filtering_policy_action import FilteringPolicyAction
        from .headers import Headers
        from .http_method import HttpMethod
        from .networking_protocol import NetworkingProtocol
        from .network_traffic_operation_status import NetworkTrafficOperationStatus
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType
        from .web_category import WebCategory

        from ..device import Device
        from ..user import User
        from .application_snapshot import ApplicationSnapshot
        from .cloud_application_metadata import CloudApplicationMetadata
        from .device_category import DeviceCategory
        from .filtering_policy_action import FilteringPolicyAction
        from .headers import Headers
        from .http_method import HttpMethod
        from .networking_protocol import NetworkingProtocol
        from .network_traffic_operation_status import NetworkTrafficOperationStatus
        from .private_access_details import PrivateAccessDetails
        from .traffic_type import TrafficType
        from .web_category import WebCategory

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(FilteringPolicyAction)),
            "agentVersion": lambda n : setattr(self, 'agent_version', n.get_str_value()),
            "applicationSnapshot": lambda n : setattr(self, 'application_snapshot', n.get_object_value(ApplicationSnapshot)),
            "cloudApplicationMetadata": lambda n : setattr(self, 'cloud_application_metadata', n.get_object_value(CloudApplicationMetadata)),
            "connectionId": lambda n : setattr(self, 'connection_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "destinationFQDN": lambda n : setattr(self, 'destination_f_q_d_n', n.get_str_value()),
            "destinationIp": lambda n : setattr(self, 'destination_ip', n.get_str_value()),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_int_value()),
            "destinationUrl": lambda n : setattr(self, 'destination_url', n.get_str_value()),
            "destinationWebCategory": lambda n : setattr(self, 'destination_web_category', n.get_object_value(WebCategory)),
            "device": lambda n : setattr(self, 'device', n.get_object_value(Device)),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_enum_value(DeviceCategory)),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceOperatingSystem": lambda n : setattr(self, 'device_operating_system', n.get_str_value()),
            "deviceOperatingSystemVersion": lambda n : setattr(self, 'device_operating_system_version', n.get_str_value()),
            "filteringProfileId": lambda n : setattr(self, 'filtering_profile_id', n.get_str_value()),
            "filteringProfileName": lambda n : setattr(self, 'filtering_profile_name', n.get_str_value()),
            "headers": lambda n : setattr(self, 'headers', n.get_object_value(Headers)),
            "httpMethod": lambda n : setattr(self, 'http_method', n.get_enum_value(HttpMethod)),
            "initiatingProcessName": lambda n : setattr(self, 'initiating_process_name', n.get_str_value()),
            "networkProtocol": lambda n : setattr(self, 'network_protocol', n.get_enum_value(NetworkingProtocol)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operationStatus": lambda n : setattr(self, 'operation_status', n.get_enum_value(NetworkTrafficOperationStatus)),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyName": lambda n : setattr(self, 'policy_name', n.get_str_value()),
            "policyRuleId": lambda n : setattr(self, 'policy_rule_id', n.get_str_value()),
            "policyRuleName": lambda n : setattr(self, 'policy_rule_name', n.get_str_value()),
            "popProcessingRegion": lambda n : setattr(self, 'pop_processing_region', n.get_str_value()),
            "privateAccessDetails": lambda n : setattr(self, 'private_access_details', n.get_object_value(PrivateAccessDetails)),
            "receivedBytes": lambda n : setattr(self, 'received_bytes', n.get_int_value()),
            "remoteNetworkId": lambda n : setattr(self, 'remote_network_id', n.get_str_value()),
            "resourceTenantId": lambda n : setattr(self, 'resource_tenant_id', n.get_str_value()),
            "responseCode": lambda n : setattr(self, 'response_code', n.get_int_value()),
            "sentBytes": lambda n : setattr(self, 'sent_bytes', n.get_int_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "sourceIp": lambda n : setattr(self, 'source_ip', n.get_str_value()),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_int_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "threatType": lambda n : setattr(self, 'threat_type', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(TrafficType)),
            "transactionId": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "transportProtocol": lambda n : setattr(self, 'transport_protocol', n.get_enum_value(NetworkingProtocol)),
            "user": lambda n : setattr(self, 'user', n.get_object_value(User)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "vendorNames": lambda n : setattr(self, 'vendor_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("action", self.action)
        writer.write_str_value("agentVersion", self.agent_version)
        writer.write_object_value("applicationSnapshot", self.application_snapshot)
        writer.write_object_value("cloudApplicationMetadata", self.cloud_application_metadata)
        writer.write_str_value("connectionId", self.connection_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("destinationFQDN", self.destination_f_q_d_n)
        writer.write_str_value("destinationIp", self.destination_ip)
        writer.write_int_value("destinationPort", self.destination_port)
        writer.write_str_value("destinationUrl", self.destination_url)
        writer.write_object_value("destinationWebCategory", self.destination_web_category)
        writer.write_object_value("device", self.device)
        writer.write_enum_value("deviceCategory", self.device_category)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceOperatingSystem", self.device_operating_system)
        writer.write_str_value("deviceOperatingSystemVersion", self.device_operating_system_version)
        writer.write_str_value("filteringProfileId", self.filtering_profile_id)
        writer.write_str_value("filteringProfileName", self.filtering_profile_name)
        writer.write_object_value("headers", self.headers)
        writer.write_enum_value("httpMethod", self.http_method)
        writer.write_str_value("initiatingProcessName", self.initiating_process_name)
        writer.write_enum_value("networkProtocol", self.network_protocol)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operationStatus", self.operation_status)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyName", self.policy_name)
        writer.write_str_value("policyRuleId", self.policy_rule_id)
        writer.write_str_value("policyRuleName", self.policy_rule_name)
        writer.write_str_value("popProcessingRegion", self.pop_processing_region)
        writer.write_object_value("privateAccessDetails", self.private_access_details)
        writer.write_int_value("receivedBytes", self.received_bytes)
        writer.write_str_value("remoteNetworkId", self.remote_network_id)
        writer.write_str_value("resourceTenantId", self.resource_tenant_id)
        writer.write_int_value("responseCode", self.response_code)
        writer.write_int_value("sentBytes", self.sent_bytes)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_str_value("sourceIp", self.source_ip)
        writer.write_int_value("sourcePort", self.source_port)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("threatType", self.threat_type)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_str_value("transactionId", self.transaction_id)
        writer.write_enum_value("transportProtocol", self.transport_protocol)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_primitive_values("vendorNames", self.vendor_names)
        writer.write_additional_data_value(self.additional_data)
    

