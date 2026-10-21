from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .relation import Relation

from .relation import Relation

@dataclass
class WorkspaceIndicatorRelation(Relation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.caseManagement.workspaceIndicatorRelation"
    # The Azure resource group name for the workspace.
    resource_group_name: Optional[str] = None
    # The Azure subscription identifier for the workspace.
    subscription_id: Optional[str] = None
    # The Log Analytics workspace name.
    workspace_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkspaceIndicatorRelation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkspaceIndicatorRelation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkspaceIndicatorRelation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .relation import Relation

        from .relation import Relation

        fields: dict[str, Callable[[Any], None]] = {
            "resourceGroupName": lambda n : setattr(self, 'resource_group_name', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "workspaceName": lambda n : setattr(self, 'workspace_name', n.get_str_value()),
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
        writer.write_str_value("resourceGroupName", self.resource_group_name)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("workspaceName", self.workspace_name)
    

