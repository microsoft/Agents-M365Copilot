from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .exact_match_data_store_base import ExactMatchDataStoreBase
    from .exact_match_session import ExactMatchSession

from .exact_match_data_store_base import ExactMatchDataStoreBase

@dataclass
class ExactMatchDataStore(ExactMatchDataStoreBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The sessions property
    sessions: Optional[list[ExactMatchSession]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExactMatchDataStore:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDataStore
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExactMatchDataStore()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .exact_match_data_store_base import ExactMatchDataStoreBase
        from .exact_match_session import ExactMatchSession

        from .exact_match_data_store_base import ExactMatchDataStoreBase
        from .exact_match_session import ExactMatchSession

        fields: dict[str, Callable[[Any], None]] = {
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(ExactMatchSession)),
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
        writer.write_collection_of_object_values("sessions", self.sessions)
    

