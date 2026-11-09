from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .submission_detected_file import SubmissionDetectedFile
    from .submission_result_category import SubmissionResultCategory
    from .submission_result_detail import SubmissionResultDetail
    from .user_mailbox_setting import UserMailboxSetting

@dataclass
class SubmissionResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The submission result category. The possible values are: notJunk, spam, phishing, malware, allowedByPolicy, blockedByPolicy, spoof, unknown, noResultAvailable, unknownFutureValue, beingAnalyzed, notSubmittedToMicrosoft, phishingSimulation, allowedDueToOrganizationOverride, blockedDueToOrganizationOverride, allowedDueToUserOverride, blockedDueToUserOverride, itemNotfound, threatsFound, noThreatsFound, domainImpersonation, userImpersonation, brandImpersonation, authenticationFailure, spoofedBlocked, spoofedAllowed, bulk, and reasonLostInTransit. You must use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: beingAnalyzed, notSubmittedToMicrosoft, phishingSimulation, allowedDueToOrganizationOverride, blockedDueToOrganizationOverride, allowedDueToUserOverride, blockedDueToUserOverride, itemNotfound, threatsFound, noThreatsFound, domainImpersonation, userImpersonation, brandImpersonation, authenticationFailure, spoofedBlocked, spoofedAllowed, bulk, and reasonLostInTransit.
    category: Optional[SubmissionResultCategory] = None
    # Specifies the extra details provided by Microsoft to substantiate their analysis result.
    detail: Optional[SubmissionResultDetail] = None
    # Specifies the files detected by Microsoft in the submitted emails.
    detected_files: Optional[list[SubmissionDetectedFile]] = None
    # Specifies the URLs detected by Microsoft in the submitted email.
    detected_urls: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the setting for user mailbox denoted by a comma-separated string.
    user_mailbox_setting: Optional[UserMailboxSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubmissionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubmissionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SubmissionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .submission_detected_file import SubmissionDetectedFile
        from .submission_result_category import SubmissionResultCategory
        from .submission_result_detail import SubmissionResultDetail
        from .user_mailbox_setting import UserMailboxSetting

        from .submission_detected_file import SubmissionDetectedFile
        from .submission_result_category import SubmissionResultCategory
        from .submission_result_detail import SubmissionResultDetail
        from .user_mailbox_setting import UserMailboxSetting

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(SubmissionResultCategory)),
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(SubmissionResultDetail)),
            "detectedFiles": lambda n : setattr(self, 'detected_files', n.get_collection_of_object_values(SubmissionDetectedFile)),
            "detectedUrls": lambda n : setattr(self, 'detected_urls', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userMailboxSetting": lambda n : setattr(self, 'user_mailbox_setting', n.get_collection_of_enum_values(UserMailboxSetting)),
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
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("detail", self.detail)
        writer.write_collection_of_object_values("detectedFiles", self.detected_files)
        writer.write_collection_of_primitive_values("detectedUrls", self.detected_urls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("userMailboxSetting", self.user_mailbox_setting)
        writer.write_additional_data_value(self.additional_data)
    

