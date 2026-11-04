from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

@dataclass
class LifecyclePolicyAgentIdentitySubjectReference(LifecyclePolicySubjectReference, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.lifecyclePolicyAgentIdentitySubjectReference"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyAgentIdentitySubjectReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyAgentIdentitySubjectReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyAgentIdentitySubjectReference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

        from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

        fields: dict[str, Callable[[Any], None]] = {
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
    

