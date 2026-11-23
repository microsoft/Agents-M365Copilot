from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_verification_event import IdentityVerificationEvent
    from .verification_state import VerificationState

from .entity import Entity

@dataclass
class IdentityVerificationStatus(Entity, Parsable):
    """
    Per-user singleton tracking identity verification state and bounded event history.
    """
    # The effective expiry of the user's overall verified state, computed as the latest expiresDateTime across active verification events. null when no active event has an expiry. Read-only.
    expiry_date_time: Optional[datetime.datetime] = None
    # The date and time of the most recent successful identity verification. null when state is unverified. Read-only.
    last_verified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[VerificationState] = None
    # The user's recent verification events, automatically included when the status is retrieved. Contains up to 10 events, ordered by recency. Older events are removed when the limit is reached.
    verification_events: Optional[list[IdentityVerificationEvent]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityVerificationStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityVerificationStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityVerificationStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_verification_event import IdentityVerificationEvent
        from .verification_state import VerificationState

        from .entity import Entity
        from .identity_verification_event import IdentityVerificationEvent
        from .verification_state import VerificationState

        fields: dict[str, Callable[[Any], None]] = {
            "expiryDateTime": lambda n : setattr(self, 'expiry_date_time', n.get_datetime_value()),
            "lastVerifiedDateTime": lambda n : setattr(self, 'last_verified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(VerificationState)),
            "verificationEvents": lambda n : setattr(self, 'verification_events', n.get_collection_of_object_values(IdentityVerificationEvent)),
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
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("verificationEvents", self.verification_events)
    

