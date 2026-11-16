from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CorsConfiguration_v2(Entity, Parsable):
    # The request headers that the origin domain may specify on the CORS request. The wildcard character * indicates that any header beginning with the specified prefix is allowed.
    allowed_headers: Optional[list[str]] = None
    # The HTTP request methods that the origin domain may use for a CORS request.
    allowed_methods: Optional[list[str]] = None
    # The origin domains that are permitted to make a request against the service via CORS. The origin domain is the domain from which the request originates. The origin must be an exact case-sensitive match with the origin that the user agent sends to the service.
    allowed_origins: Optional[list[str]] = None
    # The maximum amount of time that a browser should cache the response to the preflight OPTIONS request.
    max_age_in_seconds: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource within the application segment for which CORS permissions are granted. / grants permission for the whole app segment.
    resource: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CorsConfiguration_v2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CorsConfiguration_v2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CorsConfiguration_v2()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "allowedHeaders": lambda n : setattr(self, 'allowed_headers', n.get_collection_of_primitive_values(str)),
            "allowedMethods": lambda n : setattr(self, 'allowed_methods', n.get_collection_of_primitive_values(str)),
            "allowedOrigins": lambda n : setattr(self, 'allowed_origins', n.get_collection_of_primitive_values(str)),
            "maxAgeInSeconds": lambda n : setattr(self, 'max_age_in_seconds', n.get_int_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("allowedHeaders", self.allowed_headers)
        writer.write_collection_of_primitive_values("allowedMethods", self.allowed_methods)
        writer.write_collection_of_primitive_values("allowedOrigins", self.allowed_origins)
        writer.write_int_value("maxAgeInSeconds", self.max_age_in_seconds)
        writer.write_str_value("resource", self.resource)
    

