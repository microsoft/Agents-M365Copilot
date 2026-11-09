from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential
    from .cloud_pc_domain_join_key_vault_intent_configuration import CloudPcDomainJoinKeyVaultIntentConfiguration

from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential

@dataclass
class CloudPcKeyVaultDomainJoinCredential(CloudPcDomainJoinCredential, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcKeyVaultDomainJoinCredential"
    # The keyVaultIntentConfiguration property
    key_vault_intent_configuration: Optional[CloudPcDomainJoinKeyVaultIntentConfiguration] = None
    # The full Azure Resource Manager resource ID of the Azure Key Vault that stores the domain join password. Required format: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}. Required.
    key_vault_resource_id: Optional[str] = None
    # The name of the secret in the Azure Key Vault that stores the domain join password. Required.
    secret_name: Optional[str] = None
    # The full Azure Resource Manager resource ID of the Windows 365 service connector that grants Windows 365 access to the Azure Key Vault. Required format when specified: /subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Windows365/serviceConnectors/{serviceConnectorName}. Optional.
    service_connector_resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcKeyVaultDomainJoinCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcKeyVaultDomainJoinCredential
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcKeyVaultDomainJoinCredential()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential
        from .cloud_pc_domain_join_key_vault_intent_configuration import CloudPcDomainJoinKeyVaultIntentConfiguration

        from .cloud_pc_domain_join_credential import CloudPcDomainJoinCredential
        from .cloud_pc_domain_join_key_vault_intent_configuration import CloudPcDomainJoinKeyVaultIntentConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "keyVaultIntentConfiguration": lambda n : setattr(self, 'key_vault_intent_configuration', n.get_object_value(CloudPcDomainJoinKeyVaultIntentConfiguration)),
            "keyVaultResourceId": lambda n : setattr(self, 'key_vault_resource_id', n.get_str_value()),
            "secretName": lambda n : setattr(self, 'secret_name', n.get_str_value()),
            "serviceConnectorResourceId": lambda n : setattr(self, 'service_connector_resource_id', n.get_str_value()),
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
        writer.write_object_value("keyVaultIntentConfiguration", self.key_vault_intent_configuration)
        writer.write_str_value("keyVaultResourceId", self.key_vault_resource_id)
        writer.write_str_value("secretName", self.secret_name)
        writer.write_str_value("serviceConnectorResourceId", self.service_connector_resource_id)
    

