from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
    from .gcp_identity import GcpIdentity

from .gcp_identity import GcpIdentity

@dataclass
class GcpCloudFunction(GcpIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.gcpCloudFunction"
    # Represents the resources in an authorization system..
    resource: Optional[GcpAuthorizationSystemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GcpCloudFunction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GcpCloudFunction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GcpCloudFunction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_identity import GcpIdentity

        from .gcp_authorization_system_resource import GcpAuthorizationSystemResource
        from .gcp_identity import GcpIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(GcpAuthorizationSystemResource)),
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
        writer.write_object_value("resource", self.resource)
    

