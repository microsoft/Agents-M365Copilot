from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
    from .permissions_definition import PermissionsDefinition

from .permissions_definition import PermissionsDefinition

@dataclass
class AwsPermissionsDefinition(PermissionsDefinition, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsPermissionsDefinition"
    # The actionInfo property
    action_info: Optional[AwsPermissionsDefinitionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsPermissionsDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsPermissionsDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsPermissionsDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .permissions_definition import PermissionsDefinition

        from .aws_permissions_definition_action import AwsPermissionsDefinitionAction
        from .permissions_definition import PermissionsDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "actionInfo": lambda n : setattr(self, 'action_info', n.get_object_value(AwsPermissionsDefinitionAction)),
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
        writer.write_object_value("actionInfo", self.action_info)
    

