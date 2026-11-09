from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .related_resource import RelatedResource

from .related_resource import RelatedResource

@dataclass
class RelatedThreatIntelligence(RelatedResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.relatedThreatIntelligence"
    # Number of threats detected by threat intelligence. Required.
    threat_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedThreatIntelligence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedThreatIntelligence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedThreatIntelligence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .related_resource import RelatedResource

        from .related_resource import RelatedResource

        fields: dict[str, Callable[[Any], None]] = {
            "threatCount": lambda n : setattr(self, 'threat_count', n.get_int_value()),
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
        writer.write_int_value("threatCount", self.threat_count)
    

