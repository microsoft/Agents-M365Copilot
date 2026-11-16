from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .block_page_configuration_base import BlockPageConfigurationBase
    from .status import Status

from ..entity import Entity

@dataclass
class CustomBlockPage(Entity, Parsable):
    # The current configuration of the customized message. The body can be input in limited markdown language, supporting links via the format: link.
    configuration: Optional[BlockPageConfigurationBase] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[Status] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomBlockPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomBlockPage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomBlockPage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .block_page_configuration_base import BlockPageConfigurationBase
        from .status import Status

        from ..entity import Entity
        from .block_page_configuration_base import BlockPageConfigurationBase
        from .status import Status

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(BlockPageConfigurationBase)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(Status)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_enum_value("state", self.state)
    

