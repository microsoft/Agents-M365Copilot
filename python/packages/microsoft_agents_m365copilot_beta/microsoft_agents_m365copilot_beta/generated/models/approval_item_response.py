from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval_identity_set import ApprovalIdentitySet
    from .entity import Entity

from .entity import Entity

@dataclass
class ApprovalItemResponse(Entity, Parsable):
    # The comment made by the approver.
    comments: Optional[str] = None
    # The identity set of the approver.
    created_by: Optional[ApprovalIdentitySet] = None
    # Creation date and time of the response.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity set of the principal who owns the approval item.
    owners: Optional[list[ApprovalIdentitySet]] = None
    # Approver response based on the response options. The default response options are 'Approved' and 'Rejected'. The approval item creator can also define custom response options during approval item creation.
    response: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalItemResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalItemResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalItemResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval_identity_set import ApprovalIdentitySet
        from .entity import Entity

        from .approval_identity_set import ApprovalIdentitySet
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "comments": lambda n : setattr(self, 'comments', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(ApprovalIdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(ApprovalIdentitySet)),
            "response": lambda n : setattr(self, 'response', n.get_str_value()),
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
        writer.write_str_value("comments", self.comments)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("response", self.response)
    

