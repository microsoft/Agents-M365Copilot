from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .environment_kind import EnvironmentKind

from ..entity import Entity

@dataclass
class Environment(Entity, Parsable):
    """
    Represents a single cloud environment onboarded for security posture management.
    """
    # The kind of cloud environment onboarded to security posture management.
    kind: Optional[EnvironmentKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Environment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Environment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Environment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .environment_kind import EnvironmentKind

        from ..entity import Entity
        from .environment_kind import EnvironmentKind

        fields: dict[str, Callable[[Any], None]] = {
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(EnvironmentKind)),
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
        writer.write_enum_value("kind", self.kind)
    

