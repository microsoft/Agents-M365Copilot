from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_decision import AccessReviewDecision
    from .access_review_reviewer import AccessReviewReviewer
    from .access_review_settings import AccessReviewSettings
    from .entity import Entity
    from .identity import Identity
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class AccessReview(Entity, Parsable):
    # The business flow template identifier. Required on create. This value is case sensitive.
    business_flow_template_id: Optional[str] = None
    # The user who created this review.
    created_by: Optional[UserIdentity] = None
    # The collection of decisions for this access review.
    decisions: Optional[list[AccessReviewDecision]] = None
    # The description provided by the access review creator, to show to the reviewers.
    description: Optional[str] = None
    # The access review name. Required on create.
    display_name: Optional[str] = None
    # The DateTime when the review is scheduled to end. This must be at least one day later than the start date. Required on create.
    end_date_time: Optional[datetime.datetime] = None
    # The collection of access reviews instances past, present, and future, if this object is a recurring access review.
    instances: Optional[list[AccessReview]] = None
    # The collection of decisions for the caller, if the caller is a reviewer.
    my_decisions: Optional[list[AccessReviewDecision]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The object for which the access review is reviewing the access rights assignments. This identity can be the group for the review of memberships of users in a group, or the app for a review of assignments of users to an application. Required on create.
    reviewed_entity: Optional[Identity] = None
    # The relationship type of reviewer to the target object, one of: self, delegated, entityOwners. Required on create.
    reviewer_type: Optional[str] = None
    # The collection of reviewers for an access review, if access review reviewerType is of type delegated.
    reviewers: Optional[list[AccessReviewReviewer]] = None
    # The settings of an accessReview, see type definition below.
    settings: Optional[AccessReviewSettings] = None
    # The date and time when the review is scheduled to be start. This date can be in the future.  Required on create.
    start_date_time: Optional[datetime.datetime] = None
    # This read-only field specifies the status of an accessReview. The typical states include Initializing, NotStarted, Starting,InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_decision import AccessReviewDecision
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_settings import AccessReviewSettings
        from .entity import Entity
        from .identity import Identity
        from .user_identity import UserIdentity

        from .access_review_decision import AccessReviewDecision
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_settings import AccessReviewSettings
        from .entity import Entity
        from .identity import Identity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "businessFlowTemplateId": lambda n : setattr(self, 'business_flow_template_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(AccessReviewDecision)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(AccessReview)),
            "myDecisions": lambda n : setattr(self, 'my_decisions', n.get_collection_of_object_values(AccessReviewDecision)),
            "reviewedEntity": lambda n : setattr(self, 'reviewed_entity', n.get_object_value(Identity)),
            "reviewerType": lambda n : setattr(self, 'reviewer_type', n.get_str_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(AccessReviewReviewer)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AccessReviewSettings)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("businessFlowTemplateId", self.business_flow_template_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_collection_of_object_values("myDecisions", self.my_decisions)
        writer.write_object_value("reviewedEntity", self.reviewed_entity)
        writer.write_str_value("reviewerType", self.reviewer_type)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("settings", self.settings)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    

