from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .investigation_output_type import InvestigationOutputType

from .entity import Entity

@dataclass
class InvestigationOutput(Entity, Parsable):
    """
    A read-only stored-file output owned and contained by an investigation session. Inherited id is the existing stable opaque stored-file identifier, unique within its session. Metadata and content reads enforce the same parent-session authorization.
    """
    # The output bytes, retrieved through /security/agenticSecurity/sessions/{session-id}/outputs/{output-id}/content. The stream isn't inline in the metadata response. Read-only.
    content: Optional[bytes] = None
    # Output category: summary text or an artifact, both retrieved through the authenticated content stream.
    kind: Optional[InvestigationOutputType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvestigationOutput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvestigationOutput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvestigationOutput()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .investigation_output_type import InvestigationOutputType

        from .entity import Entity
        from .investigation_output_type import InvestigationOutputType

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(InvestigationOutputType)),
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
    

