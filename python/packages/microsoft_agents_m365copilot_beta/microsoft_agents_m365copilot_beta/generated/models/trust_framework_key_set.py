from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .trust_framework_key import TrustFrameworkKey
    from .trust_framework_key_v2 import TrustFrameworkKey_v2

from .entity import Entity

@dataclass
class TrustFrameworkKeySet(Entity, Parsable):
    # A collection of the keys.
    keys: Optional[list[TrustFrameworkKey]] = None
    # A collection of the keys.
    keys_v2: Optional[list[TrustFrameworkKey_v2]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrustFrameworkKeySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrustFrameworkKeySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TrustFrameworkKeySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .trust_framework_key import TrustFrameworkKey
        from .trust_framework_key_v2 import TrustFrameworkKey_v2

        from .entity import Entity
        from .trust_framework_key import TrustFrameworkKey
        from .trust_framework_key_v2 import TrustFrameworkKey_v2

        fields: dict[str, Callable[[Any], None]] = {
            "keys": lambda n : setattr(self, 'keys', n.get_collection_of_object_values(TrustFrameworkKey)),
            "keys_v2": lambda n : setattr(self, 'keys_v2', n.get_collection_of_object_values(TrustFrameworkKey_v2)),
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
        writer.write_collection_of_object_values("keys", self.keys)
        writer.write_collection_of_object_values("keys_v2", self.keys_v2)
    

