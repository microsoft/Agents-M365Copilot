from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .app_category import AppCategory
    from .discovered_cloud_app_info import DiscoveredCloudAppInfo
    from .discovered_cloud_app_i_p_address import DiscoveredCloudAppIPAddress
    from .discovered_cloud_app_user import DiscoveredCloudAppUser
    from .endpoint_discovered_cloud_app_detail import EndpointDiscoveredCloudAppDetail

from ..entity import Entity

@dataclass
class DiscoveredCloudAppDetail(Entity, Parsable):
    # The application information.
    app_info: Optional[DiscoveredCloudAppInfo] = None
    # The category property
    category: Optional[AppCategory] = None
    # The description property
    description: Optional[str] = None
    # The app name.
    display_name: Optional[str] = None
    # The domain.
    domains: Optional[list[str]] = None
    # The download traffic size.
    download_network_traffic_in_bytes: Optional[int] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The IP address.
    ip_address_count: Optional[int] = None
    # The list of IP addresses accessed by the app.
    ip_addresses: Optional[list[DiscoveredCloudAppIPAddress]] = None
    # The last seen date of the discovered app. The Timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The risk score of the app.
    risk_score: Optional[int] = None
    # The tags applied to an app. Possible values include Unsanctioned, Sanctioned, Monitored, or a custom value.
    tags: Optional[list[str]] = None
    # The app transaction count.
    transaction_count: Optional[int] = None
    # The app upload traffic size, in bytes.
    upload_network_traffic_in_bytes: Optional[int] = None
    # The count of users who use the app.
    user_count: Optional[int] = None
    # The list of users who access the app.
    users: Optional[list[DiscoveredCloudAppUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DiscoveredCloudAppDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DiscoveredCloudAppDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.endpointDiscoveredCloudAppDetail".casefold():
            from .endpoint_discovered_cloud_app_detail import EndpointDiscoveredCloudAppDetail

            return EndpointDiscoveredCloudAppDetail()
        return DiscoveredCloudAppDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .app_category import AppCategory
        from .discovered_cloud_app_info import DiscoveredCloudAppInfo
        from .discovered_cloud_app_i_p_address import DiscoveredCloudAppIPAddress
        from .discovered_cloud_app_user import DiscoveredCloudAppUser
        from .endpoint_discovered_cloud_app_detail import EndpointDiscoveredCloudAppDetail

        from ..entity import Entity
        from .app_category import AppCategory
        from .discovered_cloud_app_info import DiscoveredCloudAppInfo
        from .discovered_cloud_app_i_p_address import DiscoveredCloudAppIPAddress
        from .discovered_cloud_app_user import DiscoveredCloudAppUser
        from .endpoint_discovered_cloud_app_detail import EndpointDiscoveredCloudAppDetail

        fields: dict[str, Callable[[Any], None]] = {
            "appInfo": lambda n : setattr(self, 'app_info', n.get_object_value(DiscoveredCloudAppInfo)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(AppCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_primitive_values(str)),
            "downloadNetworkTrafficInBytes": lambda n : setattr(self, 'download_network_traffic_in_bytes', n.get_int_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "ipAddressCount": lambda n : setattr(self, 'ip_address_count', n.get_int_value()),
            "ipAddresses": lambda n : setattr(self, 'ip_addresses', n.get_collection_of_object_values(DiscoveredCloudAppIPAddress)),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "transactionCount": lambda n : setattr(self, 'transaction_count', n.get_int_value()),
            "uploadNetworkTrafficInBytes": lambda n : setattr(self, 'upload_network_traffic_in_bytes', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(DiscoveredCloudAppUser)),
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
        writer.write_object_value("appInfo", self.app_info)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("domains", self.domains)
        writer.write_int_value("downloadNetworkTrafficInBytes", self.download_network_traffic_in_bytes)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_int_value("ipAddressCount", self.ip_address_count)
        writer.write_collection_of_object_values("ipAddresses", self.ip_addresses)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_int_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_int_value("transactionCount", self.transaction_count)
        writer.write_int_value("uploadNetworkTrafficInBytes", self.upload_network_traffic_in_bytes)
        writer.write_int_value("userCount", self.user_count)
        writer.write_collection_of_object_values("users", self.users)
    

