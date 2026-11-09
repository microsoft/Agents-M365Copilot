from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
    from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource

from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource

@dataclass
class AwsIdentitySource(PermissionsDefinitionIdentitySource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsIdentitySource"
    # The authorizationSystemInfo property
    authorization_system_info: Optional[PermissionsDefinitionAuthorizationSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AwsIdentitySource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsIdentitySource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AwsIdentitySource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
        from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource

        from .permissions_definition_authorization_system import PermissionsDefinitionAuthorizationSystem
        from .permissions_definition_identity_source import PermissionsDefinitionIdentitySource

        fields: dict[str, Callable[[Any], None]] = {
            "authorizationSystemInfo": lambda n : setattr(self, 'authorization_system_info', n.get_object_value(PermissionsDefinitionAuthorizationSystem)),
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
        writer.write_object_value("authorizationSystemInfo", self.authorization_system_info)
    

