from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .verification_event_detail import VerificationEventDetail
    from .verification_event_lifecycle import VerificationEventLifecycle
    from .verification_event_override import VerificationEventOverride

from .entity import Entity

@dataclass
class IdentityVerificationEvent(Entity, Parsable):
    """
    A single identity verification event with its verification, lifecycle, and optional override details.
    """
    # The source and current lifecycle state of the event.
    lifecycle: Optional[VerificationEventLifecycle] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The administrative or programmatic override applied to the event. null when no override was applied.
    override_details: Optional[VerificationEventOverride] = None
    # The verification state, provider, credential identifiers, and timestamps.
    verification: Optional[VerificationEventDetail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityVerificationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityVerificationEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityVerificationEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .verification_event_detail import VerificationEventDetail
        from .verification_event_lifecycle import VerificationEventLifecycle
        from .verification_event_override import VerificationEventOverride

        from .entity import Entity
        from .verification_event_detail import VerificationEventDetail
        from .verification_event_lifecycle import VerificationEventLifecycle
        from .verification_event_override import VerificationEventOverride

        fields: dict[str, Callable[[Any], None]] = {
            "lifecycle": lambda n : setattr(self, 'lifecycle', n.get_object_value(VerificationEventLifecycle)),
            "overrideDetails": lambda n : setattr(self, 'override_details', n.get_object_value(VerificationEventOverride)),
            "verification": lambda n : setattr(self, 'verification', n.get_object_value(VerificationEventDetail)),
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
        writer.write_object_value("lifecycle", self.lifecycle)
        writer.write_object_value("overrideDetails", self.override_details)
        writer.write_object_value("verification", self.verification)
    

