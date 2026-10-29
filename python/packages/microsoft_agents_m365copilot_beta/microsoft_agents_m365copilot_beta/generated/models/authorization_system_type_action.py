from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_action_severity import AuthorizationSystemActionSeverity
    from .authorization_system_action_type import AuthorizationSystemActionType
    from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
    from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
    from .entity import Entity
    from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

from .entity import Entity

@dataclass
class AuthorizationSystemTypeAction(Entity, Parsable):
    # The type of action allowed in the authorization system's service. The possible values are: delete, read, unknownFutureValue. Supports $filter and (eq).
    action_type: Optional[AuthorizationSystemActionType] = None
    # The display name of an action. Read-only. Supports $filter and (eq).
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resource types in the authorization system's service where the action can be performed. Supports $filter and (eq).
    resource_types: Optional[list[str]] = None
    # The severity property
    severity: Optional[AuthorizationSystemActionSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizationSystemTypeAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizationSystemTypeAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsAuthorizationSystemTypeAction".casefold():
            from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction

            return AwsAuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureAuthorizationSystemTypeAction".casefold():
            from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction

            return AzureAuthorizationSystemTypeAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.gcpAuthorizationSystemTypeAction".casefold():
            from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

            return GcpAuthorizationSystemTypeAction()
        return AuthorizationSystemTypeAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_action_severity import AuthorizationSystemActionSeverity
        from .authorization_system_action_type import AuthorizationSystemActionType
        from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
        from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
        from .entity import Entity
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

        from .authorization_system_action_severity import AuthorizationSystemActionSeverity
        from .authorization_system_action_type import AuthorizationSystemActionType
        from .aws_authorization_system_type_action import AwsAuthorizationSystemTypeAction
        from .azure_authorization_system_type_action import AzureAuthorizationSystemTypeAction
        from .entity import Entity
        from .gcp_authorization_system_type_action import GcpAuthorizationSystemTypeAction

        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(AuthorizationSystemActionType)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "resourceTypes": lambda n : setattr(self, 'resource_types', n.get_collection_of_primitive_values(str)),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AuthorizationSystemActionSeverity)),
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
        writer.write_enum_value("actionType", self.action_type)
        writer.write_str_value("externalId", self.external_id)
        writer.write_collection_of_primitive_values("resourceTypes", self.resource_types)
        writer.write_enum_value("severity", self.severity)
    

