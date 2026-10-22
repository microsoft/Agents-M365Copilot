from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
    from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

from .aws_permissions_definition_action import AwsPermissionsDefinitionAction

@dataclass
class AwsPolicyPermissionsDefinitionAction(AwsPermissionsDefinitionAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsPolicyPermissionsDefinitionAction"
    # ID for the role.
    assign_to_role_id: Optional[str] = None
    # The policies property
    policies: Optional[list[PermissionsDefinitionAwsPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsPolicyPermissionsDefinitionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsPolicyPermissionsDefinitionAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsPolicyPermissionsDefinitionAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .permissions_definition_aws_policy import PermissionsDefinitionAwsPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "assignToRoleId": lambda n : setattr(self, 'assign_to_role_id', n.get_str_value()),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(PermissionsDefinitionAwsPolicy)),
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
        writer.write_str_value("assignToRoleId", self.assign_to_role_id)
        writer.write_collection_of_object_values("policies", self.policies)
    

