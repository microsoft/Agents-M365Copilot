from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
    from .service_principal import ServicePrincipal

from .service_principal import ServicePrincipal

@dataclass
class AgentIdentityBlueprintPrincipal(ServicePrincipal, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.agentIdentityBlueprintPrincipal"
    # The lifecyclePolicyComplianceState property
    lifecycle_policy_compliance_state: Optional[LifecyclePolicyComplianceState] = None
    # The lifecyclePolicyComplianceStateLastModifiedDateTime property
    lifecycle_policy_compliance_state_last_modified_date_time: Optional[datetime.datetime] = None
    # The lifecyclePolicyComplianceStateReason property
    lifecycle_policy_compliance_state_reason: Optional[str] = None
    # The lifecyclePolicyNonComplianceDisablementDateTime property
    lifecycle_policy_non_compliance_disablement_date_time: Optional[datetime.datetime] = None
    # The collection of application IDs designated as managers of this agent identity blueprint principal's backing agentIdentityBlueprint. Read-only; the value is server-managed and reflects the managerApplications of the backing agentIdentityBlueprint. To change the managers, an owner or administrator must update the managerApplications property on the backing agentIdentityBlueprint in the tenant where it's registered. For multitenant agent identity blueprints, admins in a tenant where the blueprint is only consumed can't make this change — they must ask an owner or administrator in the blueprint's home tenant. Not nullable. Returned only on $select.
    manager_applications: Optional[list[UUID]] = None
    # The sponsors for this agent identity blueprint principal. Sponsors are users or service principals who can authorize and manage the lifecycle of agent identity instances.
    sponsors: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AgentIdentityBlueprintPrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgentIdentityBlueprintPrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AgentIdentityBlueprintPrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
        from .service_principal import ServicePrincipal

        from .directory_object import DirectoryObject
        from .lifecycle_policy_compliance_state import LifecyclePolicyComplianceState
        from .service_principal import ServicePrincipal

        fields: dict[str, Callable[[Any], None]] = {
            "lifecyclePolicyComplianceState": lambda n : setattr(self, 'lifecycle_policy_compliance_state', n.get_enum_value(LifecyclePolicyComplianceState)),
            "lifecyclePolicyComplianceStateLastModifiedDateTime": lambda n : setattr(self, 'lifecycle_policy_compliance_state_last_modified_date_time', n.get_datetime_value()),
            "lifecyclePolicyComplianceStateReason": lambda n : setattr(self, 'lifecycle_policy_compliance_state_reason', n.get_str_value()),
            "lifecyclePolicyNonComplianceDisablementDateTime": lambda n : setattr(self, 'lifecycle_policy_non_compliance_disablement_date_time', n.get_datetime_value()),
            "managerApplications": lambda n : setattr(self, 'manager_applications', n.get_collection_of_primitive_values(UUID)),
            "sponsors": lambda n : setattr(self, 'sponsors', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_enum_value("lifecyclePolicyComplianceState", self.lifecycle_policy_compliance_state)
        writer.write_datetime_value("lifecyclePolicyComplianceStateLastModifiedDateTime", self.lifecycle_policy_compliance_state_last_modified_date_time)
        writer.write_str_value("lifecyclePolicyComplianceStateReason", self.lifecycle_policy_compliance_state_reason)
        writer.write_datetime_value("lifecyclePolicyNonComplianceDisablementDateTime", self.lifecycle_policy_non_compliance_disablement_date_time)
        writer.write_collection_of_object_values("sponsors", self.sponsors)
    

