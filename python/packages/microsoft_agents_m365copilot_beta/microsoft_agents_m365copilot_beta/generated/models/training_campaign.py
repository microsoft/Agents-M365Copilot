from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_target_content import AccountTargetContent
    from .campaign_schedule import CampaignSchedule
    from .email_identity import EmailIdentity
    from .end_user_notification_setting import EndUserNotificationSetting
    from .entity import Entity
    from .training_campaign_report import TrainingCampaignReport
    from .training_setting import TrainingSetting

from .entity import Entity

@dataclass
class TrainingCampaign(Entity, Parsable):
    # Details about the schedule and current status for a training campaign
    campaign_schedule: Optional[CampaignSchedule] = None
    # Identity of the user who created the training campaign
    created_by: Optional[EmailIdentity] = None
    # Date and time of creation of the training campaign.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the training campaign.
    description: Optional[str] = None
    # Display name of the training campaign. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Details about the end user notification setting.
    end_user_notification_setting: Optional[EndUserNotificationSetting] = None
    # Users excluded from the training campaign.
    excluded_account_target: Optional[AccountTargetContent] = None
    # Users targeted in the training campaign.
    included_account_target: Optional[AccountTargetContent] = None
    # Identity of the user who most recently modified the training campaign.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time of the most recent modification of the training campaign.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Report of the training campaign.
    report: Optional[TrainingCampaignReport] = None
    # Details about the training settings for a training campaign.
    training_setting: Optional[TrainingSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrainingCampaign:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingCampaign
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrainingCampaign()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .account_target_content import AccountTargetContent
        from .campaign_schedule import CampaignSchedule
        from .email_identity import EmailIdentity
        from .end_user_notification_setting import EndUserNotificationSetting
        from .entity import Entity
        from .training_campaign_report import TrainingCampaignReport
        from .training_setting import TrainingSetting

        from .account_target_content import AccountTargetContent
        from .campaign_schedule import CampaignSchedule
        from .email_identity import EmailIdentity
        from .end_user_notification_setting import EndUserNotificationSetting
        from .entity import Entity
        from .training_campaign_report import TrainingCampaignReport
        from .training_setting import TrainingSetting

        fields: dict[str, Callable[[Any], None]] = {
            "campaignSchedule": lambda n : setattr(self, 'campaign_schedule', n.get_object_value(CampaignSchedule)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endUserNotificationSetting": lambda n : setattr(self, 'end_user_notification_setting', n.get_object_value(EndUserNotificationSetting)),
            "excludedAccountTarget": lambda n : setattr(self, 'excluded_account_target', n.get_object_value(AccountTargetContent)),
            "includedAccountTarget": lambda n : setattr(self, 'included_account_target', n.get_object_value(AccountTargetContent)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "report": lambda n : setattr(self, 'report', n.get_object_value(TrainingCampaignReport)),
            "trainingSetting": lambda n : setattr(self, 'training_setting', n.get_object_value(TrainingSetting)),
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
        writer.write_object_value("campaignSchedule", self.campaign_schedule)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endUserNotificationSetting", self.end_user_notification_setting)
        writer.write_object_value("excludedAccountTarget", self.excluded_account_target)
        writer.write_object_value("includedAccountTarget", self.included_account_target)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("report", self.report)
        writer.write_object_value("trainingSetting", self.training_setting)
    

