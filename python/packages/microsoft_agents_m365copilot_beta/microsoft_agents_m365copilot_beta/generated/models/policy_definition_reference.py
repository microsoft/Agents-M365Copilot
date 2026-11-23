from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assigned_policy_reference import AssignedPolicyReference
    from .resource_policy_definition import ResourcePolicyDefinition

from .assigned_policy_reference import AssignedPolicyReference

@dataclass
class PolicyDefinitionReference(AssignedPolicyReference, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.policyDefinitionReference"
    # The policyDefinition property
    policy_definition: Optional[ResourcePolicyDefinition] = None
    # The policyUniqueName property
    policy_unique_name: Optional[str] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyDefinitionReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyDefinitionReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyDefinitionReference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .assigned_policy_reference import AssignedPolicyReference
        from .resource_policy_definition import ResourcePolicyDefinition

        from .assigned_policy_reference import AssignedPolicyReference
        from .resource_policy_definition import ResourcePolicyDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "policyDefinition": lambda n : setattr(self, 'policy_definition', n.get_object_value(ResourcePolicyDefinition)),
            "policyUniqueName": lambda n : setattr(self, 'policy_unique_name', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("policyDefinition", self.policy_definition)
        writer.write_str_value("policyUniqueName", self.policy_unique_name)
        writer.write_str_value("version", self.version)
    

