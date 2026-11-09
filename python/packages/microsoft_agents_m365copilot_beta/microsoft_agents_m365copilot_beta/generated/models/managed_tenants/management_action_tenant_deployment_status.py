from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .management_action_deployment_status import ManagementActionDeploymentStatus

from ..entity import Entity

@dataclass
class ManagementActionTenantDeploymentStatus(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of deployment status for each instance of a management action. Optional.
    statuses: Optional[list[ManagementActionDeploymentStatus]] = None
    # The identifier for the tenant group that is associated with the management action. Required. Read-only.
    tenant_group_id: Optional[str] = None
    # The Microsoft Entra tenant identifier for the managed tenant. Required. Read-only.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagementActionTenantDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagementActionTenantDeploymentStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagementActionTenantDeploymentStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .management_action_deployment_status import ManagementActionDeploymentStatus

        from ..entity import Entity
        from .management_action_deployment_status import ManagementActionDeploymentStatus

        fields: dict[str, Callable[[Any], None]] = {
            "statuses": lambda n : setattr(self, 'statuses', n.get_collection_of_object_values(ManagementActionDeploymentStatus)),
            "tenantGroupId": lambda n : setattr(self, 'tenant_group_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("statuses", self.statuses)
        writer.write_str_value("tenantGroupId", self.tenant_group_id)
        writer.write_str_value("tenantId", self.tenant_id)
    

