from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tls_inspection_destination import TlsInspectionDestination

from .tls_inspection_destination import TlsInspectionDestination

@dataclass
class TlsInspectionFqdnDestination(TlsInspectionDestination, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.networkaccess.tlsInspectionFqdnDestination"
    # A collection of fully qualified domain names to match against. The special value * represents any domain. Wildcard patterns can be used in domain names (for example: *.contoso.com). This collection cannot be empty or null.
    values: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TlsInspectionFqdnDestination:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TlsInspectionFqdnDestination
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TlsInspectionFqdnDestination()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tls_inspection_destination import TlsInspectionDestination

        from .tls_inspection_destination import TlsInspectionDestination

        fields: dict[str, Callable[[Any], None]] = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("values", self.values)
    

