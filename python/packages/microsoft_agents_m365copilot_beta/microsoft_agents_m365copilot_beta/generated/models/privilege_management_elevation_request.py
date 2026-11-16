from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .elevation_request_application_detail import ElevationRequestApplicationDetail
    from .elevation_request_state import ElevationRequestState
    from .entity import Entity

from .entity import Entity

@dataclass
class PrivilegeManagementElevationRequest(Entity, Parsable):
    """
    These are elevation approval requests for EPM support arbitrated scenario initiated by IW user that admins can take action on.
    """
    # Details of the application which is being requested to elevate, allowing the admin to understand the identity of the application. It includes file info such as FilePath, FileHash, FilePublisher, and etc. Returned by default. Read-only.
    application_detail: Optional[ElevationRequestApplicationDetail] = None
    # The device name used to initiate the elevation request. For example: 'cotonso-laptop'. Returned by default. Read-only.
    device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the elevation request was submitted/created. The value cannot be modified and is automatically populated when the elevation request is submitted/created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.
    request_created_date_time: Optional[datetime.datetime] = None
    # Expiration set for the request when it was created, regardless of approved or denied status. For example: '2023-08-03T14:24:22Z'. Returned by default. Returned by default. Read-only.
    request_expiry_date_time: Optional[datetime.datetime] = None
    # Justification provided by the end user for the elevation request. For example :'Need to elevate to install microsoft word'. Read-only.
    request_justification: Optional[str] = None
    # The date and time when the elevation request was either submitted/created or approved/denied. The value cannot be modified and is automatically populated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only.
    request_last_modified_date_time: Optional[datetime.datetime] = None
    # The Azure Active Directory (AAD) identifier of the end user who is requesting this elevation. For example: 'F1A57311-B9EB-45B7-9415-8555E68EDC9E'. Returned by default. Read-only.
    requested_by_user_id: Optional[str] = None
    # The User Principal Name (UPN) of the end user who requested this elevation. For example: 'user1@contoso.com'. Returned by default. Read-only.
    requested_by_user_principal_name: Optional[str] = None
    # The Intune Device Identifier of the managed device used to initiate the elevation request. For example: '90F5F6E8-CA09-4811-97F6-4D0DD532D916'. Returned by default. Read-only.
    requested_on_device_id: Optional[str] = None
    # This is the Azure Active Directory (AAD) user id of the administrator who approved or denied the request. For example: 'F1A57311-B9EB-45B7-9415-8555E68EDC9E'. This field would be String.Empty before the request is either approved or denied. Read-only.
    review_completed_by_user_id: Optional[str] = None
    # This is the User Principal Name (UPN) of the administrator who approved or denied the request. For example: 'admin@contoso.com'. This field would be String.Empty before the request is either approved or denied. Read-only.
    review_completed_by_user_principal_name: Optional[str] = None
    # The DateTime for which the request was approved or denied. For example, midnight UTC on August 3rd, 2023 would look like this: '2023-08-03T00:00:00Z'. Read-only.
    review_completed_date_time: Optional[datetime.datetime] = None
    # An optional justification provided by approver at approval or denied time. This field will be String.Empty if approver decides to not provide a justification. For example: 'Run this installer today'
    reviewer_justification: Optional[str] = None
    # Indicates state of elevation request
    status: Optional[ElevationRequestState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegeManagementElevationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegeManagementElevationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegeManagementElevationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .elevation_request_application_detail import ElevationRequestApplicationDetail
        from .elevation_request_state import ElevationRequestState
        from .entity import Entity

        from .elevation_request_application_detail import ElevationRequestApplicationDetail
        from .elevation_request_state import ElevationRequestState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "applicationDetail": lambda n : setattr(self, 'application_detail', n.get_object_value(ElevationRequestApplicationDetail)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "requestCreatedDateTime": lambda n : setattr(self, 'request_created_date_time', n.get_datetime_value()),
            "requestExpiryDateTime": lambda n : setattr(self, 'request_expiry_date_time', n.get_datetime_value()),
            "requestJustification": lambda n : setattr(self, 'request_justification', n.get_str_value()),
            "requestLastModifiedDateTime": lambda n : setattr(self, 'request_last_modified_date_time', n.get_datetime_value()),
            "requestedByUserId": lambda n : setattr(self, 'requested_by_user_id', n.get_str_value()),
            "requestedByUserPrincipalName": lambda n : setattr(self, 'requested_by_user_principal_name', n.get_str_value()),
            "requestedOnDeviceId": lambda n : setattr(self, 'requested_on_device_id', n.get_str_value()),
            "reviewCompletedByUserId": lambda n : setattr(self, 'review_completed_by_user_id', n.get_str_value()),
            "reviewCompletedByUserPrincipalName": lambda n : setattr(self, 'review_completed_by_user_principal_name', n.get_str_value()),
            "reviewCompletedDateTime": lambda n : setattr(self, 'review_completed_date_time', n.get_datetime_value()),
            "reviewerJustification": lambda n : setattr(self, 'reviewer_justification', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ElevationRequestState)),
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
        writer.write_object_value("applicationDetail", self.application_detail)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("requestCreatedDateTime", self.request_created_date_time)
        writer.write_datetime_value("requestExpiryDateTime", self.request_expiry_date_time)
        writer.write_str_value("requestJustification", self.request_justification)
        writer.write_datetime_value("requestLastModifiedDateTime", self.request_last_modified_date_time)
        writer.write_str_value("requestedByUserId", self.requested_by_user_id)
        writer.write_str_value("requestedByUserPrincipalName", self.requested_by_user_principal_name)
        writer.write_str_value("requestedOnDeviceId", self.requested_on_device_id)
        writer.write_str_value("reviewCompletedByUserId", self.review_completed_by_user_id)
        writer.write_str_value("reviewCompletedByUserPrincipalName", self.review_completed_by_user_principal_name)
        writer.write_datetime_value("reviewCompletedDateTime", self.review_completed_date_time)
        writer.write_str_value("reviewerJustification", self.reviewer_justification)
        writer.write_enum_value("status", self.status)
    

