from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_recurrence_settings import AccessReviewRecurrenceSettings
    from .auto_review_settings import AutoReviewSettings
    from .business_flow_settings import BusinessFlowSettings

@dataclass
class AccessReviewSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether showing recommendations to reviewers is enabled.
    access_recommendations_enabled: Optional[bool] = None
    # The number of days of user activities to show to reviewers.
    activity_duration_in_days: Optional[int] = None
    # Indicates whether the auto-apply capability, to automatically change the target object access resource, is enabled.  If not enabled, a user must, after the review completes, apply the access review.
    auto_apply_review_results_enabled: Optional[bool] = None
    # Indicates whether a decision should be set if the reviewer didn't supply one. For use when, auto-apply is enabled. If you don't want to have a review decision recorded unless the reviewer makes an explicit choice, set it to false.
    auto_review_enabled: Optional[bool] = None
    # Detailed settings for how the feature should set the review decision. For use when, auto-apply is enabled.
    auto_review_settings: Optional[AutoReviewSettings] = None
    # Indicates whether reviewers are required to provide a justification when reviewing access.
    justification_required_on_approval: Optional[bool] = None
    # Indicates whether sending mails to reviewers and the review creator is enabled.
    mail_notifications_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Detailed settings for recurrence.
    recurrence_settings: Optional[AccessReviewRecurrenceSettings] = None
    # Indicates whether sending reminder emails to reviewers is enabled.
    reminders_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessFlowSettings".casefold():
            from .business_flow_settings import BusinessFlowSettings

            return BusinessFlowSettings()
        return AccessReviewSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_recurrence_settings import AccessReviewRecurrenceSettings
        from .auto_review_settings import AutoReviewSettings
        from .business_flow_settings import BusinessFlowSettings

        from .access_review_recurrence_settings import AccessReviewRecurrenceSettings
        from .auto_review_settings import AutoReviewSettings
        from .business_flow_settings import BusinessFlowSettings

        fields: dict[str, Callable[[Any], None]] = {
            "accessRecommendationsEnabled": lambda n : setattr(self, 'access_recommendations_enabled', n.get_bool_value()),
            "activityDurationInDays": lambda n : setattr(self, 'activity_duration_in_days', n.get_int_value()),
            "autoApplyReviewResultsEnabled": lambda n : setattr(self, 'auto_apply_review_results_enabled', n.get_bool_value()),
            "autoReviewEnabled": lambda n : setattr(self, 'auto_review_enabled', n.get_bool_value()),
            "autoReviewSettings": lambda n : setattr(self, 'auto_review_settings', n.get_object_value(AutoReviewSettings)),
            "justificationRequiredOnApproval": lambda n : setattr(self, 'justification_required_on_approval', n.get_bool_value()),
            "mailNotificationsEnabled": lambda n : setattr(self, 'mail_notifications_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrenceSettings": lambda n : setattr(self, 'recurrence_settings', n.get_object_value(AccessReviewRecurrenceSettings)),
            "remindersEnabled": lambda n : setattr(self, 'reminders_enabled', n.get_bool_value()),
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
        writer.write_bool_value("accessRecommendationsEnabled", self.access_recommendations_enabled)
        writer.write_int_value("activityDurationInDays", self.activity_duration_in_days)
        writer.write_bool_value("autoApplyReviewResultsEnabled", self.auto_apply_review_results_enabled)
        writer.write_bool_value("autoReviewEnabled", self.auto_review_enabled)
        writer.write_object_value("autoReviewSettings", self.auto_review_settings)
        writer.write_bool_value("justificationRequiredOnApproval", self.justification_required_on_approval)
        writer.write_bool_value("mailNotificationsEnabled", self.mail_notifications_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrenceSettings", self.recurrence_settings)
        writer.write_bool_value("remindersEnabled", self.reminders_enabled)
        writer.write_additional_data_value(self.additional_data)
    

