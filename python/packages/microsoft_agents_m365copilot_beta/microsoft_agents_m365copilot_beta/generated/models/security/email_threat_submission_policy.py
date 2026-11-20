from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class EmailThreatSubmissionPolicy(Entity, Parsable):
    # Specifies the email address of the sender from which email notifications will be sent to end users to inform them whether an email is spam, phish or clean. The default value is null. Optional for creation.
    customized_notification_sender_email_address: Optional[str] = None
    # Specifies the destination where the reported messages from end users land whenever they report something as phish, junk or not junk. The default value is null. Optional for creation.
    customized_report_recipient_email_address: Optional[str] = None
    # Indicates whether end users can report a message as spam, phish or junk directly without a confirmation(popup). The default value is true.  Optional for creation.
    is_always_report_enabled_for_users: Optional[bool] = None
    # Indicates whether end users can confirm using a popup before reporting messages as spam, phish or not junk. The default value is true.  Optional for creation.
    is_ask_me_enabled_for_users: Optional[bool] = None
    # Indicates whether the email notifications sent to end users to inform them if an email is a phish mail, spam or junk is customized or not. The default value is false. Optional for creation.
    is_customized_message_enabled: Optional[bool] = None
    # If enabled, customized message only shows when email is reported as phishing. The default value is false. Optional for creation.
    is_customized_message_enabled_for_phishing: Optional[bool] = None
    # Indicates whether to use the sender email address set using customizedNotificationSenderEmailAddress for sending email notifications to end users. The default value is false. Optional for creation.
    is_customized_notification_sender_enabled: Optional[bool] = None
    # Indicates whether end users can move the message from one folder to another based on the action of spam, phish or not junk without actually reporting it. The default value is true. Optional for creation.
    is_never_report_enabled_for_users: Optional[bool] = None
    # Indicates whether the branding logo should be used in the email notifications sent to end users. The default value is false. Optional for creation.
    is_organization_branding_enabled: Optional[bool] = None
    # Indicates whether end users can submit from the quarantine page. The default value is true. Optional for creation.
    is_report_from_quarantine_enabled: Optional[bool] = None
    # Indicates whether emails reported by end users should be sent to the custom mailbox configured using customizedReportRecipientEmailAddress.  The default value is false. Optional for creation.
    is_report_to_customized_email_address_enabled: Optional[bool] = None
    # If enabled, the email is sent to Microsoft for analysis. The default value is false. Required for creation.
    is_report_to_microsoft_enabled: Optional[bool] = None
    # Indicates whether an email notification is sent to the end user who reported the email when it has been reviewed by the admin. The default value is false. Optional for creation.
    is_review_email_notification_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailThreatSubmissionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailThreatSubmissionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailThreatSubmissionPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "customizedNotificationSenderEmailAddress": lambda n : setattr(self, 'customized_notification_sender_email_address', n.get_str_value()),
            "customizedReportRecipientEmailAddress": lambda n : setattr(self, 'customized_report_recipient_email_address', n.get_str_value()),
            "isAlwaysReportEnabledForUsers": lambda n : setattr(self, 'is_always_report_enabled_for_users', n.get_bool_value()),
            "isAskMeEnabledForUsers": lambda n : setattr(self, 'is_ask_me_enabled_for_users', n.get_bool_value()),
            "isCustomizedMessageEnabled": lambda n : setattr(self, 'is_customized_message_enabled', n.get_bool_value()),
            "isCustomizedMessageEnabledForPhishing": lambda n : setattr(self, 'is_customized_message_enabled_for_phishing', n.get_bool_value()),
            "isCustomizedNotificationSenderEnabled": lambda n : setattr(self, 'is_customized_notification_sender_enabled', n.get_bool_value()),
            "isNeverReportEnabledForUsers": lambda n : setattr(self, 'is_never_report_enabled_for_users', n.get_bool_value()),
            "isOrganizationBrandingEnabled": lambda n : setattr(self, 'is_organization_branding_enabled', n.get_bool_value()),
            "isReportFromQuarantineEnabled": lambda n : setattr(self, 'is_report_from_quarantine_enabled', n.get_bool_value()),
            "isReportToCustomizedEmailAddressEnabled": lambda n : setattr(self, 'is_report_to_customized_email_address_enabled', n.get_bool_value()),
            "isReportToMicrosoftEnabled": lambda n : setattr(self, 'is_report_to_microsoft_enabled', n.get_bool_value()),
            "isReviewEmailNotificationEnabled": lambda n : setattr(self, 'is_review_email_notification_enabled', n.get_bool_value()),
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
        writer.write_str_value("customizedNotificationSenderEmailAddress", self.customized_notification_sender_email_address)
        writer.write_str_value("customizedReportRecipientEmailAddress", self.customized_report_recipient_email_address)
        writer.write_bool_value("isAlwaysReportEnabledForUsers", self.is_always_report_enabled_for_users)
        writer.write_bool_value("isAskMeEnabledForUsers", self.is_ask_me_enabled_for_users)
        writer.write_bool_value("isCustomizedMessageEnabled", self.is_customized_message_enabled)
        writer.write_bool_value("isCustomizedMessageEnabledForPhishing", self.is_customized_message_enabled_for_phishing)
        writer.write_bool_value("isCustomizedNotificationSenderEnabled", self.is_customized_notification_sender_enabled)
        writer.write_bool_value("isNeverReportEnabledForUsers", self.is_never_report_enabled_for_users)
        writer.write_bool_value("isOrganizationBrandingEnabled", self.is_organization_branding_enabled)
        writer.write_bool_value("isReportFromQuarantineEnabled", self.is_report_from_quarantine_enabled)
        writer.write_bool_value("isReportToCustomizedEmailAddressEnabled", self.is_report_to_customized_email_address_enabled)
        writer.write_bool_value("isReportToMicrosoftEnabled", self.is_report_to_microsoft_enabled)
        writer.write_bool_value("isReviewEmailNotificationEnabled", self.is_review_email_notification_enabled)
    

