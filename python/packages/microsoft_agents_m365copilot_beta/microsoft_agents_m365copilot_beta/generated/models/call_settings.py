from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegation_settings import DelegationSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class CallSettings(Entity, Parsable):
    # Represents the delegate settings.
    delegates: Optional[list[DelegationSettings]] = None
    # Represents the delegator settings.
    delegators: Optional[list[DelegationSettings]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delegation_settings import DelegationSettings
        from .entity import Entity

        from .delegation_settings import DelegationSettings
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "delegates": lambda n : setattr(self, 'delegates', n.get_collection_of_object_values(DelegationSettings)),
            "delegators": lambda n : setattr(self, 'delegators', n.get_collection_of_object_values(DelegationSettings)),
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
        writer.write_collection_of_object_values("delegates", self.delegates)
        writer.write_collection_of_object_values("delegators", self.delegators)
    

