from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_class_group_attributes import AdditionalClassGroupAttributes
    from .additional_class_group_options import AdditionalClassGroupOptions
    from .enrollment_mappings import EnrollmentMappings

@dataclass
class ClassGroupConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The different attributes to sync for the class groups. The possible values are: courseTitle, courseCode, courseSubject, courseGradeLevel, courseExternalId, academicSessionTitle, academicSessionExternalId, classCode, unknownFutureValue.
    additional_attributes: Optional[list[AdditionalClassGroupAttributes]] = None
    # The additionalOptions property
    additional_options: Optional[AdditionalClassGroupOptions] = None
    # The enrollmentMappings property
    enrollment_mappings: Optional[EnrollmentMappings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClassGroupConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClassGroupConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClassGroupConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .additional_class_group_attributes import AdditionalClassGroupAttributes
        from .additional_class_group_options import AdditionalClassGroupOptions
        from .enrollment_mappings import EnrollmentMappings

        from .additional_class_group_attributes import AdditionalClassGroupAttributes
        from .additional_class_group_options import AdditionalClassGroupOptions
        from .enrollment_mappings import EnrollmentMappings

        fields: dict[str, Callable[[Any], None]] = {
            "additionalAttributes": lambda n : setattr(self, 'additional_attributes', n.get_collection_of_enum_values(AdditionalClassGroupAttributes)),
            "additionalOptions": lambda n : setattr(self, 'additional_options', n.get_object_value(AdditionalClassGroupOptions)),
            "enrollmentMappings": lambda n : setattr(self, 'enrollment_mappings', n.get_object_value(EnrollmentMappings)),
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
        writer.write_collection_of_enum_values("additionalAttributes", self.additional_attributes)
        writer.write_object_value("additionalOptions", self.additional_options)
        writer.write_object_value("enrollmentMappings", self.enrollment_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

