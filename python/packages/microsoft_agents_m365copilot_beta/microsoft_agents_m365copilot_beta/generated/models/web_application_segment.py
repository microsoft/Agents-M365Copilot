from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_segment import ApplicationSegment
    from .cors_configuration_v2 import CorsConfiguration_v2

from .application_segment import ApplicationSegment

@dataclass
class WebApplicationSegment(ApplicationSegment, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.webApplicationSegment"
    # If you're configuring a traffic manager in front of multiple app proxy application segments, this property contains the user-friendly URL that points to the traffic manager.
    alternate_url: Optional[str] = None
    # A collection of CORS Rule definitions for a particular application segment.
    cors_configurations: Optional[list[CorsConfiguration_v2]] = None
    # The published external URL for the application segment; for example, https://intranet.contoso.com/.
    external_url: Optional[str] = None
    # The internal URL of the application segment; for example, https://intranet/.
    internal_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplicationSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationSegment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebApplicationSegment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_segment import ApplicationSegment
        from .cors_configuration_v2 import CorsConfiguration_v2

        from .application_segment import ApplicationSegment
        from .cors_configuration_v2 import CorsConfiguration_v2

        fields: dict[str, Callable[[Any], None]] = {
            "alternateUrl": lambda n : setattr(self, 'alternate_url', n.get_str_value()),
            "corsConfigurations": lambda n : setattr(self, 'cors_configurations', n.get_collection_of_object_values(CorsConfiguration_v2)),
            "externalUrl": lambda n : setattr(self, 'external_url', n.get_str_value()),
            "internalUrl": lambda n : setattr(self, 'internal_url', n.get_str_value()),
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
        writer.write_str_value("alternateUrl", self.alternate_url)
        writer.write_collection_of_object_values("corsConfigurations", self.cors_configurations)
        writer.write_str_value("externalUrl", self.external_url)
        writer.write_str_value("internalUrl", self.internal_url)
    

