from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .action_summary import ActionSummary
    from .authorization_system_identity import AuthorizationSystemIdentity
    from .finding import Finding
    from .permissions_creep_index import PermissionsCreepIndex

from .finding import Finding

@dataclass
class InactiveGroupFinding(Finding, Parsable):
    # The actionSummary property
    action_summary: Optional[ActionSummary] = None
    # The group property
    group: Optional[AuthorizationSystemIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The permissionsCreepIndex property
    permissions_creep_index: Optional[PermissionsCreepIndex] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InactiveGroupFinding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InactiveGroupFinding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InactiveGroupFinding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .action_summary import ActionSummary
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        from .action_summary import ActionSummary
        from .authorization_system_identity import AuthorizationSystemIdentity
        from .finding import Finding
        from .permissions_creep_index import PermissionsCreepIndex

        fields: dict[str, Callable[[Any], None]] = {
            "actionSummary": lambda n : setattr(self, 'action_summary', n.get_object_value(ActionSummary)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(AuthorizationSystemIdentity)),
            "permissionsCreepIndex": lambda n : setattr(self, 'permissions_creep_index', n.get_object_value(PermissionsCreepIndex)),
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
        writer.write_object_value("actionSummary", self.action_summary)
        writer.write_object_value("group", self.group)
        writer.write_object_value("permissionsCreepIndex", self.permissions_creep_index)
    

