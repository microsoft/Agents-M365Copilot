from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .aws_access_key import AwsAccessKey
    from .aws_ec2_instance import AwsEc2Instance
    from .aws_group import AwsGroup
    from .aws_lambda import AwsLambda
    from .aws_role import AwsRole
    from .aws_user import AwsUser

from .authorization_system_identity import AuthorizationSystemIdentity

@dataclass
class AwsIdentity(AuthorizationSystemIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsIdentity"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsIdentity
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsLambda".casefold():
            from .aws_lambda import AwsLambda

            return AwsLambda()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsRole".casefold():
            from .aws_role import AwsRole

            return AwsRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.awsUser".casefold():
            from .aws_user import AwsUser

            return AwsUser()
        return AwsIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_access_key import AwsAccessKey
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_group import AwsGroup
        from .aws_lambda import AwsLambda
        from .aws_role import AwsRole
        from .aws_user import AwsUser

        from .authorization_system_identity import AuthorizationSystemIdentity
        from .aws_access_key import AwsAccessKey
        from .aws_ec2_instance import AwsEc2Instance
        from .aws_group import AwsGroup
        from .aws_lambda import AwsLambda
        from .aws_role import AwsRole
        from .aws_user import AwsUser

        fields: dict[str, Callable[[Any], None]] = {
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
    

