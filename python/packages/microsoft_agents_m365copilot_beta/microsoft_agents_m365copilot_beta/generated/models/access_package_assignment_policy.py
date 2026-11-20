from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_notification_settings import AccessPackageNotificationSettings
    from .access_package_question import AccessPackageQuestion
    from .approval_settings import ApprovalSettings
    from .assignment_review_settings import AssignmentReviewSettings
    from .custom_extension_handler import CustomExtensionHandler
    from .custom_extension_stage_setting import CustomExtensionStageSetting
    from .entity import Entity
    from .requestor_settings import RequestorSettings
    from .verifiable_credential_settings import VerifiableCredentialSettings

from .entity import Entity

@dataclass
class AccessPackageAssignmentPolicy(Entity, Parsable):
    # The access package with this policy. Read-only. Nullable. Supports $expand.
    access_package: Optional[AccessPackage] = None
    # The accessPackageCatalog property
    access_package_catalog: Optional[AccessPackageCatalog] = None
    # Identifier of the access package.
    access_package_id: Optional[str] = None
    # Represents the settings for email notifications for requests to an access package.
    access_package_notification_settings: Optional[AccessPackageNotificationSettings] = None
    # Who must review, and how often, the assignments to the access package from this policy. This property is null if reviews aren't required.
    access_review_settings: Optional[AssignmentReviewSettings] = None
    # Indicates whether a user can extend the access package assignment duration after approval.
    can_extend: Optional[bool] = None
    # The createdBy property
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
    custom_extension_handlers: Optional[list[CustomExtensionHandler]] = None
    # The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
    custom_extension_stage_settings: Optional[list[CustomExtensionStageSetting]] = None
    # The description of the policy.
    description: Optional[str] = None
    # The display name of the policy. Supports $filter (eq).
    display_name: Optional[str] = None
    # The number of days in which assignments from this policy last until they're expired.
    duration_in_days: Optional[int] = None
    # The expiration date for assignments created in this policy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    expiration_date_time: Optional[datetime.datetime] = None
    # The modifiedBy property
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Questions that are posed to the  requestor.
    questions: Optional[list[AccessPackageQuestion]] = None
    # Who must approve requests for access package in this policy.
    request_approval_settings: Optional[ApprovalSettings] = None
    # Who can request this access package from this policy.
    requestor_settings: Optional[RequestorSettings] = None
    # Settings for verifiable credentials set up through the Microsoft Entra Verified I D service. These settings represent the verifiable credentials that a requestor of an access package in this policy can present to be assigned the access package.
    verifiable_credential_settings: Optional[VerifiableCredentialSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_notification_settings import AccessPackageNotificationSettings
        from .access_package_question import AccessPackageQuestion
        from .approval_settings import ApprovalSettings
        from .assignment_review_settings import AssignmentReviewSettings
        from .custom_extension_handler import CustomExtensionHandler
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .entity import Entity
        from .requestor_settings import RequestorSettings
        from .verifiable_credential_settings import VerifiableCredentialSettings

        from .access_package import AccessPackage
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_notification_settings import AccessPackageNotificationSettings
        from .access_package_question import AccessPackageQuestion
        from .approval_settings import ApprovalSettings
        from .assignment_review_settings import AssignmentReviewSettings
        from .custom_extension_handler import CustomExtensionHandler
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .entity import Entity
        from .requestor_settings import RequestorSettings
        from .verifiable_credential_settings import VerifiableCredentialSettings

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackage": lambda n : setattr(self, 'access_package', n.get_object_value(AccessPackage)),
            "accessPackageCatalog": lambda n : setattr(self, 'access_package_catalog', n.get_object_value(AccessPackageCatalog)),
            "accessPackageId": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
            "accessPackageNotificationSettings": lambda n : setattr(self, 'access_package_notification_settings', n.get_object_value(AccessPackageNotificationSettings)),
            "accessReviewSettings": lambda n : setattr(self, 'access_review_settings', n.get_object_value(AssignmentReviewSettings)),
            "canExtend": lambda n : setattr(self, 'can_extend', n.get_bool_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customExtensionHandlers": lambda n : setattr(self, 'custom_extension_handlers', n.get_collection_of_object_values(CustomExtensionHandler)),
            "customExtensionStageSettings": lambda n : setattr(self, 'custom_extension_stage_settings', n.get_collection_of_object_values(CustomExtensionStageSetting)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(AccessPackageQuestion)),
            "requestApprovalSettings": lambda n : setattr(self, 'request_approval_settings', n.get_object_value(ApprovalSettings)),
            "requestorSettings": lambda n : setattr(self, 'requestor_settings', n.get_object_value(RequestorSettings)),
            "verifiableCredentialSettings": lambda n : setattr(self, 'verifiable_credential_settings', n.get_object_value(VerifiableCredentialSettings)),
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
        writer.write_object_value("accessPackage", self.access_package)
        writer.write_object_value("accessPackageCatalog", self.access_package_catalog)
        writer.write_str_value("accessPackageId", self.access_package_id)
        writer.write_object_value("accessPackageNotificationSettings", self.access_package_notification_settings)
        writer.write_object_value("accessReviewSettings", self.access_review_settings)
        writer.write_bool_value("canExtend", self.can_extend)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("customExtensionHandlers", self.custom_extension_handlers)
        writer.write_collection_of_object_values("customExtensionStageSettings", self.custom_extension_stage_settings)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("requestApprovalSettings", self.request_approval_settings)
        writer.write_object_value("requestorSettings", self.requestor_settings)
        writer.write_object_value("verifiableCredentialSettings", self.verifiable_credential_settings)
    

