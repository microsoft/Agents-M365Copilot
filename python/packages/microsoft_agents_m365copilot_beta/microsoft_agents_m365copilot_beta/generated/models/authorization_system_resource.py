from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system import AuthorizationSystem
    from .aws_authorization_system_resource import AwsAuthorizationSystemResource
    from .azure_authorization_system_resource import AzureAuthorizationSystemResource
    from .entity import Entity
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

from .entity import Entity

@dataclass
class AuthorizationSystemResource(Entity, Parsable):
    # The authorization system that the resource exists in.
    authorization_system: Optional[AuthorizationSystem] = None
    # The name of the resource. Read-only. Supports $filter (eq,contains).
    display_name: Optional[str] = None
    # The ID of the resource as defined by the authorization system provider. Read-only. Supports $filter (eq).
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the resource. Read-only. Supports $filter (eq).
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizationSystemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystemResource".casefold():
            from .aws_authorization_system_resource import AwsAuthorizationSystemResource

            return AwsAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystemResource".casefold():
            from .azure_authorization_system_resource import AzureAuthorizationSystemResource

            return AzureAuthorizationSystemResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystemResource".casefold():
            from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

            return GcpAuthorizationSystemResource()
        return AuthorizationSystemResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system import AuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .entity import Entity
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

        from .authorization_system import AuthorizationSystem
        from .aws_authorization_system_resource import AwsAuthorizationSystemResource
        from .azure_authorization_system_resource import AzureAuthorizationSystemResource
        from .entity import Entity
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource

        fields: dict[str, Callable[[Any], None]] = {
            "authorizationSystem": lambda n : setattr(self, 'authorization_system', n.get_object_value(AuthorizationSystem)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_str_value("resourceType", self.resource_type)
    

