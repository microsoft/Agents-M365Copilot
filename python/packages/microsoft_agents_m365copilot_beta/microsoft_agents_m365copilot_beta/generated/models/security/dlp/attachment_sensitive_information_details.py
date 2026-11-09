from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sensitive_information_detailed_confidence_level_result import SensitiveInformationDetailedConfidenceLevelResult

@dataclass
class AttachmentSensitiveInformationDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitiveInformationDetailedClassificationAttributes property
    sensitive_information_detailed_classification_attributes: Optional[list[SensitiveInformationDetailedConfidenceLevelResult]] = None
    # The sensitiveInformationDetectionIndices property
    sensitive_information_detection_indices: Optional[list[int]] = None
    # The sensitiveType property
    sensitive_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttachmentSensitiveInformationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttachmentSensitiveInformationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttachmentSensitiveInformationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sensitive_information_detailed_confidence_level_result import SensitiveInformationDetailedConfidenceLevelResult

        from .sensitive_information_detailed_confidence_level_result import SensitiveInformationDetailedConfidenceLevelResult

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sensitiveInformationDetailedClassificationAttributes": lambda n : setattr(self, 'sensitive_information_detailed_classification_attributes', n.get_collection_of_object_values(SensitiveInformationDetailedConfidenceLevelResult)),
            "sensitiveInformationDetectionIndices": lambda n : setattr(self, 'sensitive_information_detection_indices', n.get_collection_of_primitive_values(int)),
            "sensitiveType": lambda n : setattr(self, 'sensitive_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("sensitiveInformationDetailedClassificationAttributes", self.sensitive_information_detailed_classification_attributes)
        writer.write_collection_of_primitive_values("sensitiveInformationDetectionIndices", self.sensitive_information_detection_indices)
        writer.write_str_value("sensitiveType", self.sensitive_type)
        writer.write_additional_data_value(self.additional_data)
    

