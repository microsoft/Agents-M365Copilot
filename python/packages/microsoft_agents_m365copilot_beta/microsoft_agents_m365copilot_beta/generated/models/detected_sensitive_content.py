from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_attribute import ClassificationAttribute
    from .classification_method import ClassificationMethod
    from .detected_sensitive_content_base import DetectedSensitiveContentBase
    from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
    from .sensitive_content_location import SensitiveContentLocation
    from .sensitive_type_scope import SensitiveTypeScope
    from .sensitive_type_source import SensitiveTypeSource

from .detected_sensitive_content_base import DetectedSensitiveContentBase

@dataclass
class DetectedSensitiveContent(DetectedSensitiveContentBase, Parsable):
    # The classificationAttributes property
    classification_attributes: Optional[list[ClassificationAttribute]] = None
    # The classificationMethod property
    classification_method: Optional[ClassificationMethod] = None
    # The matches property
    matches: Optional[list[SensitiveContentLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope property
    scope: Optional[SensitiveTypeScope] = None
    # The sensitiveTypeSource property
    sensitive_type_source: Optional[SensitiveTypeSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectedSensitiveContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectedSensitiveContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.machineLearningDetectedSensitiveContent".casefold():
            from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent

            return MachineLearningDetectedSensitiveContent()
        return DetectedSensitiveContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .classification_attribute import ClassificationAttribute
        from .classification_method import ClassificationMethod
        from .detected_sensitive_content_base import DetectedSensitiveContentBase
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
        from .sensitive_content_location import SensitiveContentLocation
        from .sensitive_type_scope import SensitiveTypeScope
        from .sensitive_type_source import SensitiveTypeSource

        from .classification_attribute import ClassificationAttribute
        from .classification_method import ClassificationMethod
        from .detected_sensitive_content_base import DetectedSensitiveContentBase
        from .machine_learning_detected_sensitive_content import MachineLearningDetectedSensitiveContent
        from .sensitive_content_location import SensitiveContentLocation
        from .sensitive_type_scope import SensitiveTypeScope
        from .sensitive_type_source import SensitiveTypeSource

        fields: dict[str, Callable[[Any], None]] = {
            "classificationAttributes": lambda n : setattr(self, 'classification_attributes', n.get_collection_of_object_values(ClassificationAttribute)),
            "classificationMethod": lambda n : setattr(self, 'classification_method', n.get_enum_value(ClassificationMethod)),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(SensitiveContentLocation)),
            "scope": lambda n : setattr(self, 'scope', n.get_collection_of_enum_values(SensitiveTypeScope)),
            "sensitiveTypeSource": lambda n : setattr(self, 'sensitive_type_source', n.get_enum_value(SensitiveTypeSource)),
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
        writer.write_collection_of_object_values("classificationAttributes", self.classification_attributes)
        writer.write_enum_value("classificationMethod", self.classification_method)
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_enum_value("scope", self.scope)
        writer.write_enum_value("sensitiveTypeSource", self.sensitive_type_source)
    

