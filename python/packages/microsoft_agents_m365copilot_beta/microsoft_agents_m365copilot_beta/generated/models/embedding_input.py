from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chunk_offsets import ChunkOffsets

@dataclass
class EmbeddingInput(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional offset metadata for the text chunks that produced this embedding data. The starts property is required when chunkOffsets is present. When lengths is also present, the decoded element counts must match and pair by index.
    chunk_offsets: Optional[ChunkOffsets] = None
    # The embedding vectors the model produced for the text, encoded as a base64 string of little-endian 32-bit floats. Every vector the model emitted (for example, one per text chunk) is concatenated in order; each contributes exactly the modelType's embedding dimension worth of float components, so the decoded length must be a whole multiple of that dimension.
    data: Optional[str] = None
    # The embedding model identifier drawn from the service allow-list (for example: text-embedding-3-small-512). Unique (case-insensitive) within the embeddings collection; entries whose modelType is outside the allow-list are rejected with a 400.
    model_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmbeddingInput:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddingInput
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmbeddingInput()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chunk_offsets import ChunkOffsets

        from .chunk_offsets import ChunkOffsets

        fields: dict[str, Callable[[Any], None]] = {
            "chunkOffsets": lambda n : setattr(self, 'chunk_offsets', n.get_object_value(ChunkOffsets)),
            "data": lambda n : setattr(self, 'data', n.get_str_value()),
            "modelType": lambda n : setattr(self, 'model_type', n.get_str_value()),
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
        writer.write_object_value("chunkOffsets", self.chunk_offsets)
        writer.write_str_value("data", self.data)
        writer.write_str_value("modelType", self.model_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

