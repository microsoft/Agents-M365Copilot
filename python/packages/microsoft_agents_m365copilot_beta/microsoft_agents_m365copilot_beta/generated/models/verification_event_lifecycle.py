from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .verification_event_lifecycle_state import VerificationEventLifecycleState
    from .verification_lifecycle_source import VerificationLifecycleSource

@dataclass
class VerificationEventLifecycle(AdditionalDataHolder, Parsable):
    """
    Lifecycle tracking for a verification event, indicating who triggered it and its current state.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The service-populated timestamp for an event in the invalidated lifecycle state. Otherwise, null. Read-only.
    invalidated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source property
    source: Optional[VerificationLifecycleSource] = None
    # The state property
    state: Optional[VerificationEventLifecycleState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerificationEventLifecycle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerificationEventLifecycle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerificationEventLifecycle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .verification_event_lifecycle_state import VerificationEventLifecycleState
        from .verification_lifecycle_source import VerificationLifecycleSource

        from .verification_event_lifecycle_state import VerificationEventLifecycleState
        from .verification_lifecycle_source import VerificationLifecycleSource

        fields: dict[str, Callable[[Any], None]] = {
            "invalidatedDateTime": lambda n : setattr(self, 'invalidated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(VerificationLifecycleSource)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(VerificationEventLifecycleState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

