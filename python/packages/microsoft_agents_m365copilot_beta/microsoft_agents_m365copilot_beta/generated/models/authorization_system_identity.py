from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .authorization_system_identity_source import AuthorizationSystemIdentitySource
    from .aws_access_key import AwsAccessKey
    from .aws_ec2_instance import AwsEc2Instance
    from .aws_group import AwsGroup
    from .aws_identity import AwsIdentity
    from .aws_lambda import AwsLambda
    from .aws_role import AwsRole
    from .aws_user import AwsUser
    from .azure_group import AzureGroup
    from .azure_identity import AzureIdentity
    from .azure_managed_identity import AzureManagedIdentity
    from .azure_serverless_function import AzureServerlessFunction
    from .azure_service_principal import AzureServicePrincipal
    from .azure_user import AzureUser
    from .entity import Entity
    from .gcp_cloud_function import GcpCloudFunction
    from .gcp_group import GcpGroup
    from .gcp_identity import GcpIdentity
    from .gcp_service_account import GcpServiceAccount
    from .gcp_user import GcpUser

from .entity import Entity

@dataclass
class AuthorizationSystemIdentity(Entity, Parsable):
    # Navigation to the authorizationSystem object
    authorization_system: Optional[AuthorizationSystem] = None
    # The name of the identity. Read-only. Supports $filter and (eq,contains).
    display_name: Optional[str] = None
    # Unique ID of the identity within the external system. Read-only.
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents details of the source of the identity.
    source: Optional[AuthorizationSystemIdentitySource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizationSystemIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAccessKey".casefold():
            from .aws_access_key import AwsAccessKey

            return AwsAccessKey()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsEc2Instance".casefold():
            from .aws_ec2_instance import AwsEc2Instance

            return AwsEc2Instance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsGroup".casefold():
            from .aws_group import AwsGroup

            return AwsGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsIdentity".casefold():
            from .aws_identity import AwsIdentity

            return AwsIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsLambda".casefold():
            from .aws_lambda import AwsLambda

            return AwsLambda()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsRole".casefold():
            from .aws_role import AwsRole

            return AwsRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsUser".casefold():
            from .aws_user import AwsUser

            return AwsUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureGroup".casefold():
            from .azure_group import AzureGroup

            return AzureGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureIdentity".casefold():
            from .azure_identity import AzureIdentity

            return AzureIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureManagedIdentity".casefold():
            from .azure_managed_identity import AzureManagedIdentity

            return AzureManagedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServerlessFunction".casefold():
            from .azure_serverless_function import AzureServerlessFunction

            return AzureServerlessFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureServicePrincipal".casefold():
            from .azure_service_principal import AzureServicePrincipal

            return AzureServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureUser".casefold():
            from .azure_user import AzureUser

            return AzureUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpCloudFunction".casefold():
            from .gcp_cloud_function import GcpCloudFunction

            return GcpCloudFunction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpGroup".casefold():
            from .gcp_group import GcpGroup

            return GcpGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpIdentity".casefold():
            from .gcp_identity import GcpIdentity

            return GcpIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpServiceAccount".casefold():
            from .gcp_service_account import GcpServiceAccount

            return GcpServiceAccount()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpUser".casefold():
            from .gcp_user import GcpUser

            return GcpUser()
        return AuthorizationSystemIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .authorization_system_identity_source import AuthorizationSystemIdentitySource
        from .aws_access_key import AwsAccessKey
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_group import AwsGroup
        from .aws_identity import AwsIdentity
        from .aws_lambda import AwsLambda
        from .aws_role import AwsRole
        from .aws_user import AwsUser
        from .azure_group import AzureGroup
        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser
        from .entity import Entity
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_identity import GcpIdentity
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        from .authorization_system import AuthorizationSystem
        from .authorization_system_identity_source import AuthorizationSystemIdentitySource
        from .aws_access_key import AwsAccessKey
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_group import AwsGroup
        from .aws_identity import AwsIdentity
        from .aws_lambda import AwsLambda
        from .aws_role import AwsRole
        from .aws_user import AwsUser
        from .azure_group import AzureGroup
        from .azure_identity import AzureIdentity
        from .azure_managed_identity import AzureManagedIdentity
        from .azure_serverless_function import AzureServerlessFunction
        from .azure_service_principal import AzureServicePrincipal
        from .azure_user import AzureUser
        from .entity import Entity
        from .gcp_cloud_function import GcpCloudFunction
        from .gcp_group import GcpGroup
        from .gcp_identity import GcpIdentity
        from .gcp_service_account import GcpServiceAccount
        from .gcp_user import GcpUser

        fields: dict[str, Callable[[Any], None]] = {
            "authorizationSystem": lambda n : setattr(self, 'authorization_system', n.get_object_value(AuthorizationSystem)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(AuthorizationSystemIdentitySource)),
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
        writer.write_object_value("authorizationSystem", self.authorization_system)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("source", self.source)
    

