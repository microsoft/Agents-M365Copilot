from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .subject_type import SubjectType

from ..entity import Entity

@dataclass
class LifecyclePolicyPriorityConfiguration(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifiers of the lifecycle policies in evaluation priority order. The first policy in the collection has the highest priority. A maximum of 10 policies are allowed per subject type.
    ordered_policy_ids: Optional[list[str]] = None
    # The subjectType property
    subject_type: Optional[SubjectType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyPriorityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyPriorityConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyPriorityConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .subject_type import SubjectType

        from ..entity import Entity
        from .subject_type import SubjectType

        fields: dict[str, Callable[[Any], None]] = {
            "orderedPolicyIds": lambda n : setattr(self, 'ordered_policy_ids', n.get_collection_of_primitive_values(str)),
            "subjectType": lambda n : setattr(self, 'subject_type', n.get_collection_of_enum_values(SubjectType)),
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
        writer.write_collection_of_primitive_values("orderedPolicyIds", self.ordered_policy_ids)
        writer.write_enum_value("subjectType", self.subject_type)
    

