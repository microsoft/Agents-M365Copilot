from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_base import PolicyBase
    from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

from .policy_base import PolicyBase

@dataclass
class ServicePrincipalCreationPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.servicePrincipalCreationPolicy"
    # The excludes property
    excludes: Optional[list[ServicePrincipalCreationConditionSet]] = None
    # The includes property
    includes: Optional[list[ServicePrincipalCreationConditionSet]] = None
    # The isBuiltIn property
    is_built_in: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalCreationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalCreationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalCreationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_base import PolicyBase
        from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

        from .policy_base import PolicyBase
        from .service_principal_creation_condition_set import ServicePrincipalCreationConditionSet

        fields: dict[str, Callable[[Any], None]] = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(ServicePrincipalCreationConditionSet)),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(ServicePrincipalCreationConditionSet)),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
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
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_collection_of_object_values("includes", self.includes)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
    

