from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_policy_reference import LifecyclePolicyReference
    from .lifecycle_policy_relationship import LifecyclePolicyRelationship
    from .lifecycle_policy_subject_compliance import LifecyclePolicySubjectCompliance
    from .lifecycle_policy_subject_enforcement import LifecyclePolicySubjectEnforcement
    from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

from ..entity import Entity

@dataclass
class LifecyclePolicySubjectReport(Entity, Parsable):
    # The compliance property
    compliance: Optional[LifecyclePolicySubjectCompliance] = None
    # A reference to the effective lifecycle policy for the subject.
    effective_policy: Optional[LifecyclePolicyReference] = None
    # The enforcement property
    enforcement: Optional[LifecyclePolicySubjectEnforcement] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relationship property
    relationship: Optional[LifecyclePolicyRelationship] = None
    # The subject property
    subject: Optional[LifecyclePolicySubjectReference] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicySubjectReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicySubjectReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicySubjectReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_policy_reference import LifecyclePolicyReference
        from .lifecycle_policy_relationship import LifecyclePolicyRelationship
        from .lifecycle_policy_subject_compliance import LifecyclePolicySubjectCompliance
        from .lifecycle_policy_subject_enforcement import LifecyclePolicySubjectEnforcement
        from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

        from ..entity import Entity
        from .lifecycle_policy_reference import LifecyclePolicyReference
        from .lifecycle_policy_relationship import LifecyclePolicyRelationship
        from .lifecycle_policy_subject_compliance import LifecyclePolicySubjectCompliance
        from .lifecycle_policy_subject_enforcement import LifecyclePolicySubjectEnforcement
        from .lifecycle_policy_subject_reference import LifecyclePolicySubjectReference

        fields: dict[str, Callable[[Any], None]] = {
            "compliance": lambda n : setattr(self, 'compliance', n.get_object_value(LifecyclePolicySubjectCompliance)),
            "effectivePolicy": lambda n : setattr(self, 'effective_policy', n.get_object_value(LifecyclePolicyReference)),
            "enforcement": lambda n : setattr(self, 'enforcement', n.get_object_value(LifecyclePolicySubjectEnforcement)),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(LifecyclePolicyRelationship)),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(LifecyclePolicySubjectReference)),
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
        writer.write_object_value("compliance", self.compliance)
        writer.write_object_value("effectivePolicy", self.effective_policy)
        writer.write_object_value("enforcement", self.enforcement)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_object_value("subject", self.subject)
    

