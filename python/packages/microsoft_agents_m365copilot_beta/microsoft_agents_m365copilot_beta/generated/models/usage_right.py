from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .usage_right_state import UsageRightState

from .entity import Entity

@dataclass
class UsageRight(Entity, Parsable):
    # Product id corresponding to the usage right.
    catalog_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of the service corresponding to the usage right.
    service_identifier: Optional[str] = None
    # The state property
    state: Optional[UsageRightState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageRight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageRight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageRight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .usage_right_state import UsageRightState

        from .entity import Entity
        from .usage_right_state import UsageRightState

        fields: dict[str, Callable[[Any], None]] = {
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
            "serviceIdentifier": lambda n : setattr(self, 'service_identifier', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(UsageRightState)),
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
        writer.write_str_value("catalogId", self.catalog_id)
        writer.write_str_value("serviceIdentifier", self.service_identifier)
        writer.write_enum_value("state", self.state)
    

