from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
    from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
    from .entity import Entity

from .entity import Entity

@dataclass
class PolicyDeletableRoot(Entity, Parsable):
    # Represents the partner-specific configuration for cross-tenant access and tenant restrictions. Cross-tenant access settings include inbound and outbound settings of Microsoft Entra B2B collaboration and B2B direct connect.
    cross_tenant_partners: Optional[list[CrossTenantAccessPolicyConfigurationPartner]] = None
    # Defines the cross-tenant policy for synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multi-tenant organization by automating the creation, update, and deletion of users from one tenant to another.
    cross_tenant_sync_policy_partners: Optional[list[CrossTenantIdentitySyncPolicyPartner]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyDeletableRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyDeletableRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyDeletableRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .entity import Entity

        from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
        from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "crossTenantPartners": lambda n : setattr(self, 'cross_tenant_partners', n.get_collection_of_object_values(CrossTenantAccessPolicyConfigurationPartner)),
            "crossTenantSyncPolicyPartners": lambda n : setattr(self, 'cross_tenant_sync_policy_partners', n.get_collection_of_object_values(CrossTenantIdentitySyncPolicyPartner)),
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
        writer.write_collection_of_object_values("crossTenantPartners", self.cross_tenant_partners)
        writer.write_collection_of_object_values("crossTenantSyncPolicyPartners", self.cross_tenant_sync_policy_partners)
    

