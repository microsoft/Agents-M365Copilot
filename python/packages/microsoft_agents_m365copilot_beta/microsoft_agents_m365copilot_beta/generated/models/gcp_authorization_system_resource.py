from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_resource import AuthorizationSystemResource
    from .authorization_system_type_service import AuthorizationSystemTypeService

from .authorization_system_resource import AuthorizationSystemResource

@dataclass
class GcpAuthorizationSystemResource(AuthorizationSystemResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpAuthorizationSystemResource"
    # The service associated with the resource in a GCP authorization system. This object is autoexpanded.
    service: Optional[AuthorizationSystemTypeService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpAuthorizationSystemResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpAuthorizationSystemResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpAuthorizationSystemResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_service import AuthorizationSystemTypeService

        from .authorization_system_resource import AuthorizationSystemResource
        from .authorization_system_type_service import AuthorizationSystemTypeService

        fields: dict[str, Callable[[Any], None]] = {
            "service": lambda n : setattr(self, 'service', n.get_object_value(AuthorizationSystemTypeService)),
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
        writer.write_object_value("service", self.service)
    

