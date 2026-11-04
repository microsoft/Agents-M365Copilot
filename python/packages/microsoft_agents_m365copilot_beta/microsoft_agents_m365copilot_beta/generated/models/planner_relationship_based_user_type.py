from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_relationship_user_roles import PlannerRelationshipUserRoles
    from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase

from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase

@dataclass
class PlannerRelationshipBasedUserType(PlannerTaskConfigurationRoleBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.plannerRelationshipBasedUserType"
    # The role property
    role: Optional[PlannerRelationshipUserRoles] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerRelationshipBasedUserType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerRelationshipBasedUserType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerRelationshipBasedUserType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .planner_relationship_user_roles import PlannerRelationshipUserRoles
        from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase

        from .planner_relationship_user_roles import PlannerRelationshipUserRoles
        from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase

        fields: dict[str, Callable[[Any], None]] = {
            "role": lambda n : setattr(self, 'role', n.get_enum_value(PlannerRelationshipUserRoles)),
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
        writer.write_enum_value("role", self.role)
    

