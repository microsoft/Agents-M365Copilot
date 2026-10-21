from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .email_content_threat_submission import EmailContentThreatSubmission
    from .email_threat_submission import EmailThreatSubmission
    from .email_url_threat_submission import EmailUrlThreatSubmission
    from .file_content_threat_submission import FileContentThreatSubmission
    from .file_threat_submission import FileThreatSubmission
    from .file_url_threat_submission import FileUrlThreatSubmission
    from .long_running_operation_status import LongRunningOperationStatus
    from .submission_admin_review import SubmissionAdminReview
    from .submission_category import SubmissionCategory
    from .submission_client_source import SubmissionClientSource
    from .submission_content_type import SubmissionContentType
    from .submission_result import SubmissionResult
    from .submission_source import SubmissionSource
    from .submission_user_identity import SubmissionUserIdentity
    from .url_threat_submission import UrlThreatSubmission

from ..entity import Entity

@dataclass
class ThreatSubmission(Entity, Parsable):
    # Specifies the admin review property that constitutes of who reviewed the user submission, when and what was it identified as.
    admin_review: Optional[SubmissionAdminReview] = None
    # The category property
    category: Optional[SubmissionCategory] = None
    # Specifies the source of the submission. The possible values are: microsoft, other, and unkownFutureValue.
    client_source: Optional[SubmissionClientSource] = None
    # Specifies the type of content being submitted. The possible values are: email, url, file, app, and unkownFutureValue.
    content_type: Optional[SubmissionContentType] = None
    # Specifies who submitted the email as a threat. Supports $filter = createdBy/email eq 'value'.
    created_by: Optional[SubmissionUserIdentity] = None
    # Specifies when the threat submission was created. Supports $filter = createdDateTime ge 2022-01-01T00:00:00Z and createdDateTime lt 2022-01-02T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the result of the analysis performed by Microsoft.
    result: Optional[SubmissionResult] = None
    # Specifies the role of the submitter. Supports $filter = source eq 'value'. The possible values are: administrator,  user, and unkownFutureValue.
    source: Optional[SubmissionSource] = None
    # Indicates whether the threat submission has been analyzed by Microsoft. Supports $filter = status eq 'value'. The possible values are: notStarted, running, succeeded, failed, skipped, and unkownFutureValue.
    status: Optional[LongRunningOperationStatus] = None
    # Indicates the tenant id of the submitter. Not required when created using a POST operation. It's extracted from the token of the post API call.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThreatSubmission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailContentThreatSubmission".casefold():
            from .email_content_threat_submission import EmailContentThreatSubmission

            return EmailContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailThreatSubmission".casefold():
            from .email_threat_submission import EmailThreatSubmission

            return EmailThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.emailUrlThreatSubmission".casefold():
            from .email_url_threat_submission import EmailUrlThreatSubmission

            return EmailUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileContentThreatSubmission".casefold():
            from .file_content_threat_submission import FileContentThreatSubmission

            return FileContentThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileThreatSubmission".casefold():
            from .file_threat_submission import FileThreatSubmission

            return FileThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.fileUrlThreatSubmission".casefold():
            from .file_url_threat_submission import FileUrlThreatSubmission

            return FileUrlThreatSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.urlThreatSubmission".casefold():
            from .url_threat_submission import UrlThreatSubmission

            return UrlThreatSubmission()
        return ThreatSubmission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .email_content_threat_submission import EmailContentThreatSubmission
        from .email_threat_submission import EmailThreatSubmission
        from .email_url_threat_submission import EmailUrlThreatSubmission
        from .file_content_threat_submission import FileContentThreatSubmission
        from .file_threat_submission import FileThreatSubmission
        from .file_url_threat_submission import FileUrlThreatSubmission
        from .long_running_operation_status import LongRunningOperationStatus
        from .submission_admin_review import SubmissionAdminReview
        from .submission_category import SubmissionCategory
        from .submission_client_source import SubmissionClientSource
        from .submission_content_type import SubmissionContentType
        from .submission_result import SubmissionResult
        from .submission_source import SubmissionSource
        from .submission_user_identity import SubmissionUserIdentity
        from .url_threat_submission import UrlThreatSubmission

        from ..entity import Entity
        from .email_content_threat_submission import EmailContentThreatSubmission
        from .email_threat_submission import EmailThreatSubmission
        from .email_url_threat_submission import EmailUrlThreatSubmission
        from .file_content_threat_submission import FileContentThreatSubmission
        from .file_threat_submission import FileThreatSubmission
        from .file_url_threat_submission import FileUrlThreatSubmission
        from .long_running_operation_status import LongRunningOperationStatus
        from .submission_admin_review import SubmissionAdminReview
        from .submission_category import SubmissionCategory
        from .submission_client_source import SubmissionClientSource
        from .submission_content_type import SubmissionContentType
        from .submission_result import SubmissionResult
        from .submission_source import SubmissionSource
        from .submission_user_identity import SubmissionUserIdentity
        from .url_threat_submission import UrlThreatSubmission

        fields: dict[str, Callable[[Any], None]] = {
            "adminReview": lambda n : setattr(self, 'admin_review', n.get_object_value(SubmissionAdminReview)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(SubmissionCategory)),
            "clientSource": lambda n : setattr(self, 'client_source', n.get_enum_value(SubmissionClientSource)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_enum_value(SubmissionContentType)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(SubmissionUserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "result": lambda n : setattr(self, 'result', n.get_object_value(SubmissionResult)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(SubmissionSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_object_value("adminReview", self.admin_review)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("clientSource", self.client_source)
        writer.write_enum_value("contentType", self.content_type)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("result", self.result)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("tenantId", self.tenant_id)
    

