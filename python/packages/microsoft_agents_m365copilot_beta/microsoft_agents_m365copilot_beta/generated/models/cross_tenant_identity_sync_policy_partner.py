from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_group_sync_inbound import CrossTenantGroupSyncInbound
    from .cross_tenant_role_enabled_group_sync_inbound import CrossTenantRoleEnabledGroupSyncInbound
    from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
    from .policy_deletable_item import PolicyDeletableItem

from .policy_deletable_item import PolicyDeletableItem

@dataclass
class CrossTenantIdentitySyncPolicyPartner(PolicyDeletableItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.crossTenantIdentitySyncPolicyPartner"
    # Display name for the cross-tenant user and group synchronization policy. Use the name of the partner Microsoft Entra tenant to easily identify the policy. Optional.
    display_name: Optional[str] = None
    # The externalCloudAuthorizedApplicationId property
    external_cloud_authorized_application_id: Optional[str] = None
    # Defines whether groups can be synchronized from a partner tenant.
    group_sync_inbound: Optional[CrossTenantGroupSyncInbound] = None
    # The roleEnabledGroupSyncInbound property
    role_enabled_group_sync_inbound: Optional[CrossTenantRoleEnabledGroupSyncInbound] = None
    # Tenant identifier for the partner Microsoft Entra organization. Key. Read-only.
    tenant_id: Optional[str] = None
    # Defines whether users can be synchronized from the partner tenant.
    user_sync_inbound: Optional[CrossTenantUserSyncInbound] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantIdentitySyncPolicyPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantIdentitySyncPolicyPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantIdentitySyncPolicyPartner()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_group_sync_inbound import CrossTenantGroupSyncInbound
        from .cross_tenant_role_enabled_group_sync_inbound import CrossTenantRoleEnabledGroupSyncInbound
        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
        from .policy_deletable_item import PolicyDeletableItem

        from .cross_tenant_group_sync_inbound import CrossTenantGroupSyncInbound
        from .cross_tenant_role_enabled_group_sync_inbound import CrossTenantRoleEnabledGroupSyncInbound
        from .cross_tenant_user_sync_inbound import CrossTenantUserSyncInbound
        from .policy_deletable_item import PolicyDeletableItem

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalCloudAuthorizedApplicationId": lambda n : setattr(self, 'external_cloud_authorized_application_id', n.get_str_value()),
            "groupSyncInbound": lambda n : setattr(self, 'group_sync_inbound', n.get_object_value(CrossTenantGroupSyncInbound)),
            "roleEnabledGroupSyncInbound": lambda n : setattr(self, 'role_enabled_group_sync_inbound', n.get_object_value(CrossTenantRoleEnabledGroupSyncInbound)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "userSyncInbound": lambda n : setattr(self, 'user_sync_inbound', n.get_object_value(CrossTenantUserSyncInbound)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalCloudAuthorizedApplicationId", self.external_cloud_authorized_application_id)
        writer.write_object_value("groupSyncInbound", self.group_sync_inbound)
        writer.write_object_value("roleEnabledGroupSyncInbound", self.role_enabled_group_sync_inbound)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("userSyncInbound", self.user_sync_inbound)
    

