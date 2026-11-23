from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .investigation_input_type import InvestigationInputType

from .entity import Entity

@dataclass
class InvestigationInput(Entity, Parsable):
    """
    An addressable reference to an external resource or keyword, contained only by an investigation session and shared as session context across its agent runs. It does not identify the exact input consumed by an individual run. The referenced resource remains external. Inherited id is server-owned, stable and unique within the containing session. New input ids are persisted GUIDs. Historical immutable input records retain deterministic parent-and-slot GUIDs without rewriting stored business identifiers.
    """
    # The display name populated by the service when available. Read-only.
    display_name: Optional[str] = None
    # Kind of external resource identifier or keyword supplied to a playbook.
    kind: Optional[InvestigationInputType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type-specific resource identifier or keyword text. Required when creating a session and immutable afterward.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationInput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationInput()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .investigation_input_type import InvestigationInputType

        from .entity import Entity
        from .investigation_input_type import InvestigationInputType

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(InvestigationInputType)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_enum_value("kind", self.kind)
        writer.write_str_value("value", self.value)
    

