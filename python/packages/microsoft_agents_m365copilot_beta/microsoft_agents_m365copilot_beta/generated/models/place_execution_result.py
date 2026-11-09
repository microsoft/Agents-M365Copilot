from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place
    from .public_error import PublicError

@dataclass
class PlaceExecutionResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The upsert results of children places of the place.
    children: Optional[list[PlaceExecutionResult]] = None
    # The error that occurred during the upsert of the place.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The succeededPlace property
    succeeded_place: Optional[Place] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlaceExecutionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlaceExecutionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlaceExecutionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place
        from .public_error import PublicError

        from .place import Place
        from .public_error import PublicError

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(PlaceExecutionResult)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "succeededPlace": lambda n : setattr(self, 'succeeded_place', n.get_object_value(Place)),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("succeededPlace", self.succeeded_place)
        writer.write_additional_data_value(self.additional_data)
    

