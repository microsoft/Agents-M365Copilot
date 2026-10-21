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
class ApprovalItemRequest(Entity, Parsable):
    # The identity set of the principal assigned to this request.
    approver: Optional[ApprovalIdentitySet] = None
    # Creation date and time for the request.
    created_date_time: Optional[datetime.datetime] = None
    # Indicates whether a request was reassigned.
    is_reassigned: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identity set of the principal who reassigned the request.
    reassigned_from: Optional[ApprovalIdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalItemRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalItemRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalItemRequest()
    
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
            "approver": lambda n : setattr(self, 'approver', n.get_object_value(ApprovalIdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isReassigned": lambda n : setattr(self, 'is_reassigned', n.get_bool_value()),
            "reassignedFrom": lambda n : setattr(self, 'reassigned_from', n.get_object_value(ApprovalIdentitySet)),
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
    

