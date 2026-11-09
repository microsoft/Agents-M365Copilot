from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_timeout_behavior import AccessReviewTimeoutBehavior
    from .user_set import UserSet

@dataclass
class AssignmentReviewSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The default decision to apply if the request isn't reviewed within the period specified in durationInDays. The possible values are: acceptAccessRecommendation, keepAccess, removeAccess, and unknownFutureValue.
    access_review_timeout_behavior: Optional[AccessReviewTimeoutBehavior] = None
    # The number of days within which reviewers should provide input.
    duration_in_days: Optional[int] = None
    # Specifies whether to display recommendations to the reviewer. The default value is true
    is_access_recommendation_enabled: Optional[bool] = None
    # The isAgenticExperienceEnabled property
    is_agentic_experience_enabled: Optional[bool] = None
    # Specifies whether the reviewer must provide justification for the approval. The default value is true.
    is_approval_justification_required: Optional[bool] = None
    # If true, access reviews are required for assignments from this policy.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The interval for recurrence, such as monthly or quarterly.
    recurrence_type: Optional[str] = None
    # Who should be asked to do the review, either Self, Reviewers or Manager.
    reviewer_type: Optional[str] = None
    # If the reviewerType is Reviewers, this collection specifies the users who will be reviewers, either by ID or as members of a group, using a collection of singleUser and groupMembers.
    reviewers: Optional[list[UserSet]] = None
    # When the first review should start.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentReviewSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentReviewSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_timeout_behavior import AccessReviewTimeoutBehavior
        from .user_set import UserSet

        from .access_review_timeout_behavior import AccessReviewTimeoutBehavior
        from .user_set import UserSet

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviewTimeoutBehavior": lambda n : setattr(self, 'access_review_timeout_behavior', n.get_enum_value(AccessReviewTimeoutBehavior)),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "isAccessRecommendationEnabled": lambda n : setattr(self, 'is_access_recommendation_enabled', n.get_bool_value()),
            "isAgenticExperienceEnabled": lambda n : setattr(self, 'is_agentic_experience_enabled', n.get_bool_value()),
            "isApprovalJustificationRequired": lambda n : setattr(self, 'is_approval_justification_required', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrenceType": lambda n : setattr(self, 'recurrence_type', n.get_str_value()),
            "reviewerType": lambda n : setattr(self, 'reviewer_type', n.get_str_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(UserSet)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("accessReviewTimeoutBehavior", self.access_review_timeout_behavior)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_bool_value("isAccessRecommendationEnabled", self.is_access_recommendation_enabled)
        writer.write_bool_value("isAgenticExperienceEnabled", self.is_agentic_experience_enabled)
        writer.write_bool_value("isApprovalJustificationRequired", self.is_approval_justification_required)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recurrenceType", self.recurrence_type)
        writer.write_str_value("reviewerType", self.reviewer_type)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

