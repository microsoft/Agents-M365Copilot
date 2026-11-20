from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_request_content_meta_data import ClassificationRequestContentMetaData
    from .embedding_input import EmbeddingInput
    from .entity import Entity
    from .ml_classification_match_tolerance import MlClassificationMatchTolerance
    from .sensitive_type_scope import SensitiveTypeScope

from .entity import Entity

@dataclass
class TextClassificationRequest(Entity, Parsable):
    # Metadata that describes the content being classified.
    content_meta_data: Optional[ClassificationRequestContentMetaData] = None
    # Optional caller-supplied precomputed embeddings for the text, so the service can skip recomputing them. Embeddings for models outside the allow-list are rejected with a 400.
    embeddings: Optional[list[EmbeddingInput]] = None
    # The file extension of the content being classified.
    file_extension: Optional[str] = None
    # The match tolerance levels to include in the classification results. The possible values are: exact, near.
    match_tolerances_to_include: Optional[MlClassificationMatchTolerance] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The document scopes over which to run classification. The possible values are: fullDocument, partialDocument.
    scopes_to_run: Optional[SensitiveTypeScope] = None
    # The identifiers of the sensitive information types to evaluate against the text.
    sensitive_type_ids: Optional[list[str]] = None
    # The text to classify.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TextClassificationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TextClassificationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TextClassificationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_request_content_meta_data import ClassificationRequestContentMetaData
        from .embedding_input import EmbeddingInput
        from .entity import Entity
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance
        from .sensitive_type_scope import SensitiveTypeScope

        from .classification_request_content_meta_data import ClassificationRequestContentMetaData
        from .embedding_input import EmbeddingInput
        from .entity import Entity
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance
        from .sensitive_type_scope import SensitiveTypeScope

        fields: dict[str, Callable[[Any], None]] = {
            "contentMetaData": lambda n : setattr(self, 'content_meta_data', n.get_object_value(ClassificationRequestContentMetaData)),
            "embeddings": lambda n : setattr(self, 'embeddings', n.get_collection_of_object_values(EmbeddingInput)),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "matchTolerancesToInclude": lambda n : setattr(self, 'match_tolerances_to_include', n.get_collection_of_enum_values(MlClassificationMatchTolerance)),
            "scopesToRun": lambda n : setattr(self, 'scopes_to_run', n.get_collection_of_enum_values(SensitiveTypeScope)),
            "sensitiveTypeIds": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_object_value("contentMetaData", self.content_meta_data)
        writer.write_collection_of_object_values("embeddings", self.embeddings)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_enum_value("matchTolerancesToInclude", self.match_tolerances_to_include)
        writer.write_enum_value("scopesToRun", self.scopes_to_run)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_str_value("text", self.text)
    

