from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .operation_approval_policy_type import OperationApprovalPolicyType
    from .operation_approval_request_status import OperationApprovalRequestStatus

from .entity import Entity

@dataclass
class OperationApprovalRequest(Entity, Parsable):
    """
    The OperationApprovalRequest entity encompasses the operation an admin wishes to perform and is requesting approval to complete. It contains the detail of the operation one wishes to perform, user metadata of the requestor, and a justification for the change. It allows for several operations for both the requestor and the potential approver to either approve, deny, or cancel the request and a response justification to provide information for the decision.
    """
    # Indicates the justification for approving or rejecting the request. Maximum length of justification is 1024 characters. For example: 'Approved per Change 23423 - needed for Feb 2023 application baseline updates.' Read-only. This property is read-only.
    approval_justification: Optional[str] = None
    # The identity of the approver as an Identity Set. Optionally contains the application ID, the device ID and the User ID. See information about this type here: https://learn.microsoft.com/graph/api/resources/identityset?view=graph-rest-1.0. Read-only. This property is read-only.
    approver: Optional[IdentitySet] = None
    # Indicates the DateTime when any action on the approval request is no longer permitted. The value cannot be modified and is automatically populated when the request is created using expiration offset values defined in the service controllers. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. This property is read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # Indicates the last DateTime that the request was modified. The value cannot be modified and is automatically populated whenever values in the request are updated. For example, when the 'status' property changes from needsApproval to approved. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. This property is read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the DateTime that the request was made. The value cannot be modified and is automatically populated when the request is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default. Read-only. This property is read-only.
    request_date_time: Optional[datetime.datetime] = None
    # Indicates the justification for creating the request. Maximum length of justification is 1024 characters. For example: 'Needed for Feb 2023 application baseline updates.' Read-only. This property is read-only.
    request_justification: Optional[str] = None
    # The identity of the requestor as an Identity Set. Optionally contains the application ID, the device ID and the User ID. See information about this type here: https://learn.microsoft.com/graph/api/resources/identityset?view=graph-rest-1.0. Read-only. This property is read-only.
    requestor: Optional[IdentitySet] = None
    # Indicates the approval policy types required by the request in order for the request to be approved or rejected. Read-only. This property is read-only.
    required_operation_approval_policy_types: Optional[list[OperationApprovalPolicyType]] = None
    # Indicates the status of the Approval Request. The status of a request will change when an action is successfully performed on it, such as when it is `approved` or `rejected`, or when the request's expiration DateTime passes and the result is `expired`.
    status: Optional[OperationApprovalRequestStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperationApprovalRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperationApprovalRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperationApprovalRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .operation_approval_policy_type import OperationApprovalPolicyType
        from .operation_approval_request_status import OperationApprovalRequestStatus

        from .entity import Entity
        from .identity_set import IdentitySet
        from .operation_approval_policy_type import OperationApprovalPolicyType
        from .operation_approval_request_status import OperationApprovalRequestStatus

        fields: dict[str, Callable[[Any], None]] = {
            "approvalJustification": lambda n : setattr(self, 'approval_justification', n.get_str_value()),
            "approver": lambda n : setattr(self, 'approver', n.get_object_value(IdentitySet)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "requestDateTime": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "requestJustification": lambda n : setattr(self, 'request_justification', n.get_str_value()),
            "requestor": lambda n : setattr(self, 'requestor', n.get_object_value(IdentitySet)),
            "requiredOperationApprovalPolicyTypes": lambda n : setattr(self, 'required_operation_approval_policy_types', n.get_collection_of_enum_values(OperationApprovalPolicyType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OperationApprovalRequestStatus)),
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
        writer.write_enum_value("status", self.status)
    

