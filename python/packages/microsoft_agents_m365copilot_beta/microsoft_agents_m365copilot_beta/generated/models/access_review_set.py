from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_history_definition import AccessReviewHistoryDefinition
    from .access_review_instance import AccessReviewInstance
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_policy import AccessReviewPolicy
    from .access_review_schedule_definition import AccessReviewScheduleDefinition
    from .entity import Entity
    from .unified_root import UnifiedRoot

from .entity import Entity

@dataclass
class AccessReviewSet(Entity, Parsable):
    # Represents a Microsoft Entra access review decision on an instance of a review.
    decisions: Optional[list[AccessReviewInstanceDecisionItem]] = None
    # Represents the template and scheduling for an access review.
    definitions: Optional[list[AccessReviewScheduleDefinition]] = None
    # Represents a collection of access review history data and the scopes used to collect that data.
    history_definitions: Optional[list[AccessReviewHistoryDefinition]] = None
    # Represents the instance of a review.
    instances: Optional[list[AccessReviewInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource that enables administrators to manage directory-level access review policies in their tenant.
    policy: Optional[AccessReviewPolicy] = None
    # Entry point for the unified (vNext) access reviews API surface. Requests under this path are routed to the vNext service through the dedicated accessReviews/unified path segment.
    unified: Optional[UnifiedRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_policy import AccessReviewPolicy
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .entity import Entity
        from .unified_root import UnifiedRoot

        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_policy import AccessReviewPolicy
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .entity import Entity
        from .unified_root import UnifiedRoot

        fields: dict[str, Callable[[Any], None]] = {
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(AccessReviewInstanceDecisionItem)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(AccessReviewScheduleDefinition)),
            "historyDefinitions": lambda n : setattr(self, 'history_definitions', n.get_collection_of_object_values(AccessReviewHistoryDefinition)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(AccessReviewInstance)),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(AccessReviewPolicy)),
            "unified": lambda n : setattr(self, 'unified', n.get_object_value(UnifiedRoot)),
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
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_collection_of_object_values("historyDefinitions", self.history_definitions)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_object_value("policy", self.policy)
        writer.write_object_value("unified", self.unified)
    

