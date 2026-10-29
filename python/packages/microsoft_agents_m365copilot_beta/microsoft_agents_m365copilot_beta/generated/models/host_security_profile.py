from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .logon_user import LogonUser
    from .network_interface import NetworkInterface
    from .security_vendor_information import SecurityVendorInformation

from .entity import Entity

@dataclass
class HostSecurityProfile(Entity, Parsable):
    # The azureSubscriptionId property
    azure_subscription_id: Optional[str] = None
    # The azureTenantId property
    azure_tenant_id: Optional[str] = None
    # The firstSeenDateTime property
    first_seen_date_time: Optional[datetime.datetime] = None
    # The fqdn property
    fqdn: Optional[str] = None
    # The isAzureAdJoined property
    is_azure_ad_joined: Optional[bool] = None
    # The isAzureAdRegistered property
    is_azure_ad_registered: Optional[bool] = None
    # The isHybridAzureDomainJoined property
    is_hybrid_azure_domain_joined: Optional[bool] = None
    # The lastSeenDateTime property
    last_seen_date_time: Optional[datetime.datetime] = None
    # The logonUsers property
    logon_users: Optional[list[LogonUser]] = None
    # The netBiosName property
    net_bios_name: Optional[str] = None
    # The networkInterfaces property
    network_interfaces: Optional[list[NetworkInterface]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The osVersion property
    os_version: Optional[str] = None
    # The parentHost property
    parent_host: Optional[str] = None
    # The relatedHostIds property
    related_host_ids: Optional[list[str]] = None
    # The riskScore property
    risk_score: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The vendorInformation property
    vendor_information: Optional[SecurityVendorInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostSecurityProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostSecurityProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostSecurityProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .logon_user import LogonUser
        from .network_interface import NetworkInterface
        from .security_vendor_information import SecurityVendorInformation

        from .entity import Entity
        from .logon_user import LogonUser
        from .network_interface import NetworkInterface
        from .security_vendor_information import SecurityVendorInformation

        fields: dict[str, Callable[[Any], None]] = {
            "azureSubscriptionId": lambda n : setattr(self, 'azure_subscription_id', n.get_str_value()),
            "azureTenantId": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "firstSeenDateTime": lambda n : setattr(self, 'first_seen_date_time', n.get_datetime_value()),
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "isAzureAdJoined": lambda n : setattr(self, 'is_azure_ad_joined', n.get_bool_value()),
            "isAzureAdRegistered": lambda n : setattr(self, 'is_azure_ad_registered', n.get_bool_value()),
            "isHybridAzureDomainJoined": lambda n : setattr(self, 'is_hybrid_azure_domain_joined', n.get_bool_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "logonUsers": lambda n : setattr(self, 'logon_users', n.get_collection_of_object_values(LogonUser)),
            "netBiosName": lambda n : setattr(self, 'net_bios_name', n.get_str_value()),
            "networkInterfaces": lambda n : setattr(self, 'network_interfaces', n.get_collection_of_object_values(NetworkInterface)),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "parentHost": lambda n : setattr(self, 'parent_host', n.get_str_value()),
            "relatedHostIds": lambda n : setattr(self, 'related_host_ids', n.get_collection_of_primitive_values(str)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "vendorInformation": lambda n : setattr(self, 'vendor_information', n.get_object_value(SecurityVendorInformation)),
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
        writer.write_str_value("azureSubscriptionId", self.azure_subscription_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_datetime_value("firstSeenDateTime", self.first_seen_date_time)
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_bool_value("isAzureAdJoined", self.is_azure_ad_joined)
        writer.write_bool_value("isAzureAdRegistered", self.is_azure_ad_registered)
        writer.write_bool_value("isHybridAzureDomainJoined", self.is_hybrid_azure_domain_joined)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_collection_of_object_values("logonUsers", self.logon_users)
        writer.write_str_value("netBiosName", self.net_bios_name)
        writer.write_collection_of_object_values("networkInterfaces", self.network_interfaces)
        writer.write_str_value("os", self.os)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("parentHost", self.parent_host)
        writer.write_collection_of_primitive_values("relatedHostIds", self.related_host_ids)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_object_value("vendorInformation", self.vendor_information)
    

