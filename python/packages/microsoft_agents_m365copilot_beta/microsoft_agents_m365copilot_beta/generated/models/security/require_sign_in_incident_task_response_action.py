from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .incident_task_response_action import IncidentTaskResponseAction

from .incident_task_response_action import IncidentTaskResponseAction

@dataclass
class RequireSignInIncidentTaskResponseAction(IncidentTaskResponseAction, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.requireSignInIncidentTaskResponseAction"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequireSignInIncidentTaskResponseAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequireSignInIncidentTaskResponseAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequireSignInIncidentTaskResponseAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .incident_task_response_action import IncidentTaskResponseAction

        from .incident_task_response_action import IncidentTaskResponseAction

        fields: dict[str, Callable[[Any], None]] = {
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
    

