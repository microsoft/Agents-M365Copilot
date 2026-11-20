from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .named_location import NamedLocation

from .named_location import NamedLocation

@dataclass
class ServiceTagNamedLocation(NamedLocation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.serviceTagNamedLocation"
    # The isTrusted property
    is_trusted: Optional[bool] = None
    # The serviceTags property
    service_tags: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceTagNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceTagNamedLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceTagNamedLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .named_location import NamedLocation

        from .named_location import NamedLocation

        fields: dict[str, Callable[[Any], None]] = {
            "isTrusted": lambda n : setattr(self, 'is_trusted', n.get_bool_value()),
            "serviceTags": lambda n : setattr(self, 'service_tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("isTrusted", self.is_trusted)
        writer.write_collection_of_primitive_values("serviceTags", self.service_tags)
    

