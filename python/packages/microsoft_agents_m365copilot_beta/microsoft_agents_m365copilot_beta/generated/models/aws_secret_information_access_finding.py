from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .aws_secret_information_web_services import AwsSecretInformationWebServices
    from .finding import Finding
    from .identity_details import IdentityDetails
    from .permissions_creep_index import PermissionsCreepIndex
    from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
    from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
    from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
    from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

from .finding import Finding

@dataclass
class AwsSecretInformationAccessFinding(Finding, Parsable):
    # The identity property
    identity: Optional[AuthorizationSystemIdentity] = None
    # The identityDetails property
    identity_details: Optional[IdentityDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    # The secretInformationWebServices property
    secret_information_web_services: Optional[AwsSecretInformationWebServices] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsSecretInformationAccessFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsSecretInformationAccessFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsResourceFinding".casefold():
            from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding

            return SecretInformationAccessAwsResourceFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsRoleFinding".casefold():
            from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding

            return SecretInformationAccessAwsRoleFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsServerlessFunctionFinding".casefold():
            from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding

            return SecretInformationAccessAwsServerlessFunctionFinding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secretInformationAccessAwsUserFinding".casefold():
            from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

            return SecretInformationAccessAwsUserFinding()
        return AwsSecretInformationAccessFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_secret_information_web_services import AwsSecretInformationWebServices
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_secret_information_web_services import AwsSecretInformationWebServices
        from .finding import Finding
        from .identity_details import IdentityDetails
        from .permissions_creep_index import PermissionsCreepIndex
        from .secret_information_access_aws_resource_finding import SecretInformationAccessAwsResourceFinding
        from .secret_information_access_aws_role_finding import SecretInformationAccessAwsRoleFinding
        from .secret_information_access_aws_serverless_function_finding import SecretInformationAccessAwsServerlessFunctionFinding
        from .secret_information_access_aws_user_finding import SecretInformationAccessAwsUserFinding

        fields: dict[str, Callable[[Any], None]] = {
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(AuthorizationSystemIdentity)),
            "identityDetails": lambda n : setattr(self, 'identity_details', n.get_object_value(IdentityDetails)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
            "secretInformationWebServices": lambda n : setattr(self, 'secret_information_web_services', n.get_collection_of_enum_values(AwsSecretInformationWebServices)),
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
        writer.write_enum_value("secretInformationWebServices", self.secret_information_web_services)
    

