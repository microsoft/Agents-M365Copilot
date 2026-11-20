from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provenance_actor_type import ProvenanceActorType

@dataclass
class ProvenanceAssertedBy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The identifier of the actor that established the provenance.
    actor_id: Optional[str] = None
    # The actorType property
    actor_type: Optional[ProvenanceActorType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvenanceAssertedBy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvenanceAssertedBy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvenanceAssertedBy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provenance_actor_type import ProvenanceActorType

        from .provenance_actor_type import ProvenanceActorType

        fields: dict[str, Callable[[Any], None]] = {
            "actorId": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "actorType": lambda n : setattr(self, 'actor_type', n.get_enum_value(ProvenanceActorType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("actorId", self.actor_id)
        writer.write_enum_value("actorType", self.actor_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

