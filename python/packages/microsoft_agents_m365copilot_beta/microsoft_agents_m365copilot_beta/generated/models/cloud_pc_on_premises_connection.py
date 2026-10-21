from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_management_service import CloudPcManagementService
    from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
    from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
    from .cloud_pc_on_premises_connection_status_details import CloudPcOnPremisesConnectionStatusDetails
    from .cloud_pc_on_premises_connection_subnet_ip_detail import CloudPcOnPremisesConnectionSubnetIpDetail
    from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcOnPremisesConnection(Entity, Parsable):
    # The fully qualified domain name (FQDN) of the Active Directory domain you want to join. Optional.
    ad_domain_name: Optional[str] = None
    # The password associated with adDomainUsername.
    ad_domain_password: Optional[str] = None
    # The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com. Optional.
    ad_domain_username: Optional[str] = None
    # The interface URL of the partner service's resource that links to this Azure network connection. Requires $select to retrieve.
    alternate_resource_url: Optional[str] = None
    # Specifies the method by which a provisioned Cloud PC is joined to Microsoft Entra. The azureADJoin option indicates the absence of an on-premises Active Directory (AD) in the current tenant which results in the Cloud PC device only joining to Microsoft Entra. The hybridAzureADJoin option indicates the presence of an on-premises AD in the current tenant and that the Cloud PC joins both the on-premises AD and Microsoft Entra. The selected option also determines the types of users who can be assigned and can sign into a Cloud PC. The azureADJoin option allows both cloud-only and hybrid users to be assigned and sign in, whereas hybridAzureADJoin is restricted to hybrid users only. The default value is hybridAzureADJoin. The possible values are: hybridAzureADJoin, azureADJoin, unknownFutureValue.
    connection_type: Optional[CloudPcOnPremisesConnectionType] = None
    # The display name for the Azure network connection.
    display_name: Optional[str] = None
    # Indicates whether regular health checks on the network or domain configuration are paused or active. false if the regular health checks on the network or domain configuration are currently active. true if the checks are paused. If you perform a create or update operation on a onPremisesNetworkConnection resource, this value is set to false for four weeks. If you retry a health check on network or domain configuration, this value is set to false for two weeks. If the onPremisesNetworkConnection resource is attached in a provisioningPolicy or used by a Cloud PC in the past four weeks, healthCheckPaused is set to false. Read-only. Default is false.
    health_check_paused: Optional[bool] = None
    # The healthCheckStatus property
    health_check_status: Optional[CloudPcOnPremisesConnectionStatus] = None
    # Indicates the results of health checks performed on the on-premises connection. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
    health_check_status_detail: Optional[CloudPcOnPremisesConnectionStatusDetail] = None
    # The details of the connection's health checks and the corresponding results. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
    health_check_status_details: Optional[CloudPcOnPremisesConnectionStatusDetails] = None
    # When true, the Azure network connection is in use. When false, the connection isn't in use. You can't delete a connection that’s in use. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
    in_use: Optional[bool] = None
    # Indicates whether a Cloud PC is using this on-premises network connection. true if at least one Cloud PC is using it. Otherwise, false. Read-only. Default is false.
    in_use_by_cloud_pc: Optional[bool] = None
    # The managedBy property
    managed_by: Optional[CloudPcManagementService] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizational unit (OU) in which the computer account is created. If left null, the OU configured as the default (a well-known computer object container) in your Active Directory domain (OU) is used. Optional.
    organizational_unit: Optional[str] = None
    # The ID of the target resource group. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}.
    resource_group_id: Optional[str] = None
    # The scope IDs of the corresponding permission. Currently, it's the Intune scope tag ID.
    scope_ids: Optional[list[str]] = None
    # The ID of the target subnet. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkId}/subnets/{subnetName}.
    subnet_id: Optional[str] = None
    # Contains detailed information about the private IP addresses associated with the subnet. Returned only on $select. For an example that shows how to retrieve specific properties using $select, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetails. Read-only.
    subnet_private_ip_detail: Optional[CloudPcOnPremisesConnectionSubnetIpDetail] = None
    # The ID of the target Azure subscription associated with your tenant.
    subscription_id: Optional[str] = None
    # The name of the target Azure subscription. Read-only.
    subscription_name: Optional[str] = None
    # Specifies the method by which a provisioned Cloud PC is joined to Microsoft Entra. The azureADJoin option indicates the absence of an on-premises Active Directory (AD) in the current tenant, which results in the Cloud PC device only joining to Microsoft Entra. The hybridAzureADJoin option indicates the presence of an on-premises AD in the current tenant and that the Cloud PC joins both the on-premises AD and Microsoft Entra. The selected option also determines the types of users who can be assigned and can sign into a Cloud PC. The azureADJoin option allows both cloud-only and hybrid users to be assigned and sign in, whereas hybridAzureADJoin is restricted to hybrid users only. The default value is hybridAzureADJoin. The possible values are: hybridAzureADJoin, azureADJoin, unknownFutureValue. The type property is deprecated and stopped returning data on January 31, 2024. Going forward, use the connectionType property.
    type: Optional[CloudPcOnPremisesConnectionType] = None
    # The ID of the target virtual network. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}.
    virtual_network_id: Optional[str] = None
    # Indicates the resource location of the virtual target network. Read-only, computed value.
    virtual_network_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcOnPremisesConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOnPremisesConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_status_details import CloudPcOnPremisesConnectionStatusDetails
        from .cloud_pc_on_premises_connection_subnet_ip_detail import CloudPcOnPremisesConnectionSubnetIpDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        from .cloud_pc_management_service import CloudPcManagementService
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_status_details import CloudPcOnPremisesConnectionStatusDetails
        from .cloud_pc_on_premises_connection_subnet_ip_detail import CloudPcOnPremisesConnectionSubnetIpDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "adDomainName": lambda n : setattr(self, 'ad_domain_name', n.get_str_value()),
            "adDomainPassword": lambda n : setattr(self, 'ad_domain_password', n.get_str_value()),
            "adDomainUsername": lambda n : setattr(self, 'ad_domain_username', n.get_str_value()),
            "alternateResourceUrl": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(CloudPcOnPremisesConnectionType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "healthCheckPaused": lambda n : setattr(self, 'health_check_paused', n.get_bool_value()),
            "healthCheckStatus": lambda n : setattr(self, 'health_check_status', n.get_enum_value(CloudPcOnPremisesConnectionStatus)),
            "healthCheckStatusDetail": lambda n : setattr(self, 'health_check_status_detail', n.get_object_value(CloudPcOnPremisesConnectionStatusDetail)),
            "healthCheckStatusDetails": lambda n : setattr(self, 'health_check_status_details', n.get_object_value(CloudPcOnPremisesConnectionStatusDetails)),
            "inUse": lambda n : setattr(self, 'in_use', n.get_bool_value()),
            "inUseByCloudPc": lambda n : setattr(self, 'in_use_by_cloud_pc', n.get_bool_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_collection_of_enum_values(CloudPcManagementService)),
            "organizationalUnit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
            "resourceGroupId": lambda n : setattr(self, 'resource_group_id', n.get_str_value()),
            "scopeIds": lambda n : setattr(self, 'scope_ids', n.get_collection_of_primitive_values(str)),
            "subnetId": lambda n : setattr(self, 'subnet_id', n.get_str_value()),
            "subnetPrivateIpDetail": lambda n : setattr(self, 'subnet_private_ip_detail', n.get_object_value(CloudPcOnPremisesConnectionSubnetIpDetail)),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscriptionName": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CloudPcOnPremisesConnectionType)),
            "virtualNetworkId": lambda n : setattr(self, 'virtual_network_id', n.get_str_value()),
            "virtualNetworkLocation": lambda n : setattr(self, 'virtual_network_location', n.get_str_value()),
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
        writer.write_str_value("adDomainName", self.ad_domain_name)
        writer.write_str_value("adDomainPassword", self.ad_domain_password)
        writer.write_str_value("adDomainUsername", self.ad_domain_username)
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("healthCheckPaused", self.health_check_paused)
        writer.write_enum_value("healthCheckStatus", self.health_check_status)
        writer.write_object_value("healthCheckStatusDetail", self.health_check_status_detail)
        writer.write_object_value("healthCheckStatusDetails", self.health_check_status_details)
        writer.write_bool_value("inUse", self.in_use)
        writer.write_bool_value("inUseByCloudPc", self.in_use_by_cloud_pc)
        writer.write_enum_value("managedBy", self.managed_by)
        writer.write_str_value("organizationalUnit", self.organizational_unit)
        writer.write_str_value("resourceGroupId", self.resource_group_id)
        writer.write_collection_of_primitive_values("scopeIds", self.scope_ids)
        writer.write_str_value("subnetId", self.subnet_id)
        writer.write_object_value("subnetPrivateIpDetail", self.subnet_private_ip_detail)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("virtualNetworkId", self.virtual_network_id)
        writer.write_str_value("virtualNetworkLocation", self.virtual_network_location)
    

