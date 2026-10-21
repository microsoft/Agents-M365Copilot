from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class AccessReviewDecision(Entity, Parsable):
    # The feature- generated recommendation shown to the reviewer, one of: Approve, Deny, NotAvailable.
    access_recommendation: Optional[str] = None
    # The feature-generated ID of the access review.
    access_review_id: Optional[str] = None
    # When the review completes, if the results were manually applied, the user identity of the user who applied the decision. If the review was autoapplied, the userPrincipalName is empty.
    applied_by: Optional[UserIdentity] = None
    # The date and time when the review decision was applied.
    applied_date_time: Optional[datetime.datetime] = None
    # The outcome of applying the decision, one of: NotApplied, Success, Failed, NotFound, NotSupported.
    apply_result: Optional[str] = None
    # The reviewer's business justification, if supplied.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The result of the review, one of NotReviewed, Deny, DontKnow or Approve.
    review_result: Optional[str] = None
    # The identity of the reviewer. If the recommendation was used as the review, the userPrincipalName is empty.
    reviewed_by: Optional[UserIdentity] = None
    # The reviewedDateTime property
    reviewed_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewDecision:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewDecision
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewDecision()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_identity import UserIdentity

        from .entity import Entity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "accessRecommendation": lambda n : setattr(self, 'access_recommendation', n.get_str_value()),
            "accessReviewId": lambda n : setattr(self, 'access_review_id', n.get_str_value()),
            "appliedBy": lambda n : setattr(self, 'applied_by', n.get_object_value(UserIdentity)),
            "appliedDateTime": lambda n : setattr(self, 'applied_date_time', n.get_datetime_value()),
            "applyResult": lambda n : setattr(self, 'apply_result', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "reviewResult": lambda n : setattr(self, 'review_result', n.get_str_value()),
            "reviewedBy": lambda n : setattr(self, 'reviewed_by', n.get_object_value(UserIdentity)),
            "reviewedDateTime": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
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
        writer.write_str_value("accessRecommendation", self.access_recommendation)
        writer.write_str_value("accessReviewId", self.access_review_id)
        writer.write_object_value("appliedBy", self.applied_by)
        writer.write_datetime_value("appliedDateTime", self.applied_date_time)
        writer.write_str_value("applyResult", self.apply_result)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("reviewResult", self.review_result)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
    

