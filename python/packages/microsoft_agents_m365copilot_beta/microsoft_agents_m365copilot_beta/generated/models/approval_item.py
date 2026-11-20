from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_identity_set import ApprovalIdentitySet
    from .approval_item_request import ApprovalItemRequest
    from .approval_item_response import ApprovalItemResponse
    from .approval_item_state import ApprovalItemState
    from .approval_item_type import ApprovalItemType
    from .approval_item_view_point import ApprovalItemViewPoint
    from .entity import Entity

from .entity import Entity

@dataclass
class ApprovalItem(Entity, Parsable):
    # Indicates whether the approval item can be canceled.
    allow_cancel: Optional[bool] = None
    # Indicates whether email notification is enabled.
    allow_email_notification: Optional[bool] = None
    # The workflow type of the approval item. The possible values are: basic, basicAwaitAll, custom, customAwaitAll. Required.
    approval_type: Optional[ApprovalItemType] = None
    # The identity of the principals to whom the approval item was initially assigned. Required.
    approvers: Optional[list[ApprovalIdentitySet]] = None
    # Approval request completion date and time. Read-only.
    completed_date_time: Optional[datetime.datetime] = None
    # Creation date and time of the approval request. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The description of the approval request.
    description: Optional[str] = None
    # The displayName of the approval request. Required.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity set of the principal who owns the approval item. Only provide a value for this property when creating an approval item on behalf of the principal. If the owner field isn't provided, the user information from the user context is used.
    owner: Optional[ApprovalIdentitySet] = None
    # A collection of requests created for each approver on the approval item.
    requests: Optional[list[ApprovalItemRequest]] = None
    # Approval response prompts. Only provide a value for this property when creating a custom approval item. For custom approval items, supply two response prompt strings. The default response prompts are 'Approve' and 'Reject'.
    response_prompts: Optional[list[str]] = None
    # A collection of responses created for the approval item.
    responses: Optional[list[ApprovalItemResponse]] = None
    # The result field is only populated once the approval item is in its final state. The result of the approval item is based on the approvalType. For basic approval items, the result is either 'Approved' or 'Rejected'. For custom approval items, the result could either be a single response or multiple responses separated by a semi-colon. Read-only.
    result: Optional[str] = None
    # The approval item state. The possible values are: canceled, created, pending, completed. Read-only.
    state: Optional[ApprovalItemState] = None
    # Represents user viewpoints data on the ApprovalItem. The data includes the users roles regarding the approval item. Read-only.
    view_point: Optional[ApprovalItemViewPoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_identity_set import ApprovalIdentitySet
        from .approval_item_request import ApprovalItemRequest
        from .approval_item_response import ApprovalItemResponse
        from .approval_item_state import ApprovalItemState
        from .approval_item_type import ApprovalItemType
        from .approval_item_view_point import ApprovalItemViewPoint
        from .entity import Entity

        from .approval_identity_set import ApprovalIdentitySet
        from .approval_item_request import ApprovalItemRequest
        from .approval_item_response import ApprovalItemResponse
        from .approval_item_state import ApprovalItemState
        from .approval_item_type import ApprovalItemType
        from .approval_item_view_point import ApprovalItemViewPoint
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowCancel": lambda n : setattr(self, 'allow_cancel', n.get_bool_value()),
            "allowEmailNotification": lambda n : setattr(self, 'allow_email_notification', n.get_bool_value()),
            "approvalType": lambda n : setattr(self, 'approval_type', n.get_enum_value(ApprovalItemType)),
            "approvers": lambda n : setattr(self, 'approvers', n.get_collection_of_object_values(ApprovalIdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(ApprovalIdentitySet)),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(ApprovalItemRequest)),
            "responsePrompts": lambda n : setattr(self, 'response_prompts', n.get_collection_of_primitive_values(str)),
            "responses": lambda n : setattr(self, 'responses', n.get_collection_of_object_values(ApprovalItemResponse)),
            "result": lambda n : setattr(self, 'result', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ApprovalItemState)),
            "viewPoint": lambda n : setattr(self, 'view_point', n.get_object_value(ApprovalItemViewPoint)),
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
        writer.write_bool_value("allowEmailNotification", self.allow_email_notification)
        writer.write_enum_value("approvalType", self.approval_type)
        writer.write_collection_of_object_values("approvers", self.approvers)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("requests", self.requests)
        writer.write_collection_of_primitive_values("responsePrompts", self.response_prompts)
        writer.write_collection_of_object_values("responses", self.responses)
    

