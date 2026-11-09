from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_policy_scope_processing import LifecyclePolicyScopeProcessing
    from .lifecycle_policy_subject_report import LifecyclePolicySubjectReport

from ..entity import Entity

@dataclass
class LifecyclePolicyReport(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The version of the lifecycle policy represented by the report.
    policy_version: Optional[int] = None
    # The scopeProcessing property
    scope_processing: Optional[LifecyclePolicyScopeProcessing] = None
    # The processing results for subjects included in the report.
    subjects: Optional[list[LifecyclePolicySubjectReport]] = None
    # The number of subjects currently in scope for the policy.
    subjects_in_scope_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecyclePolicyReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecyclePolicyReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecyclePolicyReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_policy_scope_processing import LifecyclePolicyScopeProcessing
        from .lifecycle_policy_subject_report import LifecyclePolicySubjectReport

        from ..entity import Entity
        from .lifecycle_policy_scope_processing import LifecyclePolicyScopeProcessing
        from .lifecycle_policy_subject_report import LifecyclePolicySubjectReport

        fields: dict[str, Callable[[Any], None]] = {
            "policyVersion": lambda n : setattr(self, 'policy_version', n.get_int_value()),
            "scopeProcessing": lambda n : setattr(self, 'scope_processing', n.get_object_value(LifecyclePolicyScopeProcessing)),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_object_values(LifecyclePolicySubjectReport)),
            "subjectsInScopeCount": lambda n : setattr(self, 'subjects_in_scope_count', n.get_int_value()),
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
        writer.write_int_value("policyVersion", self.policy_version)
        writer.write_object_value("scopeProcessing", self.scope_processing)
        writer.write_collection_of_object_values("subjects", self.subjects)
        writer.write_int_value("subjectsInScopeCount", self.subjects_in_scope_count)
    

