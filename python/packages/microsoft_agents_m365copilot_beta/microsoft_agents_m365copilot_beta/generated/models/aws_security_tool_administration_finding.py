from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .aws_security_tool_web_services import AwsSecurityToolWebServices
    from .finding import Finding
    from .identity_details import IdentityDetails
    from .permissions_creep_index import PermissionsCreepIndex
    from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
    from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
    from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
    from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

from .finding import Finding

@dataclass
class AwsSecurityToolAdministrationFinding(Finding, Parsable):
    # The identity property
    identity: Optional[AuthorizationSystemIdentity] = None
    # The identityDetails property
    identity_details: Optional[IdentityDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    # The securityTools property
    security_tools: Optional[AwsSecurityToolWebServices] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsSecurityToolAdministrationFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsSecurityToolAdministrationFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsResourceAdministratorFinding".casefold():
            from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding

            return SecurityToolAwsResourceAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsRoleAdministratorFinding".casefold():
            from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding

            return SecurityToolAwsRoleAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsServerlessFunctionAdministratorFinding".casefold():
            from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding

            return SecurityToolAwsServerlessFunctionAdministratorFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityToolAwsUserAdministratorFinding".casefold():
            from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

            return SecurityToolAwsUserAdministratorFinding()
        return AwsSecurityToolAdministrationFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_security_tool_web_services import AwsSecurityToolWebServices
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_security_tool_web_services import AwsSecurityToolWebServices
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .security_tool_aws_resource_administrator_finding import SecurityToolAwsResourceAdministratorFinding
        from .security_tool_aws_role_administrator_finding import SecurityToolAwsRoleAdministratorFinding
        from .security_tool_aws_serverless_function_administrator_finding import SecurityToolAwsServerlessFunctionAdministratorFinding
        from .security_tool_aws_user_administrator_finding import SecurityToolAwsUserAdministratorFinding

        fields: dict[str, Callable[[Any], None]] = {
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(AuthorizationSystemIdentity)),
            "identityDetails": lambda n : setattr(self, 'identity_details', n.get_object_value(IdentityDetails)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
            "securityTools": lambda n : setattr(self, 'security_tools', n.get_collection_of_enum_values(AwsSecurityToolWebServices)),
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
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("identityDetails", self.identity_details)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
        writer.write_enum_value("securityTools", self.security_tools)
    

