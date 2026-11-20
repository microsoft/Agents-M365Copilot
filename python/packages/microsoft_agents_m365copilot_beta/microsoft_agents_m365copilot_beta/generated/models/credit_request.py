from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .credit_request_state import CreditRequestState
    from .credit_request_type import CreditRequestType
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class CreditRequest(Entity, Parsable):
    """
    A credit request submitted by a user and acted on by an administrator.Derives from entity; the client-visible identifier is id.ETag-based optimistic concurrency is enforced via the standard OData ETag mechanism.Individual PATCH uses If-Match; the bulk action uses each item's etag field.
    """
    # The date and time the request was created.
    created_date_time: Optional[datetime.datetime] = None
    # The identity of the administrator who approved or rejected the request.Only the user facet is populated. Null until the request is decided.
    decision_by: Optional[IdentitySet] = None
    # The date and time the request expires. The backing service sets this to 90 days aftercreation and resets it to 90 days after a state-changing update.
    expiration_date_time: Optional[datetime.datetime] = None
    # The date and time the request was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason or trigger that caused a credit request to be created.
    request_type: Optional[CreditRequestType] = None
    # The requestedBy property
    requested_by: Optional[IdentitySet] = None
    # The open, extensible service identifier associated with this credit request,using the same values as other Copilot Cost Management APIs, such as cowork and workIQ.
    service_id: Optional[str] = None
    # The state of a credit request in the approval workflow.
    state: Optional[CreditRequestState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreditRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreditRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreditRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .credit_request_state import CreditRequestState
        from .credit_request_type import CreditRequestType
        from .entity import Entity
        from .identity_set import IdentitySet

        from .credit_request_state import CreditRequestState
        from .credit_request_type import CreditRequestType
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "decisionBy": lambda n : setattr(self, 'decision_by', n.get_object_value(IdentitySet)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "requestType": lambda n : setattr(self, 'request_type', n.get_enum_value(CreditRequestType)),
            "requestedBy": lambda n : setattr(self, 'requested_by', n.get_object_value(IdentitySet)),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(CreditRequestState)),
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
        writer.write_enum_value("requestType", self.request_type)
        writer.write_object_value("requestedBy", self.requested_by)
        writer.write_enum_value("state", self.state)
    

