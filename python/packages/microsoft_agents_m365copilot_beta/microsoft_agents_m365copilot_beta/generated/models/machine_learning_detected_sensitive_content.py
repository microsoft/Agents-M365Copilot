from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detected_sensitive_content import DetectedSensitiveContent
    from .ml_classification_match_tolerance import MlClassificationMatchTolerance

from .detected_sensitive_content import DetectedSensitiveContent

@dataclass
class MachineLearningDetectedSensitiveContent(DetectedSensitiveContent, Parsable):
    # The matchTolerance property
    match_tolerance: Optional[MlClassificationMatchTolerance] = None
    # The modelVersion property
    model_version: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MachineLearningDetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MachineLearningDetectedSensitiveContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MachineLearningDetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .detected_sensitive_content import DetectedSensitiveContent
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance

        from .detected_sensitive_content import DetectedSensitiveContent
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance

        fields: dict[str, Callable[[Any], None]] = {
            "matchTolerance": lambda n : setattr(self, 'match_tolerance', n.get_collection_of_enum_values(MlClassificationMatchTolerance)),
            "modelVersion": lambda n : setattr(self, 'model_version', n.get_str_value()),
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
        writer.write_enum_value("matchTolerance", self.match_tolerance)
        writer.write_str_value("modelVersion", self.model_version)
    

