from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authorization_system_type_service import AuthorizationSystemTypeService

@dataclass
class GcpScope(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Type of GCP resource.
    resource_type: Optional[str] = None
    # The service property
    service: Optional[AuthorizationSystemTypeService] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authorization_system_type_service import AuthorizationSystemTypeService

        from .authorization_system_type_service import AuthorizationSystemTypeService

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_object_value(AuthorizationSystemTypeService)),
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
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_object_value("service", self.service)
        writer.write_additional_data_value(self.additional_data)
    

